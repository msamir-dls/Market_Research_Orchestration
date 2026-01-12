from langchain_core.prompts import ChatPromptTemplate
from src.core.prompt_loader import load_prompt
from src.core.llm import get_llm
from src.models.schemas import FinalReport

llm = get_llm()
PROMPT = load_prompt("reviewer")

async def reviewer_node(state):
    drafts = "\n\n".join(
        f"## {s.title}\n{s.content}\n\nKey Stats:\n- " +
        "\n- ".join(s.key_stats)
        for s in state["draft_sections"]
    )

    reviewer = llm.with_structured_output(
        FinalReport, method="json_mode", strict=True
    )

    chain = ChatPromptTemplate.from_template(PROMPT) | reviewer

    report = await chain.ainvoke({
        "topic": state["topic"],
        "drafts": drafts
    })

    return {"final_report": report}
