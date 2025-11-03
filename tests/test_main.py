import pytest

from src.main import CoreOrchestrator
from src.prompt_structure import VeoPrompt, Scene

def test_core_orchestrator_initialization():
    """Tests that the CoreOrchestrator class can be instantiated."""
    orchestrator = CoreOrchestrator()
    assert isinstance(orchestrator, CoreOrchestrator)

def test_process_request_creates_character():
    """Tests that the process_request method creates a character and stores it."""
    orchestrator = CoreOrchestrator()
    user_input = "Sir Gideon"
    prompt = orchestrator.process_request(user_input)
    assert "main_character" in orchestrator.character_store
    assert orchestrator.character_store["main_character"].name == "Sir Gideon"
