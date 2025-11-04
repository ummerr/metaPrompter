import pytest
from pydantic import ValidationError

from src.prompt_structure import VeoPrompt, Scene

def test_veo_prompt_successful_creation():
    """Tests the successful creation of a VeoPrompt object with valid data."""
    scenes = [
        Scene(
            subject="a happy robot",
            action="walking through a sunlit forest",
            scene="A lush, green forest with tall trees and sunlight filtering through the canopy.",
            composition="close-up shot",
            consistent_universe="test universe",
            sounds="birds chirping, leaves rustling"
        )
    ]
    prompt = VeoPrompt(
        scenes=scenes,
        style="cinematic, photorealistic",
        dialogue="",
        technical=["4K", "16:9"]
    )
    assert prompt.scenes == scenes
    assert prompt.style == "cinematic, photorealistic"

def test_veo_prompt_missing_required_field_raises_error():
    """Tests that a pydantic ValidationError is raised if the required 'scenes' field is missing."""
    with pytest.raises(ValidationError):
        VeoPrompt(
            style="documentary",
            dialogue="",
            technical=["1080p"]
        )
