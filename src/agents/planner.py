from langchain_core.prompts import ChatPromptTemplate
from src.core.prompt_loader import load_prompt
from src.core.llm import get_llm
from src.models.schemas import ResearchPlan

llm = get_llm()
PROMPT = load_prompt("planner")

async def planner_node(state):
    planner = llm.with_structured_output(
        ResearchPlan, method="json_mode", strict=True
    )

    chain = ChatPromptTemplate.from_template(PROMPT) | planner

    plan = await chain.ainvoke({
        "topic": state["topic"],
        "domain": state["domain"],
        "sections": state["sections"]
    })

    return {"plan": plan}
