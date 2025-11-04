import pytest
from src.story_prompt_generator import StoryPromptGenerator

@pytest.fixture
def generator_and_data():
    """Pytest fixture to provide a StoryPromptGenerator and sample parsed prompt."""
    generator = StoryPromptGenerator()
    parsed_prompt = {
        "character": "a cyber-detective",
        "theme": "finding a lost memory",
        "setting": "a neon-drenched city",
        "genre": "sci-fi"
    }
    return generator, parsed_prompt

def test_generator_initialization():
    """Tests that the StoryPromptGenerator can be instantiated."""
    generator = StoryPromptGenerator()
    assert isinstance(generator, StoryPromptGenerator)

def test_generate_story_prompt_returns_string(generator_and_data):
    """Tests that the generate_story_prompt method returns a string."""
    generator, parsed_prompt = generator_and_data
    story_prompt = generator.generate_story_prompt(parsed_prompt)
    assert isinstance(story_prompt, str)

def test_prompt_contains_all_elements(generator_and_data):
    """Tests that the generated prompt string contains all the key elements."""
    generator, parsed_prompt = generator_and_data
    story_prompt = generator.generate_story_prompt(parsed_prompt)
    
    assert parsed_prompt["character"] in story_prompt
    assert parsed_prompt["theme"] in story_prompt
    assert parsed_prompt["setting"] in story_prompt
    assert parsed_prompt["genre"] in story_prompt
    assert "5-act story" in story_prompt
