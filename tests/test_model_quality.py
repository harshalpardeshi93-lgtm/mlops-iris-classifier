
from sklearn.metrics import accuracy_score, f1_score

from src.train import load_data, train_model


def test_model_meets_minimum_accuracy():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    assert accuracy >= 0.80


def test_model_predictions_have_valid_classes():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)

    assert set(predictions).issubset({0, 1, 2})


def test_model_meets_minimum_macro_f1():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)

    score = f1_score(y_test, predictions, average="macro")

    assert score >= 0.80

