# Meeting Insights Generator

This project is designed to help users gain insightful points about meeting participants, the industry, the market, and current situations. By taking inputs such as meeting participants, meeting context, and meeting objectives, the system performs extensive research to provide valuable information.

CrewAI has been used to make various agents which would work together in specific roles to generate the output, Google Gemini API has been used to access the LLM model Gemini-1.5-Flash or Groq API can be used to run the agents on Llama3-70b LLM, Exa has been used for making tools for the agents to access the web and perform extensive research about the given topics and FastAPI has been used to create an API which can connect the entire pipeline to the frontend.

## Features

- Researches and gathers information about meeting participants.
- Analyzes the industry and market related to the meeting.
- Provides current situational insights relevant to the meeting context.
- Generates actionable and insightful points to assist in the meeting preparation.

## Project Structure

The project consists of the following main components:

- `main.py`: The main entry point of the application.
- `agents.py`: Contains the logic for different agents that perform specific tasks.
- `tasks.py`: Defines various tasks that the agents need to perform.
- `tools.py`: Includes tools and utilities to aid in data gathering and analysis.

## Getting Started

### Prerequisites

- Python 3.10 or above
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/nabhpatodi10/meeting-insights-generator.git
    cd meeting-insights-generator
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the main application:

    ```bash
    python main.py
    ```

2. Provide the necessary inputs when prompted:
    - Meeting participants
    - Meeting context
    - Meeting objectives

3. Receive insightful points to aid in your meeting preparation.

## License

This project is licensed under the MIT License.
