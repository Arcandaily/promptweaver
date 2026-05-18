from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

import os


def get_deepseek_client():
    """ 初始化 DeepSeek 客户端（OpenAI 兼容）"""
    return ChatOpenAI(
        model="deepseek-chat",
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com/v1",
        temperature=0.7,
    )


def prompt_optimizer_node(state):
    """
    使用 DeepSeek 进行提示词优化的节点

    这是核心节点，负责将用户简单输入转化为高质量提示词。
    """
    user_input = state["user_input"]

    prompt_template = ChatPromptTemplate.from_template(
        "You are an expert prompt engineer for AI image generation.\n"
        "Transform the user's simple idea into a detailed, high-quality prompt.\n\n"
        "User idea: {user_input}\n\n"
        "Optimized prompt:"
    )

    llm = get_deepseek_client()
    chain = prompt_template | llm

    response = chain.invoke({"user_input": user_input})

    optimized_prompt = response.content.strip()

    return {
        "optimized_prompt": optimized_prompt,
        "current_step": "prompt_optimized",
        "history": state.get("history", []) + [{"step": "prompt_optimizer", "prompt": optimized_prompt}]
    }