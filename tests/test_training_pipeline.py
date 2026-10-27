
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from src.train import load_data, train_model, evaluate_model


def test_load_data_returns_correct_shapes():
    X_train, X_test, y_train, y_test = load_data()

    assert len(X_train) == 120
    assert len(X_test) == 30
    assert len(y_train) == 120
    assert len(y_test) == 30


def test_train_model_returns_fitted_model():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(X_train, y_train)

    assert hasattr(model, "predict")
    assert model.n_estimators == 100
    assert model.predict(X_test).shape == (30,)


def test_evaluate_model_returns_accuracy_and_report():
    X_train, X_test, y_train, y_test = load_data()

    model = train_model(X_train, y_train)
    accuracy, report = evaluate_model(model, X_test, y_test)

    assert 0.0 <= accuracy <= 1.0
    assert isinstance(report, str)
    assert "precision" in report
    assert "recall" in report

