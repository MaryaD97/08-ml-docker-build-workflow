from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from preprocess import load_data, preprocess_data

def train():
    df = load_data("data/sample.csv")
    X, y = preprocess_data(df)

    model = LogisticRegression()
    model.fit(X, y)

    predictions = model.predict(X)
    acc = accuracy_score(y, predictions)

    print(f"Training Accuracy: {acc}")

if __name__ == "__main__":
    train()

