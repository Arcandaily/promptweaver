from typing import TypedDict, List, Optional


class PromptWeaverState(TypedDict):
    """
    PromptWeaver 核心状态定义

    这个 State 是整个 Agent 流程的核心，后续会根据需求添加字段。
    """
    # 用户原始输入
    user_input: str

    # 当前优化后的提示词
    optimized_prompt: Optional[str]

    # 历史记录（用于迭代时参考）
    history: List[dict]

    # 当前步骤（用于调试和日志）
    current_step: str

    # 错误信息（简单版，后续强化）
    error: Optional[str]