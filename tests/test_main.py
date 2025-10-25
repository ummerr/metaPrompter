import pytest

# This import will fail as the module does not yet exist.
from src.main import CoreOrchestrator
from src.prompt_structure import VeoPrompt

def test_core_orchestrator_initialization():
    """Tests that the CoreOrchestrator class can be instantiated."""
    orchestrator = CoreOrchestrator()
    assert isinstance(orchestrator, CoreOrchestrator)

def test_process_request_returns_veo_prompt_object():
    """Tests that the process_request method returns an instance of VeoPrompt."""
    orchestrator = CoreOrchestrator()
    user_input = "a robot exploring a cave"
    prompt = orchestrator.process_request(user_input)
    assert isinstance(prompt, VeoPrompt)

def test_process_request_output_is_finalized():
    """Tests that the prompt returned by process_request has been finalized (i.e., has a negative prompt)."""
    orchestrator = CoreOrchestrator()
    user_input = "a robot exploring a cave"
    prompt = orchestrator.process_request(user_input)
    assert len(prompt.negative_prompt) > 0
