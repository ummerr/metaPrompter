import pytest

from src.main import CoreOrchestrator
from src.prompt_structure import VeoPrompt, Scene

def test_core_orchestrator_initialization():
    """Tests that the CoreOrchestrator class can be instantiated."""
    orchestrator = CoreOrchestrator()
    assert isinstance(orchestrator, CoreOrchestrator)

def test_process_request_returns_veo_prompt_object():
    """Tests that the process_request method returns a valid VeoPrompt object."""
    orchestrator = CoreOrchestrator()
    user_input = "a robot exploring a cave"
    prompt = orchestrator.process_request(user_input)
    assert isinstance(prompt, VeoPrompt)
    assert isinstance(prompt.scenes, list)
    assert len(prompt.scenes) > 0
    assert isinstance(prompt.scenes[0], Scene)

def test_process_request_output_is_finalized():
    """Tests that the prompt returned by process_request has been finalized."""
    orchestrator = CoreOrchestrator()
    user_input = "a robot exploring a cave"
    prompt = orchestrator.process_request(user_input)
    assert len(prompt.negative_prompt) > 0

def test_process_request_with_multi_scene_input():
    """Tests that a multi-line input produces a multi-scene prompt."""
    orchestrator = CoreOrchestrator()
    user_input = "A cat on a mat\nA dog in a bog"
    prompt = orchestrator.process_request(user_input)
    assert len(prompt.scenes) == 2
