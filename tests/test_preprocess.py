import pandas as pd
from src.preprocess import preprocess_data

def test_preprocess():
    df = pd.DataFrame({
        "feature1": [1, 2],
        "feature2": [3, 4],
        "label": [0, 1]
    })

    X, y = preprocess_data(df)

    assert "label" not in X.columns
    assert len(y) == 2
