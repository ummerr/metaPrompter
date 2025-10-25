import pytest
from pydantic import ValidationError

# This import will fail because the file doesn't exist yet, which is the goal.
from src.prompt_structure import VeoPrompt

def test_veo_prompt_successful_creation():
    """Tests the successful creation of a VeoPrompt object with valid data."""
    prompt = VeoPrompt(
        subject="a happy robot",
        action="walking through a sunlit forest",
        scene="A lush, green forest with tall trees and sunlight filtering through the canopy.",
        style="cinematic, photorealistic",
        dialogue="",
        sounds="birds chirping, leaves rustling",
        technical=["4K", "16:9"]
    )
    assert prompt.subject == "a happy robot"
    assert prompt.action == "walking through a sunlit forest"
    assert prompt.style == "cinematic, photorealistic"

def test_veo_prompt_missing_required_field_raises_error():
    """Tests that a pydantic ValidationError is raised if a required field (e.g., subject) is missing."""
    with pytest.raises(ValidationError):
        VeoPrompt(
            action="running",
            scene="a field",
            style="documentary",
            dialogue="",
            sounds="wind blowing",
            technical=["1080p"]
        )
