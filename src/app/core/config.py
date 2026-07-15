from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application
    app_name: str = "AI Knowledge Assistant"
    app_version: str = "0.1.0"

    environment: str = "development"
    debug: bool = False

    api_prefix: str = "/api/v1"

    # Database
    database_url: str | None = None

    # LLM
    default_llm: str = "gemini"

    openai_api_key: str | None = None
    gemini_api_key: str | None = None

    # Logging
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
