"""Demonstrate a reusable supervised machine learning workflow.

This module demonstrates the fundamental steps
used in supervised machine learning,
from defining the prediction problem
through evaluating results and
planning the next experiment.

Module Information:
    - Filename: ml_example.py
    - Module: ml_example
    - Location: src/pro_analytics_02/

Supervised Setup:
    1. Define the prediction problem and target.
    2. Identify the available features.
    3. Select the features to use.
    4. Prepare and preprocess the data.
    5. Design the train/test experiment.

Supervised Execution:
    1. Establish a baseline model.
    2. Train the primary model.
    3. Generate predictions on the test data.
    4. Evaluate the model using appropriate metrics.
    5. Compare the model with the baseline.
    6. Diagnose errors and model behavior.
    7. Interpret the results and draw conclusions.
    8. Identify limitations and propose the next experiment.

Key Concepts:
    - Target and feature selection
    - Train/test experimental design
    - Baseline and primary models
    - Model training and prediction
    - Model evaluation and comparison
    - Error diagnosis and interpretation
    - Iterative experimentation

Professional Applications:
    - Designing reproducible machine learning experiments
    - Comparing models against meaningful baselines
    - Evaluating model performance with appropriate metrics
    - Communicating model results and limitations
    - Planning evidence-based follow-up experiments

Open a terminal in the root project folder and run
as a module with the command:

uv run pro_analytics_02.ml_example
"""
# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path

from datafun_toolkit.logger import get_logger, log_header, log_path
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from pro_analytics_02.utils.ml_utils import (
    build_given_baseline_classification_model,
    evaluate_classification_model,
)

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("ML", level="DEBUG")

# === DEFINE GLOBAL PATHS ===

ROOT_PATH: Path = Path.cwd()
NOTEBOOKS_PATH: Path = ROOT_PATH / "notebooks"

# === DEFINE FUNCTIONS ===


def build_primary_model():
    """Build the analyst-selected primary classification model.

    This function tries to improve on the simple given baseline model.
    """
    # TODO: ANALYST DECISION: Choose an appropriate classification model
    # from the scikit-learn library.
    # You can find them at https://scikit-learn.org/stable/supervised_learning.html
    model_type = "DecisionTreeClassifier"
    max_depth = 3
    random_state = 42

    # TODO: ANALYST RATIONALE:
    # DELETE ALL EXISTING CONTENT with instructions and example.
    # ADD your own explanation.
    #
    # Explain why this model is appropriate for this prediction problem.
    reason = r"""
        INSTRUCTIONS: the analyst must write this, referencing the numeric results.
        EXAMPLE: The target is categorical.
        A decision tree learns rules from the selected features
        to predict one of the target categories.
        I choose a max depth of 3 and started with
        random state=42 for reproducibility.
    """

    LOG.info("")
    LOG.info("***************************************")
    LOG.info("Analyst-Defined Primary Model:")
    LOG.info(f"  Model type: {model_type}")
    LOG.info(f"  max_depth: {max_depth}")
    LOG.info(f"  random_state: {random_state}")
    LOG.info(f"  Rationale: {reason}")
    LOG.info("***************************************")
    LOG.info("")

    # TODO: ANALYST IMPLEMENTATION:
    # Implement the analyst-selected primary model using the chosen model type and parameters.
    model: DecisionTreeClassifier = DecisionTreeClassifier(
        max_depth=max_depth, random_state=random_state
    )

    return model


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main():
    """Run the supervised machine learning example.

    Arguments: None (nothing is passed in the parentheses after `main`).

    Returns: None (nothing is returned when this function runs).

    This function creates what we call `side effects` -
    it logs information to the console and a file.

    The example follows a standard supervised machine learning progression:

    Part 1 defines and prepares the experiment.
    Part 2 executes, evaluates, and interprets the experiment.
    """
    log_header(LOG, "Supervised Machine Learning Example")
    LOG.info("START main()")
    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "NOTEBOOKS_PATH", NOTEBOOKS_PATH)

    # ============================================================
    # === PART 1: SUPERVISED SETUP ===
    # ============================================================

    LOG.info("")
    LOG.info("=== PART 1: SUPERVISED SETUP ===")
    LOG.info("")

    # 1.1. Define the prediction problem and target.

    dataset = load_breast_cancer(as_frame=True)
    df = dataset.frame

    # TODO: ANALYST DECISION: Define the prediction problem.
    prediction_problem = "Predict whether a tumor is malignant or benign."

    # The dataset stores the classification target in a column named "target".
    target = "target"

    # Describe what the target actually represents.
    target_description = "Tumor diagnosis: malignant or benign"

    # Get the categorical target values supplied with the dataset.
    target_categories = [str(value) for value in dataset.target_names]

    LOG.info("")
    LOG.info("***************************************")
    LOG.info("Analyst-Defined Experiment:")
    LOG.info(f"  Prediction problem: {prediction_problem}")
    LOG.info(f"  Target variable: {target}")
    LOG.info(f"  Target meaning: {target_description}")
    LOG.info(f"  Target categories: {target_categories}")
    LOG.info("***************************************")
    LOG.info("")

    # 1.2. Identify the available features.

    available_features = list(dataset.feature_names)

    LOG.info("")
    LOG.info(f"Available features ({len(available_features)}):")
    for feature in available_features:
        LOG.info(f"  - {feature}")

    # 1.3. Select the features to use.

    # TODO: ANALYST DECISION: Select the features to use.
    selected_features = [
        "mean radius",
        "mean texture",
        "mean perimeter",
        "mean area",
    ]

    LOG.info("")
    LOG.info("***************************************")
    LOG.info(f"Analyst-selected features ({len(selected_features)}):")
    for feature in selected_features:
        LOG.info(f"  - {feature}")
    LOG.info("***************************************")
    LOG.info("")

    # Define X (features) and y (target).

    X = df[selected_features]
    y = df[target]

    # 1.4. Prepare and preprocess the data.

    # Scaling will be handled later inside the primary model pipeline.

    # 1.5. Design the train/test experiment.

    # TODO: ANALYST DECISION: Define the test size.
    test_size = 0.20

    # TODO: ANALYST DECISION: Provide a reason for the test size.
    test_size_reason: str = "common choice for train/test splits."

    # TODO: ANALYST DECISION: Define the random state for reproducibility.
    random_state = 42

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    LOG.info("")
    LOG.info("Train/Test Design (data):")
    LOG.info(f"  Observations:   {len(df)}")
    LOG.info(f"  Training:       {len(X_train)}")
    LOG.info(f"  Test:           {len(X_test)}")
    LOG.info("")
    LOG.info("***************************************")
    LOG.info("Train/Test Design (analyst):")
    LOG.info(f"   Test size:    {test_size:.0%}")
    LOG.info(f"   Reason:    {test_size_reason}")
    LOG.info(f"   Random state: {random_state}")
    LOG.info("***************************************")
    LOG.info("")

    # ============================================================
    # === PART 2: SUPERVISED EXECUTION ===
    # ============================================================

    LOG.info("")
    LOG.info("=== PART 2: SUPERVISED EXECUTION ===")
    LOG.info("")

    # 2.1. Establish a baseline model.

    baseline_model = build_given_baseline_classification_model(LOG)
    baseline_model.fit(X_train, y_train)

    # 2.2. Train the primary model.

    primary_model = build_primary_model()
    primary_model.fit(X_train, y_train)

    # 2.3. Generate predictions on the test data.

    _, baseline_accuracy = evaluate_classification_model(
        baseline_model,
        X_test,
        y_test,
    )

    primary_predictions, primary_accuracy = evaluate_classification_model(
        primary_model,
        X_test,
        y_test,
    )

    # 2.4. Evaluate the model using appropriate metrics.

    LOG.info("Model Performance:")
    LOG.info(f"  Baseline accuracy:      {baseline_accuracy:.1%}")
    LOG.info(f"  Primary model accuracy: {primary_accuracy:.1%}")
    improvement = primary_accuracy - baseline_accuracy
    LOG.info(f"  Improvement:            {improvement:+.1%}")

    # 2.5. Compare the model with the baseline.

    improvement = primary_accuracy - baseline_accuracy

    LOG.info(f"Improvement over baseline: {improvement:.3f}")

    # 2.6. Diagnose errors and model behavior.

    matrix = confusion_matrix(y_test, primary_predictions)

    confusion_df = pd.DataFrame(
        matrix,
        index=["Actual 0", "Actual 1"],
        columns=["Predicted 0", "Predicted 1"],
    )

    LOG.info("")
    LOG.info("Confusion Matrix:")
    LOG.info(f"\n{confusion_df}")

    # 2.7. Interpret the results and draw conclusions.

    if primary_accuracy > baseline_accuracy:
        LOG.info("The primary model outperformed the baseline.")
    else:
        LOG.info("The primary model did not outperform the baseline.")

    # TODO: ANALYST OBSERVATIONS:
    # DELETE ALL EXISTING CONTENT with instructions and example.
    # ADD your own observations based on the numeric results.
    #
    # State what you observe in the numerical results.
    # Quote specific numerical evidence such as the baseline score, model score,
    # improvement, and confusion matrix counts.
    #
    # An observation describes WHAT the results show.
    # Do NOT explain why yet.

    analyst_observations: str = r"""
        INSTRUCTIONS: the analyst must write this, referencing the numeric results.
        EXAMPLE: The primary model achieved 89.5% accuracy compared with
        63.2% for the baseline, an improvement of 26.3 percentage points.
        The confusion matrix shows 12 incorrect predictions.
    """

    # TODO: ANALYST INTERPRETATION:
    # DELETE ALL EXISTING CONTENT with instructions and example.
    # ADD your own interpretation based on the observations.
    #
    # Explain what your observations mean for this prediction problem.
    # Connect the evidence to the target, selected features, model,
    # and practical usefulness of the result.
    # An interpretation answers: SO WHAT?
    # Do not be general - be specific. What did you learn from your work?
    # This should be valuable, useful, and actionable information for a decision maker.
    # It should be clearly grounded in the evidence you observed in the results.
    analyst_interpretation: str = r"""
        INSTRUCTIONS: The analyst must write this, based on the observations.
        EXAMPLE: The selected measurements contain useful predictive information,
        because the model performs much better than the baseline.
        However, the remaining errors suggest that these four selected features alone
        do not fully distinguish malignant from benign tumors.
    """

    # 2.8. Identify limitations and propose the next experiment.

    # TODO: ANALYST PROPOSED NEXT EXPERIMENT:
    # DELETE ALL EXISTING CONTENT with instructions and example.
    # ADD your own interpretation based on the observations.
    #
    # Propose a next experiment that addresses the limitations of this experiment.
    # This should be a specific, actionable experiment that can be implemented.
    # It should be clearly grounded in the evidence you observed in the results.
    next_experiment = r"""
        INSTRUCTIONS: The analyst must write this, based on the work.
        EXAMPLE: Test whether adding selected shape and texture measurements improves
        test performance without substantially increasing model complexity.
    """

    LOG.info("")
    LOG.info("***************************************")
    LOG.info("Analyst Observations:")
    LOG.info(f"{analyst_observations}")
    LOG.info("")
    LOG.info("***************************************")
    LOG.info("Analyst Interpretation:")
    LOG.info(f"{analyst_interpretation}")

    LOG.info("")
    LOG.info("***************************************")
    LOG.info("Analyst Proposed Next Experiment:")
    LOG.info(f"  {next_experiment}")
    LOG.info("***************************************")
    LOG.info("")
    LOG.info("\nEND main()")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is standard Python boilerplate.

if __name__ == "__main__":
    main()
