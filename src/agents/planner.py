from langchain_core.prompts import ChatPromptTemplate
from src.core.prompt_loader import load_prompt
from src.core.llm import get_llm
from src.models.schemas import ResearchPlan
from src.core.metrics import timed
from src.core.cache import get_cached, set_cached

llm = get_llm()
PROMPT = load_prompt("planner")

@timed("Planner")
async def planner_node(state):
    planner = llm.with_structured_output(
        ResearchPlan, method="json_mode", strict=True
    )

    chain = ChatPromptTemplate.from_template(PROMPT) | planner

    key = {
        "topic": state["topic"],
        "domain": state["domain"],
        "sections": state["sections"]
    }

    cached = get_cached(key)
    if cached:
        return {"plan": ResearchPlan(**cached)}

    plan = await chain.ainvoke({
        "topic": state["topic"],
        "domain": state["domain"],
        "sections": state["sections"]
    })
    set_cached(key, plan.model_dump())

    return {"plan": plan}
