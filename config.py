from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    """Класс для подключения токенов."""
    login_email: SecretStr
    password: SecretStr
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / '.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )


config = Settings()
