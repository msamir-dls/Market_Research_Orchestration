from typing import List
from pydantic import BaseModel, Field, ConfigDict

class ResearchTask(BaseModel):
    title: str
    focus: str
    questions: List[str]

    model_config = ConfigDict(extra="forbid")

class ResearchPlan(BaseModel):
    market_context: str
    tasks: List[ResearchTask]

    model_config = ConfigDict(extra="forbid")

class SectionReport(BaseModel):
    title: str
    content: str
    key_stats: List[str]

    model_config = ConfigDict(extra="forbid")

class FinalReport(BaseModel):
    executive_summary: str
    full_report: str
    strategic_recommendations: List[str]

    model_config = ConfigDict(extra="forbid")
