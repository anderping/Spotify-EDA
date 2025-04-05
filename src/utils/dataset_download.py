import kagglehub
import pandas as pd
from functions import save_data
import os


os.chdir(fr"C:\Users\defco\OneDrive\Escritorio\Cursos\Programación\Cursados\Data Science Bootcamp\Spotify EDA\src\utils")


fuente1 = "https://www.kaggle.com/datasets/tomigelo/spotify-audio-features"
tracks1_path = kagglehub.dataset_download("tomigelo/spotify-audio-features")
tracks1 = pd.read_csv(fr"{tracks1_path}\SpotifyAudioFeaturesApril2019.csv")

fuente2 = "https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset"
tracks2_path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")
tracks2 = pd.read_csv(fr"{tracks2_path}\dataset.csv")


save_data(tracks1, "SpotifyAudioFeaturesApril2019.csv")
save_data(tracks2, "popularity_dataset.csv") 
