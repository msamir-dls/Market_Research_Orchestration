import asyncio
from langchain_core.prompts import ChatPromptTemplate
from src.core.prompt_loader import load_prompt
from src.core.llm import get_llm
from src.models.schemas import SectionReport
from src.core.metrics import timed
from src.core.retry import retry_async

llm = get_llm()
PROMPT = load_prompt("worker")

async def run_task(task):
    worker = llm.with_structured_output(
        SectionReport, method="json_mode", strict=True
    )

    chain = ChatPromptTemplate.from_template(PROMPT) | worker

    async def call():
        return await chain.ainvoke({
            "title": task.title,
            "focus": task.focus,
            "questions": "\n".join(f"- {q}" for q in task.questions)
        })

    return await retry_async(call)

@timed("Workers")
async def worker_node(state):
    tasks = state["plan"].tasks
    results = await asyncio.gather(*(run_task(t) for t in tasks))
    return {"draft_sections": results}
