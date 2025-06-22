import os
from pathlib import Path

############# DATA INGESTION  ################

RAW_DIR = "artifacts/raw"
CONFIG_PATH = "config/config.yaml"

############ DATA PROCESSING #############

PROCESSED_DIR = "artifacts/processed"
ANIMELIST_CSV = "artifacts/raw/animelist.csv"
ANIME_CSV = "artifacts/raw/anime.csv"
ANIME_SYNOPSIS_CSV = "artifacts/raw/anime_with_synopsis.csv"

X_TRAIN_ARRAY = os.path.join(PROCESSED_DIR,"X_train_array.pkl")
X_TEST_ARRAY = os.path.join(PROCESSED_DIR,"X_test_array.pkl")
Y_TRAIN_ARRAY = os.path.join(PROCESSED_DIR,"y_train_array.pkl")
Y_TEST_ARRAY = os.path.join(PROCESSED_DIR,"y_test_array.pkl")

RATING_DF = os.path.join(PROCESSED_DIR,"rating_df.csv")
DF_PATH = os.path.join(PROCESSED_DIR,"anime_df.csv")
SYNOPSIS_DF = os.path.join(PROCESSED_DIR,"synopsis.csv")

USER2USERENCODE = "artifacts\processed\user2userencoded.pkl"
USER2USERDECODE = "artifacts\processed\user2userdecoded.pkl"

