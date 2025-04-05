from dotenv import load_dotenv
import os
import requests
import pandas as pd
import base64
import json
import time

# Cargar variables de entorno
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


def get_spotify_token(client_id, client_secret):
    """Obtiene un token de acceso de Spotify utilizando las credenciales del cliente."""

    url = "https://accounts.spotify.com/api/token"

    auth_str = f"{client_id}:{client_secret}"
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}

    auth_response = requests.post(url, headers=headers, data=data)
    
    if auth_response.status_code == 200:
        json_result = json.loads(auth_response.content)
        token = json_result["access_token"]
        return token

    else:
        print(f"FIRST Error {auth_response.status_code}: {auth_response.text}")
        return None


def get_auth_header(token):
    """Devuelve el encabezado de autorización para las solicitudes a la API de Spotify."""

    return {"Authorization": f"Bearer {token}"}


def get_paginated_data(url, headers, item_key, ids, limit=50):
    """Obtiene datos paginados en bloques de 'limit' elementos."""

    results = []

    for i in range(0, len(ids), limit):
        batch_ids = ids[i:i + limit]

        try:
            response = requests.get(f"{url}?ids={','.join(batch_ids)}", headers=headers)
            print(f"Status Code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")
            continue  # Continúa con la siguiente iteración en caso de error

        if response.status_code == 200:
            if response.text:
                try:
                    response_json = response.json()
                    results.extend(response_json.get(item_key, []))

                except ValueError:
                    print("Error al decodificar la respuesta JSON")
                    continue
            else:
                print("Respuesta vacía")

        elif response.status_code == 429:
            retry_after = response.headers.get("Retry-After")

            if retry_after:
                print(f"Límite de solicitudes alcanzado. Esperando {retry_after} segundos.")
                time.sleep(int(retry_after))
            else:
                print("Límite de solicitudes alcanzado. Esperando 30 segundos antes de reintentar.")
                time.sleep(30)
        else:
            print(f"Error: {response.status_code} - {response.text}")

    return results


def get_track_data(token, track_ids, desired_data, limit=50):
    """Obtiene datos de las canciones y sus artistas a partir de los IDs de las canciones."""

    headers = get_auth_header(token)

    # Obtener datos de las canciones con paginación
    track_url = "https://api.spotify.com/v1/tracks"
    tracks_data = get_paginated_data(track_url, headers, "tracks", track_ids, limit)

    # Obtener IDs de artistas sin duplicados para optimizar la consulta
    artist_ids = list(set(artist["id"] for track in tracks_data for artist in track["artists"]))

    # Obtener datos de los artistas con paginación
    artists_url = "https://api.spotify.com/v1/artists"
    artists_data = get_paginated_data(artists_url, headers, "artists", artist_ids, limit)

    # Crear un diccionario para buscar artistas por su ID
    artists_dict = {artist["id"]: artist for artist in artists_data}

    results = []

    for track in tracks_data:
        track_info = {}
        first_artist_id = track["artists"][0]["id"]
        artist_data = artists_dict.get(first_artist_id, {})

        if "album" in desired_data and "album" in track:
            track_info["album_name"] = track["album"]["name"]
        if "release_date" in desired_data and "album" in track:
            track_info["release_date"] = track["album"].get("release_date", "Unknown")
        if "explicit" in desired_data:
            track_info["explicit"] = track.get("explicit", "Unknown")
        if "genre" in desired_data and "genres" in artist_data:
            track_info["genre"] = artist_data.get("genres", ["Others"])[0]
        if "followers" in desired_data and "followers" in artist_data:
            track_info["followers"] = artist_data["followers"].get("total", "Unknown")

        results.append(track_info)

    return results
