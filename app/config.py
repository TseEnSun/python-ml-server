from pydantic import BaseSettings, PostgresDsn, validator, EmailStr
from typing import Any, Dict, Optional
import secrets


class Settings(BaseSettings):
    PROJECT_NAME: str = "Sticker Search"
    API_PATH: str = "/sticker-search"
    API_V1_STR: str = f"{API_PATH}/v1"
    
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )
    
    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # one week

    class Config:
        case_sensitive = True


settings = Settings()
