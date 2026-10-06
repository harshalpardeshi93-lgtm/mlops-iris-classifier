# Hyperparameter Tuning Analysis

## 1. Baseline Model

### Model
DecisionTreeClassifier with default hyperparameters.

### Cross-Validation
5-fold cross-validation using F1 Macro scoring.

### Results

- CV F1 Macro: 0.9663
- CV F1 Macro Std: 0.0316
- Test Accuracy: 0.9000
- Total Fits: 5

The baseline model provides a reference point for evaluating the effect of hyperparameter tuning.

---

## 2. Grid Search

### Model
RandomForestClassifier

### Search Method
GridSearchCV

### Search Space

- `n_estimators`: 50, 100, 200
- `max_depth`: 3, 5, 10, None
- `min_samples_split`: 2, 5, 10
- `max_features`: sqrt, log2

### Search Size

72 combinations were evaluated using 5-fold cross-validation.

Total fits:

72 × 5 = 360

### Best Parameters

```text
max_depth = 3
max_features = sqrt
min_samples_split = 2
n_estimators = 50
