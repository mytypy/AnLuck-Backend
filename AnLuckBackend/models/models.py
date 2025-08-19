from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSecret(BaseSettings):
    DB: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    
    model_config = SettingsConfigDict(
        env_prefix='POSTGRES_',
        env_file='.env',
        extra='allow'
    )

class JwtSecret(BaseSettings):
    SECRET: str
    ACCESS_MAX_AGE_HOURS: int
    REFRESH_MAX_AGE_DAYS: int
    
    model_config = SettingsConfigDict(
        env_prefix='JWT_',
        env_file='.env',
        extra='allow'
    )