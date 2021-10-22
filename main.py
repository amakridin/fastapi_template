import uvicorn
from fastapi import FastAPI

from routes import router


class Settings:
    host: str = "0.0.0.0"
    port: int = 8008
    service_name: str = "fastapi_app"
    timeout: int = 2


if __name__ == "__main__":
    settings = Settings()
    app = FastAPI(title=settings.service_name)
    app.include_router(router)
    uvicorn.run(app=app,
                port=settings.port,
                access_log=True,
                host=settings.host)
