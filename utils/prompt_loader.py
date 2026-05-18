from pathlib import Path


def load_prompt(filename: str, prompts_dir: Path = None) -> str:
    """
    加载 prompts/ 目录下的模板文件

    Args:
        filename: 模板文件名（例：prompt_optimizer.md）
        prompts_dir: 自定义 prompts 目录路径
    """
    if prompts_dir is None:
        prompts_dir = Path(__file__).parent.parent / "prompts"

    file_path = prompts_dir / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Prompt template not found: {file_path}")

    return file_path.read_text(encoding="utf-8").strip()