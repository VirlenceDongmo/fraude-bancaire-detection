"""Tests unitaires de base pour le module preprocessing."""

import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from preprocessing import clean_data, split_data


def test_clean_data_removes_duplicates():
    df = pd.DataFrame({
        "Amount": [10, 10, 20],
        "Class": [0, 0, 1],
    })
    cleaned = clean_data(df)
    assert len(cleaned) == 2


def test_split_data_stratifies_classes():
    df = pd.DataFrame({
        "Amount": range(20),
        "Class": [0] * 18 + [1] * 2,
    })
    X_train, X_test, y_train, y_test = split_data(df, test_size=0.5)
    assert len(X_train) == len(X_test) == 10
    assert y_train.sum() >= 1  # au moins une fraude dans le train
