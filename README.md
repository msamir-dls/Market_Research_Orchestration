# Market Research Orchestration

Using the Orchestration Worker Agentic Design Paradigm to create a market research system that captures summaries and outputs relevant decisions.

## Overview
A production-grade, multi-agent market research system that orchestrates LLM agents (planner, parallel workers, reviewer) using LangGraph and asyncio.

## Example Usage
```bash
export GROQ_API_KEY=your_key
python -m src.main \
  --topic "Solid State Batteries in EVs 2025" \
  --domain energy \
  --sections 4
