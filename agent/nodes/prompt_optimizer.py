import os
import time
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def get_deepseek_client():
    """DeepSeek API 客户端"""
    return ChatOpenAI(
        model="deepseek-chat",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com/v1",
        temperature=0.7,
    )


def load_prompt_template() -> str:
    """ 从 prompts/ 加载模板 """
    prompts_dir = Path(__file__).parent.parent.parent / "prompts"
    file_path = prompts_dir / "prompt_optimizer.md"
    if not file_path.exists():
        raise FileNotFoundError(f"Prompt template not found: {file_path}")
    return file_path.read_text(encoding="utf-8")


def prompt_optimizer_node(state, max_retries: int = 2):
    """
    使用 DeepSeek 将简单输入转化为高质量英文提示词。

    特点：
    - 使用外部模板
    - 包含简单重试
    - 输出更干净
    """
    user_input = state["user_input"]
    template_str = load_prompt_template()
    prompt_template = ChatPromptTemplate.from_template(template_str)

    llm = get_deepseek_client()
    chain = prompt_template | llm

    last_error = None

    for attempt in range(max_retries + 1):
        try:
            response = chain.invoke({"user_input": user_input})
            optimized_prompt = response.content.strip()

            return {
                "optimized_prompt": optimized_prompt,
                "current_step": "prompt_optimized",
                "history": state.get("history", []) + [{
                    "step": "prompt_optimizer",
                    "attempt": attempt + 1,
                    "optimized_prompt": optimized_prompt
                }]
            }
        except Exception as e:
            last_error = str(e)
            if attempt < max_retries:
                time.sleep(1)
            else:
                break

    return {
        "optimized_prompt": None,
        "current_step": "error",
        "error": f"DeepSeek 调用失败: {last_error}",
        "history": state.get("history", [])
    }