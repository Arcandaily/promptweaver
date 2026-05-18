# PromptWeaver 技术架构

## 模型分工

- **DeepSeek-v4-flash**: 主大脑 - 提示词构建、优化、迭代重构、意图理解
- **Qwen 生图模型**: 文生图 / 图生图
- **Qwen-VL**: 图像理解（性价比版）

## Agent 流程（LangGraph）

1. Prompt Builder Node (DeepSeek)
2. Image Generator Node (Qwen)
3. Image Analyzer Node (Qwen-VL + DeepSeek 指导)
4. Iteration Controller

## 本地优先

- 支持 API Key 调用
- 后续可支持 Ollama 本地模型

## 前端

Vue 3 + TypeScript + 现代 UI 设计