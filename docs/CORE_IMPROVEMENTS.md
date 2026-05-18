# Core Improvements Log

## 2026-05-18

### Changes Made
- Added `core/config.py` for centralized configuration
- Added `utils/prompt_loader.py` as reusable utility
- Improved `prompts/prompt_optimizer.md` with better system prompt
- Enhanced `main.py` UX (better output formatting)
- Confirmed API-first approach (DeepSeek + future Qwen via API)

### Current Core Flow
1. User provides simple idea
2. `prompt_optimizer_node` uses DeepSeek to expand it into high-quality prompt
3. Result is returned with history

### Next Steps
- Integrate prompt_loader into the node
- Add simple retry logic
- Prepare for Qwen image generation node

## Design Decisions
- API first (no local model priority in early stage)
- Prompts managed in `prompts/` folder as .md files
- Keep initial error handling simple