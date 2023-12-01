from dotenv import load_dotenv
import os

load_dotenv('.env')

class Config:
    
    PROPOGATE_EXCEPTIONS = True
    
    # OpenAPI (Swagger)
    API_TITLE = "NewFeed REST API"
    API_VERSION = "v1"    
    OPENAPI_VERSION = "3.0.2"
    OPENAPI_URL_PREFIX = "/"            
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    # DB
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_HOST = os.environ.get("DATABASE_HOST")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DB_PORT = os.environ.get("DB_PORT")
    DATABASE_URI = os.environ.get("DATABASE_URI")


