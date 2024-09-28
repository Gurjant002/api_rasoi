from pathlib import Path
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, UJSONResponse
from fastapi.exceptions import RequestValidationError

APP_ROOT = Path(__file__).resolve().parent

def get_app() -> FastAPI:
    app = FastAPI(
        title="API Rasoi",
        version="v1",
        description="API created to manage orders in a restaurant.",
        # docs_url="/swagger",
        default_response_class=UJSONResponse,
    )

    app.middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    