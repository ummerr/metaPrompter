import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Adjust path to import from the root project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.main import CoreOrchestrator
from src.prompt_structure import VeoPrompt

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

orchestrator = CoreOrchestrator()

class UserInput(BaseModel):
    text: str

@app.post("/generate-prompt/", response_model=VeoPrompt)
async def generate_prompt(user_input: UserInput):
    """
    Accepts user text input and returns a generated VeoPrompt.
    """
    prompt = orchestrator.process_request(user_input.text)
    return orchestrator.output_formatter.to_dict(prompt)
