import os
from pathlib import Path


class Settings:
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com/v1"
    DEEPSEEK_MODEL: str = "deepseek-chat"

    # 后续模型配置
    QWEN_API_KEY: str = os.getenv("QWEN_API_KEY", "")

    PROMPTS_DIR: Path = Path(__file__).parent.parent / "prompts"


settings = Settings()