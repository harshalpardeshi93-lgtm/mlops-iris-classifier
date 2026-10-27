import pandas as pd
from src.pipeline.features import engineer_features


def test_engineer_features_creates_expected_columns(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    data = {
        "sepal length (cm)": [5.1, 6.2],
        "sepal width (cm)": [3.5, 3.4],
        "petal length (cm)": [1.4, 5.4],
        "petal width (cm)": [0.2, 2.3],
        "species": ["setosa", "virginica"],
    }

    pd.DataFrame(data).to_csv(input_file, index=False)

    result = engineer_features(str(input_file), str(output_file))

    assert "sepal_area" in result.columns
    assert "petal_area" in result.columns
    assert "sepal_to_petal_length_ratio" in result.columns
    assert "petal_length_bin" in result.columns
    assert output_file.exists()


def test_engineer_features_calculates_area_correctly(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    data = {
        "sepal length (cm)": [5.0],
        "sepal width (cm)": [3.0],
        "petal length (cm)": [2.0],
        "petal width (cm)": [0.5],
        "species": ["setosa"],
    }

    pd.DataFrame(data).to_csv(input_file, index=False)

    result = engineer_features(str(input_file), str(output_file))

    assert result["sepal_area"].iloc[0] == 15.0
    assert result["petal_area"].iloc[0] == 1.0
    assert result["sepal_to_petal_length_ratio"].iloc[0] == 2.5
