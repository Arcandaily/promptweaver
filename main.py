"""
PromptWeaver 初始测试脚本

运行方式：
python main.py
"""

import os
from dotenv import load_dotenv
from agent.graph import graph

load_dotenv()

def main():
    print("=== PromptWeaver 初始版本 ===\n")

    user_input = input("请输入你的生图想法: ").strip()

    if not user_input:
        user_input = "a cyberpunk cat sitting on a rooftop in Shanghai at night"

    initial_state = {
        "user_input": user_input,
        "optimized_prompt": None,
        "history": [],
        "current_step": "start",
        "error": None
    }

    print("\n\u6b63在优化提示词...\n")
    result = graph.invoke(initial_state)

    print("\n=== 优化后的提示词 ===")
    print(result.get("optimized_prompt"))
    print("\n=== 完成 ===")


if __name__ == "__main__":
    main()