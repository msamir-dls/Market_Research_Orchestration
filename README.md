# Market_Research_Orchestration
Using the Orchestration worker Agentic Design Paradign to crete market researcher which captures the summary as well as output the relevant decisions.

# Market Research Orchestrator (Multi-Agent, Async)

## Overview
A production-grade, multi-agent market research system that orchestrates LLM agents
(planner, parallel workers, reviewer) using LangGraph and asyncio.

## Architecture
```mermaid
graph TD
    A[User Input] --> B[Planner Agent]
    B --> C[Worker Agents (Parallel)]
    C --> D[Reviewer Agent]
    D --> E[Final Report]


Example:
export GROQ_API_KEY=your_key
python -m src.main \
  --topic "Solid State Batteries in EVs 2025" \
  --domain energy \
  --sections 4
