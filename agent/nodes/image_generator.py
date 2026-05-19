import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def get_siliconflow_client():
    """ 础于硅基流动的 OpenAI 兼容客户端 """
    return ChatOpenAI(
        model="Qwen/Qwen-Image",
        api_key=os.getenv("SILICONFLOW_API_KEY"),
        base_url="https://api.siliconflow.cn/v1",
        temperature=0.8,
    )


def image_generator_node(state):
    """
    使用 Qwen-Image 进行文生图
    """
    prompt = state.get("optimized_prompt")

    if not prompt:
        return {
            "image_url": None,
            "current_step": "error",
            "error": "没有提示词，无法生成图像"
        }

    llm = get_siliconflow_client()

    # 使用简单提示词调用生图（硅基流动 Qwen-Image 支持）
    response = llm.invoke(prompt)

    # 注：Qwen-Image 在硅基流动上通常返回图片 URL
    image_url = response.content.strip() if hasattr(response, 'content') else None

    return {
        "image_url": image_url,
        "current_step": "image_generated",
        "history": state.get("history", []) + [{
            "step": "image_generator",
            "prompt_used": prompt,
            "image_url": image_url
        }]
    }