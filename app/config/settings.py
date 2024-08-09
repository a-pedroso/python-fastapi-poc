from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

#from dotenv import find_dotenv, load_dotenv

#load_dotenv(find_dotenv(".env"))

# class Settings(BaseSettings):
#     database_url: str

#     model_config = SettingsConfigDict(case_sensitive=True)

#     # class Config:
#     #     env_file = ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    DATABASE_URL: str = ''
    
    