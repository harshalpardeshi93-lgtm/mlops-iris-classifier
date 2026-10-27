import pandas as pd
import pytest

from src.pipeline.validate import validate, DataValidationError


def valid_data():
    return {
        "sepal length (cm)": [5.1],
        "sepal width (cm)": [3.5],
        "petal length (cm)": [1.4],
        "petal width (cm)": [0.2],
        "species": ["setosa"],
        "sepal_area": [17.85],
        "petal_area": [0.28],
        "sepal_to_petal_length_ratio": [5.1 / 1.4],
        "petal_length_bin": ["short"],
    }


def test_validate_accepts_valid_data(tmp_path):
    input_file = tmp_path / "valid.csv"
    pd.DataFrame(valid_data()).to_csv(input_file, index=False)

    result = validate(str(input_file))

    assert len(result) == 1
    assert result["species"].iloc[0] == "setosa"


def test_validate_rejects_invalid_species(tmp_path):
    input_file = tmp_path / "invalid.csv"
    data = valid_data()
    data["species"] = ["invalid_species"]
    pd.DataFrame(data).to_csv(input_file, index=False)

    with pytest.raises(DataValidationError):
        validate(str(input_file))


def test_validate_rejects_out_of_range_values(tmp_path):
    input_file = tmp_path / "range.csv"
    data = valid_data()
    data["sepal length (cm)"] = [99.0]
    pd.DataFrame(data).to_csv(input_file, index=False)

    with pytest.raises(DataValidationError):
        validate(str(input_file))


def test_validate_rejects_missing_columns(tmp_path):
    input_file = tmp_path / "missing.csv"
    pd.DataFrame({"species": ["setosa"]}).to_csv(
        input_file, index=False
    )

    with pytest.raises(DataValidationError):
        validate(str(input_file))
