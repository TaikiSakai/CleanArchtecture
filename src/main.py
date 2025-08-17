from fastapi import FastAPI
from src.presentation.handler.user_handler import router


app = FastAPI()
# app.include_router(router)
app.include_router(router, prefix="/api", tags=["v1"])


@app.get("/health_check")
def ping():
    return {'status': 'ok'}
