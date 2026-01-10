import pandas as pd
import joblib
from app.core.config import settings
from app.cache.redis_cache import get_cached_output, set_cached_output

model = joblib.load(settings.MODEL_PATH)

def predict_car_price(data: dict):
    cache_key = " ".join([str(val) for val in data.values()])
    cached = get_cached_output(cache_key)
    if cached:
        return cached
    

    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    set_cached_output(cache_key, prediction)
    return prediction