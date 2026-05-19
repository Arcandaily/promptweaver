import os
import requests
from typing import Optional


def generate_image_with_siliconflow(prompt: str) -> Optional[str]:
    """
    使用硅基流动 API 调用 Qwen/Qwen-Image 生成图片
    """
    api_key = os.getenv("SILICONFLOW_API_KEY")
    if not api_key:
        raise ValueError("SILICONFLOW_API_KEY 未设置")

    url = "https://api.siliconflow.cn/v1/images/generations"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "Qwen/Qwen-Image",
        "prompt": prompt,
        "size": "1024x1024"
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=90)
        response.raise_for_status()
        data = response.json()

        if "data" in data and len(data["data"]) > 0:
            return data["data"][0].get("url")
        return None
    except Exception as e:
        print(f"[SiliconFlow Image Error] {e}")
        return None


def image_generator_node(state):
    """
    LangGraph 节点：调用 Qwen-Image 生成图片
    """
    prompt = state.get("optimized_prompt")

    if not prompt:
        return {
            "image_url": None,
            "current_step": "error",
            "error": "没有可用的提示词"
        }

    print("\n正在调用 Qwen-Image 生成图片...")
    image_url = generate_image_with_siliconflow(prompt)

    if image_url:
        print(f"图片生成成功！")
    else:
        print("图片生成失败")

    return {
        "image_url": image_url,
        "current_step": "image_generated" if image_url else "error",
        "error": None if image_url else "图片甐成失败",
        "history": state.get("history", []) + [{
            "step": "image_generator",
            "prompt_used": prompt,
            "image_url": image_url
        }]
    }