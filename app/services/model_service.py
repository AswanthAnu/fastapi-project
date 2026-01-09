import pandas as pd
from core.config import settings
from redis_cache import get_cached_output, set_cached_output

model = settings.MODEL_PATH

def predict_car_price(data: dict):
    cache_key = " ".join([val for val in data.values()])
    cached = get_cached_output(cache_key)
    if cached:
        return cached
    

    input = pd.DataFrame([data])
    prediction = model.predict(input)[0]
    set_cached_output(cache_key, prediction)
    return prediction