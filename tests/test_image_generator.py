import pytest
from src.image_generator import ImageGenerator
from src.prompt_structure import Scene

def test_image_generator_initialization():
    """Tests that the ImageGenerator can be instantiated."""
    generator = ImageGenerator()
    assert isinstance(generator, ImageGenerator)

def test_generate_image_for_scene_returns_url():
    """Tests that the method returns a URL-like string."""
    generator = ImageGenerator()
    scene = Scene(
        subject="a knight",
        action="fighting a dragon",
        scene="a volcano",
        composition="wide shot",
        consistent_universe="fantasy",
        sounds="roaring, clashing steel"
    )
    style = "epic fantasy"
    url = generator.generate_image_for_scene(scene, style)
    assert isinstance(url, str)
    assert url.startswith("https://images.example.com/")
    assert url.endswith(".png")

def test_generate_image_is_deterministic():
    """Tests that the same scene input always produces the same image URL."""
    generator = ImageGenerator()
    scene1 = Scene(
        subject="a robot",
        action="exploring a cave",
        scene="a dark, mysterious cave",
        composition="low angle",
        consistent_universe="sci-fi",
        sounds="dripping water, metallic footsteps"
    )
    scene2 = Scene(
        subject="a robot",
        action="exploring a cave",
        scene="a dark, mysterious cave",
        composition="low angle",
        consistent_universe="sci-fi",
        sounds="dripping water, metallic footsteps"
    )
    style = "cinematic sci-fi"
    
    url1 = generator.generate_image_for_scene(scene1, style)
    url2 = generator.generate_image_for_scene(scene2, style)
    
    assert url1 == url2
