from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from dotenv import load_dotenv
load_dotenv()
from crewai import Crew
from tasks import MeetingPrepTasks
from agents import MeetingPrepAgents

app = FastAPI()

tasks = MeetingPrepTasks()
agents = MeetingPrepAgents()
    
research_agent = agents.research_agent()
industry_analysis_agent = agents.industry_analysis_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()

@app.get("/")
def read_root():
    return {"data": {"Welcome Text":"Welcome to Meeting Agent"}}

class meeting_details(BaseModel):
    meeting_participants: str
    meeting_context: str
    meeting_objective: str

@app.post("/meeting_agent")
def meeting_agent(data: meeting_details):
    research_task = tasks.research_task(research_agent, data.meeting_participants, data.meeting_context)
    industry_analysis_task = tasks.industry_analysis_task(industry_analysis_agent, data.meeting_participants, data.meeting_context)
    meeting_strategy_task = tasks.meeting_strategy_task(meeting_strategy_agent, data.meeting_context, data.meeting_objective)
    summary_and_briefing_task = tasks.summary_and_briefing_task(summary_and_briefing_agent, data.meeting_context, data.meeting_objective)
    
    meeting_strategy_task.context = [research_task, industry_analysis_task]
    summary_and_briefing_task.context = [research_task, industry_analysis_task, meeting_strategy_task]
    
    crew = Crew(
      agents=[
        research_agent,
        industry_analysis_agent,
        meeting_strategy_agent,
        summary_and_briefing_agent
      ],
      tasks=[
        research_task,
        industry_analysis_task,
        meeting_strategy_task,
        summary_and_briefing_task
      ]
    )
    
    result = crew.kickoff()
    
    return result
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)