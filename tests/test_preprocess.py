import pandas as pd
from src.pipeline.preprocess import preprocess


def test_preprocess_removes_duplicates_and_timestamp(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    data = {
        "sepal length (cm)": [5.1, 5.1, 6.2],
        "sepal width (cm)": [3.5, 3.5, 3.4],
        "petal length (cm)": [1.4, 1.4, 5.4],
        "petal width (cm)": [0.2, 0.2, 2.3],
        "species": ["setosa", "setosa", "virginica"],
        "collected_at": ["2026-01-01", "2026-01-01", "2026-01-02"],
    }

    pd.DataFrame(data).to_csv(input_file, index=False)

    result = preprocess(str(input_file), str(output_file))

    assert len(result) == 2
    assert "collected_at" not in result.columns
    assert output_file.exists()


def test_preprocess_imputes_missing_numeric_values(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    data = {
        "sepal length (cm)": [5.0, None, 7.0],
        "sepal width (cm)": [3.0, 3.2, 3.4],
        "petal length (cm)": [1.0, 1.5, 5.0],
        "petal width (cm)": [0.2, 0.3, 1.8],
        "species": ["setosa", "setosa", "virginica"],
    }

    pd.DataFrame(data).to_csv(input_file, index=False)

    result = preprocess(str(input_file), str(output_file))

    assert result["sepal length (cm)"].isna().sum() == 0
    assert result["sepal length (cm)"].iloc[1] == 6.0
