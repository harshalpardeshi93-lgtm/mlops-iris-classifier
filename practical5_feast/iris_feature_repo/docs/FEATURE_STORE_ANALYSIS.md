# Feature Store Analysis

## 1. Elimination of Training-Serving Skew

Feast provides a centralized feature store for both offline and online feature retrieval.

The same feature definitions are used for training and serving. The engineered features such as `sepal_area`, `petal_area`, `sepal_to_petal_length_ratio`, and `petal_length_bin` are defined once in the Feast Feature Views.

This helps maintain consistency between the features used during model training and those retrieved during online inference.

## 2. Feature Reusability

The `iris_feature_service` provides a reusable collection of features from the two Feature Views:

- `iris_measurements`
- `iris_engineered_features`

The features can be retrieved using the Feature Service without reimplementing the feature engineering logic.

This demonstrates that the same features can be reused for different machine learning workflows.

## 3. Centralized Governance

The feature definitions are maintained centrally in `features.py`.

This provides a single source of truth for feature definitions, including:

- Entity definitions
- Feature Views
- Feature data types
- Online availability
- Feature Service configuration

Centralized feature management makes the feature store easier to maintain and govern.
