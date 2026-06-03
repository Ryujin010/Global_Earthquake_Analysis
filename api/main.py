from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(
    title="Global Earthquake Prediction API",
    version="1.0"
)

# ============================================
# CARGAR MODELO
# ============================================

model = joblib.load(
    "models/random_forest_model.pkl"
)

# ============================================
# HOME
# ============================================

@app.get("/")
def home():

    return {
        "message": "Earthquake Prediction API Running"
    }

# ============================================
# PREDICCION
# ============================================

@app.get("/predict")

def predict(
    depth: float,
    latitude: float,
    longitude: float,
    year: int
):

    data = pd.DataFrame({
        "depth": [depth],
        "latitude": [latitude],
        "longitude": [longitude],
        "year": [year]
    })

    prediction = model.predict(data)

    return {
        "predicted_magnitude":
        round(float(prediction[0]), 2)
    }