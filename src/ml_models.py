import joblib

#from sklearn.model_selection import train_test_split

from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    accuracy_score,
    classification_report
)

from xgboost import XGBRegressor, XGBClassifier


# =========================================================
# REGRESION
# =========================================================

def train_random_forest_regressor(X, y):

    model = RandomForestRegressor(
        n_estimators = 100,
        random_state = 42
    )

    model.fit(X, y)
    return model


def train_xgboost_regressor(X, y):

    model = XGBRegressor(
        n_estimators = 100,
        random_state = 42
    )

    model.fit(X, y)
    return model


def regression_metrics(model, X_test, y_test):

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    rmse = mean_squared_error(y_test, predictions) ** 0.5

    r2 = r2_score(y_test, predictions)

    return {
        "MAE : " : mae,
        "RMSE : " : rmse,
        "R2 : " : r2
    }

# =========================================================
# CLASIFICACION
# =========================================================

def train_random_forest_classifier(X, y):

    model = RandomForestClassifier(
        n_estimators = 100,
        random_state = 42
    )

    model.fit(X, y)

    return model


def train_xgboost_classifier(X, y):

    model = XGBClassifier(
        n_estimators = 100,
        random_state = 42
    )

    model.fit(X, y)

    return model


def classification_metrics(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    report = classification_report(y_test, predictions)

    return {
        "Accuracy : " : accuracy,
        "Report : " : report
    }


# =========================================================
# EXPORTAR MODELOS
# =========================================================

def save_model(model, path):

    joblib.dump(model, path)
