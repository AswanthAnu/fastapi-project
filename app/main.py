from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers
from app.api import routes_auth, routes_predict

app = FastAPI(title='Car Prediction App')

# link middleware
app.add_middleware(LoggingMiddleware)


# link endpoints
app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_predict.router, tags=['Predict'])

# monitoring using prometheus
Instrumentator().instrument(app).expose(app)

#link exception handler
register_exception_handlers(app)