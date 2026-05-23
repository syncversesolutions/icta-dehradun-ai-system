# ============================================
# IMPORTS
# ============================================

from sklearn.linear_model import LinearRegression

from sklearn.metrics import (

    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ============================================
# TRAIN MODEL
# ============================================

def train_congestion_model(X, y):

    model = LinearRegression()

    model.fit(X, y)

    return model

# ============================================
# GENERATE PREDICTIONS
# ============================================

def generate_predictions(model, X):

    predictions = model.predict(X)

    return predictions

# ============================================
# EVALUATE MODEL
# ============================================

def evaluate_model(y_true, y_pred):

    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    mse = mean_squared_error(
        y_true,
        y_pred
    )

    r2 = r2_score(
        y_true,
        y_pred
    )

    metrics = {

        "MAE": round(mae, 4),

        "MSE": round(mse, 4),

        "R2_SCORE": round(r2, 4)
    }

    return metrics

# ============================================
# CLASSIFY RISK
# ============================================

def classify_risk(score):

    if score < 1.5:

        return "Low"

    elif score < 2.5:

        return "Medium"

    elif score < 3.5:

        return "High"

    else:

        return "Severe"