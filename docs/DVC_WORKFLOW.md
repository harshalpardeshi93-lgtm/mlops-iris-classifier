# DVC Workflow

## Dataset Versioning

This project uses DVC with Git to track and version the Iris dataset.

### Version 1

- Dataset: `data/raw/iris_v1.csv`
- Rows: 150
- Git commit: `de81ce9`
- DVC MD5: `4d301abed5efe50eccda350cde38e0eb`

### Version 2

- Dataset: `data/raw/iris_v1.csv`
- Rows: 170
- Git commit: `e05c79c`
- DVC MD5: `d9036d4341f8ac67d705d6b00a95377a`

## DVC Commands Used

```bash
dvc init
dvc remote add -d myremote ~/dvc-remote-storage
dvc add data/raw/iris_v1.csv
dvc push
dvc status
dvc diff de81ce9
dvc checkout data/raw/iris_v1.csv.dvc
