from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSecret(BaseSettings):
    DB: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    
    model_config = SettingsConfigDict(env_prefix='POSTGRES_', env_file='.env')