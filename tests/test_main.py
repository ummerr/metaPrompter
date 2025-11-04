import pytest

from src.main import CoreOrchestrator
from src.prompt_structure import VeoPrompt
from src.story_prompt_generator import StoryPromptGenerator

def test_core_orchestrator_initialization():
    """Tests that the CoreOrchestrator instantiates modules correctly."""
    orchestrator = CoreOrchestrator()
    assert isinstance(orchestrator, CoreOrchestrator)
    assert isinstance(orchestrator.story_prompt_generator, StoryPromptGenerator)
    assert not hasattr(orchestrator, 'story_parser') # Ensure parser is gone

def test_process_request_end_to_end():
    """Tests the full end-to-end process_request method."""
    orchestrator = CoreOrchestrator()
    user_input = "A knight named Sir Gideon fighting a dragon in a volcano"
    
    final_prompt = orchestrator.process_request(user_input)
    
    assert isinstance(final_prompt, VeoPrompt)
    assert len(final_prompt.scenes) == 5
    
    # Check that the final prompt subject contains the hardcoded subject
    # This confirms the GenerationEngine is still enhancing the subject
    assert "Sir Gideon" in final_prompt.scenes[0].subject
    assert "knight in obsidian armor" in final_prompt.scenes[0].subject
    
    # Check a specific detail from the hardcoded scenes
    assert "Ignis" in final_prompt.scenes[1].subject
    
    # Check that the final prompt action contains the hardcoded action
    assert "plunges his sword" in final_prompt.scenes[3].action
    
    # Check that image generation ran
    assert final_prompt.scenes[4].image_url is not None
