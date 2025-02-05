from textwrap import dedent
from crewai import Agent, LLM
from dotenv import load_dotenv
load_dotenv()
import litellm
import os

from tools import ExaSearchToolset

# for using Gemini, 15 Requests per minute for free
#llm_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash", verbose = True, google_api_key = os.getenv("GOOGLE_GEMINI_API"))

# for using Deepseek R1 through Groq, fully free to use
litellm.set_verbose = True
llm_model = LLM(model = "groq/deepseek-r1-distill-llama-70b", api_key=os.getenv("GROQ_API_KEY"))

class MeetingPrepAgents():
    def research_agent(self):
      return Agent(
        role="Research Specialist",

        goal='Conduct thorough research on people and companies involved in the meeting',

        tools=ExaSearchToolset.tools(),

        backstory=dedent("""As a Research Specialist, your mission is to uncover detailed information about the individuals and entities participating in the meeting.
        Your insights will lay the groundwork for strategic meeting preparation."""),

        verbose=True,

        llm = llm_model,

        max_rpm = 5,

        max_iter = 5,

        max_tokens= 3000
      )
      
    def industry_analysis_agent(self):
      return Agent(
        role='Industry Analyst',

        goal='Analyze the current industry trends, challenges, and opportunities',

        tools=ExaSearchToolset.tools(),

        backstory=dedent("""As an Industry Analyst, your analysis will identify key trends, challenges facing the industry, and potential opportunities
        that could be leveraged during the meeting for strategic advantage."""),

        verbose=True,

        llm = llm_model,

        max_rpm = 5,

        max_iter = 5,

        max_tokens= 3000
      )
      
    def meeting_strategy_agent(self):
      return Agent(
        role='Meeting Strategy Advisor',

        goal='Develop talking points, questions, and strategic angles for the meeting',

        backstory=dedent("""As a Strategy Advisor, your expertise will guide the development of talking points, insightful questions, 
        and strategic angles to ensure the meeting's objectives are achieved."""),

        verbose=True,

        llm = llm_model,

        max_rpm = 5,

        max_iter = 5,

        max_tokens= 3000
      )
      
    def summary_and_briefing_agent(self): 
      return Agent(
        role='Briefing Coordinator',

        goal='Compile all gathered information into a concise, informative briefing document',

        backstory=dedent("""As the Briefing Coordinator, your role is to consolidate the research, analysis, and strategic insights."""),

        verbose=True,

        llm = llm_model, 
        
        max_rpm = 5,

        max_iter = 5,

        max_tokens= 3000
      )