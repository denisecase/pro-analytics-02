"""ml_utils.py - reusable functions for machine learning.

Uses r-strings (raw strings) for multi-line docstrings
for convenience.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging

from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.metrics import accuracy_score

# === DEFINE REUSABLE MACHINE LEARNING FUNCTIONS ===


def get_model_type(is_supervised: bool, is_target_categorical: bool) -> str:
    """Determine the model type based on the problem type and target type.

    Arguments:
        is_supervised (bool): True if the problem is supervised.
        is_target_categorical (bool): True if the target is categorical.

    Returns:
        str: The model type as a string.
    """
    if is_supervised:
        if is_target_categorical:
            return "Classification"
        return "Regression"
    return "Unsupervised"


def build_given_baseline_classification_model(log: logging.Logger):
    """Build and log a given baseline classification model for a categorical target."""

    # A baseline model is provided.
    is_supervised: bool = True
    is_target_categorical: bool = True

    model_name: str = "DummyClassifier"
    strategy: str = "most_frequent"

    reason: str = r"""
        When the target is categorical,
        a most-frequent DummyClassifier
        provides a simple reference model
        that ignores the selected features.
        """

    log.info("")
    log.info("Given Baseline Model:")
    log.info(f"  Problem type: {get_model_type(is_supervised, is_target_categorical)}")
    log.info(f"  Model: {model_name}")
    log.info(f"  Strategy: {strategy}")
    log.info(f"  Rationale: {reason}")
    log.info("")

    return DummyClassifier(strategy=strategy)


def build_given_baseline_regression_model(log: logging.Logger):
    """Build and log a given baseline regression model for a numerical target."""

    is_supervised: bool = True
    is_target_categorical: bool = False

    model_name: str = "DummyRegressor"
    strategy: str = "mean"

    reason: str = r"""
        When the target is numerical,
        a mean DummyRegressor
        provides a simple reference model
        that always predicts the mean training target value
        and ignores the selected features.
        """

    log.info("")
    log.info("Given Baseline Model:")
    log.info(f"  Problem type: {get_model_type(is_supervised, is_target_categorical)}")
    log.info(f"  Model: {model_name}")
    log.info(f"  Strategy: {strategy}")
    log.info(f"  Rationale: {reason}")
    log.info("")

    return DummyRegressor(strategy=strategy)


def evaluate_classification_model(model, X_test, y_test):
    """Generate predictions and calculate classification accuracy.

    Works with any classification model that follows the usual
    scikit-learn estimator interface and provides .predict().

    Including:
    DummyClassifier(...)
    DecisionTreeClassifier(...)
    RandomForestClassifier(...)
    LogisticRegression(...)
    KNeighborsClassifier(...)
    """
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return predictions, accuracy
