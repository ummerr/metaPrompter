import pytest

from src.main import CoreOrchestrator
from src.prompt_structure import VeoPrompt, Scene

def test_core_orchestrator_initialization():
    """Tests that the CoreOrchestrator class can be instantiated."""
    orchestrator = CoreOrchestrator()
    assert isinstance(orchestrator, CoreOrchestrator)

def test_process_request_returns_veo_prompt_with_5_scenes():
    """Tests that the process_request method returns a VeoPrompt with 5 scenes."""
    orchestrator = CoreOrchestrator()
    user_input = "a robot exploring a cave"
    prompt = orchestrator.process_request(user_input)
    assert isinstance(prompt, VeoPrompt)
    assert len(prompt.scenes) == 5
