# PromptWeaver 智绘提示师

**PromptWeaver** 是一个基于双模型（DeepSeek + Qwen）的智能生图提示词优化与生成系统。

核心理念：**简单输入 = 高质量结果** + 智能迭代优化

## 项目目标

- 让不会写提示词的普通用户也能稳定得到高质量 AI 图像
- 使用 **DeepSeek-v4-flash** 负责提示词构建、优化、迭代重构
- 使用 **Qwen** 系列模型负责图像生成与理解
- 支持图生图 + 基于图片的智能迭代
- 内置专业预设库（风格、场景、画风等）
- 本地优先支持

## 技术架构

- **Agent 编排** : LangGraph
- **后端** : FastAPI + Python
- **前端** : Vue 3 + TypeScript + Tailwind
- **模型分工**
  - DeepSeek-v4-flash 主大脑（提示词工程师）
  - Qwen 生图模型（画家）
  - Qwen-VL（眼睛，性价比版）

## 状态

正在开发中... 

详情请查看 Issues 和 Projects。

---

**Created by Grok + Arcandaily** | 开源项目 | 适合学习与二次开发