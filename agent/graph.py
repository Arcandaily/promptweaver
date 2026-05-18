from langgraph.graph import StateGraph, END
from agent.state import PromptWeaverState
from agent.nodes.prompt_optimizer import prompt_optimizer_node


def build_graph():
    """
    构建 PromptWeaver 核心工作流

    当前为初始版本，只包含 Prompt Optimizer 节点。
    后续会添加生图节点、迭代节点等。
    """
    workflow = StateGraph(PromptWeaverState)

    # 添加节点
    workflow.add_node("prompt_optimizer", prompt_optimizer_node)

    # 设置入口
    workflow.set_entry_point("prompt_optimizer")

    # 目前直接结束（后续会改为条件边）
    workflow.add_edge("prompt_optimizer", END)

    return workflow.compile()


graph = build_graph()