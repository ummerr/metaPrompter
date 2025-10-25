import pytest

# This import will fail as the module does not yet exist.
from src.quality_validator import QualityValidator
from src.prompt_structure import VeoPrompt

def test_quality_validator_initialization():
    """Tests that the QualityValidator class can be instantiated."""
    validator = QualityValidator()
    assert isinstance(validator, QualityValidator)

def test_validate_and_finalize_returns_veo_prompt_object():
    """Tests that the validate_and_finalize method returns an instance of VeoPrompt."""
    validator = QualityValidator()
    prompt = VeoPrompt(
        subject="a test subject",
        action="a test action",
        scene="a test scene",
        style="cinematic",
        dialogue="",
        sounds="",
        technical=["1080p"]
    )
    final_prompt = validator.validate_and_finalize(prompt)
    assert isinstance(final_prompt, VeoPrompt)

def test_validate_and_finalize_adds_negative_prompt():
    """Tests that the validate_and_finalize method adds a negative prompt to the prompt object."""
    validator = QualityValidator()
    prompt = VeoPrompt(
        subject="a test subject",
        action="a test action",
        scene="a test scene",
        style="cinematic",
        dialogue="",
        sounds="",
        technical=["1080p"]
    )
    final_prompt = validator.validate_and_finalize(prompt)
    assert final_prompt.negative_prompt is not None
    assert len(final_prompt.negative_prompt) > 0
