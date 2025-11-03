import pytest

from src.quality_validator import QualityValidator
from src.prompt_structure import VeoPrompt, Scene

def test_quality_validator_initialization():
    """Tests that the QualityValidator class can be instantiated."""
    validator = QualityValidator()
    assert isinstance(validator, QualityValidator)

def test_validate_and_finalize_returns_veo_prompt_object():
    """Tests that the validate_and_finalize method returns an instance of VeoPrompt."""
    validator = QualityValidator()
    prompt = VeoPrompt(
        scenes=[Scene(subject="a test subject", action="a test action", scene="a test scene", composition="close-up", consistent_universe="test universe")],
        style="cinematic",
        dialogue="",
        sounds="",
        technical=["1080p"]
    )
    final_prompt = validator.validate_and_finalize(prompt)
    assert isinstance(final_prompt, VeoPrompt)

def test_validate_and_finalize_raises_error_for_empty_subject():
    """Tests that an error is raised if a scene has an empty subject."""
    validator = QualityValidator()
    prompt = VeoPrompt(
        scenes=[Scene(subject="", action="a test action", scene="a test scene", composition="close-up", consistent_universe="test universe")],
        style="cinematic",
        dialogue="",
        sounds="",
        technical=["1080p"]
    )
    with pytest.raises(ValueError, match="Subject cannot be empty in scene 1"):
        validator.validate_and_finalize(prompt)

def test_validate_and_finalize_raises_error_for_no_scenes():
    """Tests that an error is raised if the prompt has no scenes."""
    validator = QualityValidator()
    prompt = VeoPrompt(
        scenes=[],
        style="cinematic",
        dialogue="",
        sounds="",
        technical=["1080p"]
    )
    with pytest.raises(ValueError, match="Prompt must contain at least one scene."):
        validator.validate_and_finalize(prompt)

def test_validate_and_finalize_adds_photorealistic_negatives():
    """Tests that photorealistic negative prompts are added for the correct style."""
    validator = QualityValidator()
    prompt = VeoPrompt(
        scenes=[Scene(subject="a test subject", action="a test action", scene="a test scene", composition="close-up", consistent_universe="test universe")],
        style="photorealistic",
        dialogue="",
        sounds="",
        technical=["1080p"]
    )
    final_prompt = validator.validate_and_finalize(prompt)
    assert "cartoon, anime, 3d render" in final_prompt.negative_prompt

def test_validate_and_finalize_adds_person_negatives():
    """Tests that person-related negative prompts are added for the correct subject."""
    validator = QualityValidator()
    prompt = VeoPrompt(
        scenes=[Scene(subject="a person walking", action="a test action", scene="a test scene", composition="close-up", consistent_universe="test universe")],
        style="cinematic",
        dialogue="",
        sounds="",
        technical=["1080p"]
    )
    final_prompt = validator.validate_and_finalize(prompt)
    assert "deformed, ugly, disfigured" in final_prompt.negative_prompt
