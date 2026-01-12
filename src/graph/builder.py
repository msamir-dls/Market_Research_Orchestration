from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from src.agents.planner import planner_node
from src.agents.planner import planner_node
from src.agents.worker import worker_node
from src.agents.reviewer import reviewer_node
from src.models.schemas import ResearchPlan, SectionReport, FinalReport

class AgentState(TypedDict):
    topic: str
    domain: str
    sections: int
    plan: ResearchPlan
    draft_sections: List[SectionReport]
    final_report: FinalReport

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("workers", worker_node)
    graph.add_node("reviewer", reviewer_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "workers")
    graph.add_edge("workers", "reviewer")
    graph.add_edge("reviewer", END)

    return graph.compile()
