"""app.py - demo marimo notebook app.

The official name starts with a lowercase "m" (marimo),
and the module name is lowercase (marimo).

See: https://github.com/marimo-team/marimo-uv-starter-template
And: https://marimo.io/gallery

Run with:

uv run python notebooks/app.py
uv run ruff format --check notebooks/app.py
uv run ruff check notebooks/app.py

To view as notebook,
click the "Open in marimo" button (m inside circle)
in the top right corner of this page.

To view again as a file, right-click and select
"Reopen editor" / "Text Editor".
"""

# === Imports ===

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import pandas as pd
    from sklearn.datasets import load_breast_cancer
    from sklearn.dummy import DummyClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, confusion_matrix
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler


@app.cell
def _():
    mo.md("""
    # Supervised Machine Learning Example

    This example demonstrates a repeatable supervised machine learning workflow.

    The work is divided into two parts:

    1. **Supervised Setup** - define the prediction problem and design the experiment.
    2. **Supervised Execution** - train, evaluate, compare, and interpret models.
    """)
    return


@app.cell
def _():
    mo.md("""
    ## Part 1. Supervised Setup

    1. Define the prediction problem and target.
    2. Identify the available features.
    3. Select the features to use.
    4. Prepare and preprocess the data.
    5. Design the train/test experiment.
    """)
    return


@app.cell
def _():
    # Load a built-in classification dataset.
    dataset = load_breast_cancer(as_frame=True)
    df = dataset.frame

    # 1. Define the prediction problem and target.
    target = "target"

    # 2. Identify the available features.
    available_features = list(dataset.feature_names)

    # 3. Select the features to use.
    selected_features = [
        "mean radius",
        "mean texture",
        "mean perimeter",
        "mean area",
    ]

    # Define X (features) and y (target).
    X = df[selected_features]
    y = df[target]

    # 4. Prepare and preprocess the data.
    # Scaling will be handled later inside the model pipeline.

    # 5. Design the train/test experiment.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )
    return (
        X_test,
        X_train,
        available_features,
        df,
        selected_features,
        target,
        y_test,
        y_train,
    )


@app.cell
def _(X_test, X_train, available_features, df, selected_features, target):
    mo.md(
        f"""
    ### Experiment Design

    **Prediction problem:** Predict whether a tumor is malignant or benign.

    **Target:** `{target}`

    **Available features:** {len(available_features)}

    **Selected features:** {", ".join(selected_features)}

    **Total observations:** {len(df)}

    **Training observations:** {len(X_train)}

    **Test observations:** {len(X_test)}

    The target is separated from the predictor features before model training.
    The test set is held out for evaluation.
    """
    )
    return


@app.cell
def _():
    mo.md("""
    ## Part 2. Supervised Execution

    1. Establish a baseline model.
    2. Train the primary model.
    3. Generate predictions on the test data.
    4. Evaluate the model using appropriate metrics.
    5. Compare the model with the baseline.
    6. Diagnose errors and model behavior.
    7. Interpret the results and draw conclusions.
    8. Identify limitations and propose the next experiment.
    """)
    return


@app.cell
def _(X_test, X_train, y_test, y_train):
    # 1. Establish a baseline model.
    baseline_model = DummyClassifier(strategy="most_frequent")
    baseline_model.fit(X_train, y_train)

    # 2. Train the primary model.
    primary_model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=2000),
    )
    primary_model.fit(X_train, y_train)

    # 3. Generate predictions on the test data.
    baseline_predictions = baseline_model.predict(X_test)
    primary_predictions = primary_model.predict(X_test)

    # 4. Evaluate the models.
    baseline_accuracy = accuracy_score(y_test, baseline_predictions)
    primary_accuracy = accuracy_score(y_test, primary_predictions)

    # 5. Compare with the baseline.
    improvement = primary_accuracy - baseline_accuracy

    # 6. Diagnose errors.
    matrix = confusion_matrix(y_test, primary_predictions)

    confusion_df = pd.DataFrame(
        matrix,
        index=["Actual 0", "Actual 1"],
        columns=["Predicted 0", "Predicted 1"],
    )
    return baseline_accuracy, confusion_df, improvement, primary_accuracy


@app.cell
def _(baseline_accuracy, improvement, primary_accuracy):
    mo.md(
        f"""
    ### Model Results

    **Baseline accuracy:** {baseline_accuracy:.3f}

    **Primary model accuracy:** {primary_accuracy:.3f}

    **Improvement over baseline:** {improvement:.3f}

    ### Interpretation

    The primary model should be evaluated relative to the baseline,
    not only by its standalone accuracy.

    Next, inspect the errors and consider whether the selected features,
    model choice, preprocessing, or experiment design should change.
    """
    )
    return


@app.cell
def _(confusion_df):
    mo.vstack(
        [
            mo.md("### Confusion Matrix"),
            confusion_df,
        ]
    )
    return


@app.cell
def _():
    mo.md("""
    ## Limitations and Next Experiment

    Consider:

    - Are these the best features?
    - Is accuracy the best evaluation metric?
    - Are the classes balanced?
    - Would another model perform better?
    - Would changing the train/test design affect the conclusions?
    - What should be tested next?

    A machine learning result is not the end of the analysis.
    It should lead to the next well-defined experiment.
    """)
    return


if __name__ == "__main__":
    app.run()
