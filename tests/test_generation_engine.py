import pytest
from src.generation_engine import GenerationEngine
from src.knowledge_base import KnowledgeBase
from src.character_builder import CharacterBuilder
from src.prompt_structure import VeoPrompt, Scene

@pytest.fixture
def engine_and_data():
    """Pytest fixture to provide a GenerationEngine and sample data for a sci-fi prompt."""
    kb = KnowledgeBase()
    cb = CharacterBuilder()
    engine = GenerationEngine(knowledge_base=kb, character_builder=cb)
    
    character = cb.create_character({"name": "Zane", "appearance": "a rugged cyborg", "personality": "a lone wolf"})
    # The analyzed_request contains the 5-act structure from the StoryWriter
    analyzed_request = {
        "scenes": [
            {"subject": "Zane", "action": "is seen calibrating a complex device", "scene": "in a sterile, white laboratory", "character_key": "main_character"},
            {"subject": "Zane", "action": "reacts as an alien artifact activates", "scene": "within the laboratory", "character_key": "main_character"},
            {"subject": "Zane", "action": "is shown dodging laser fire", "scene": "in a crumbling corridor", "character_key": "main_character"},
            {"subject": "Zane", "action": "overloads the reactor core", "scene": "in the engine room", "character_key": "main_character"},
            {"subject": "Zane", "action": "gazes out at a nebula", "scene": "from the bridge of a starship", "character_key": "main_character"},
        ],
        "characters": {"main_character": character}
    }
    parsed_prompt = {
        "character": "Zane",
        "theme": "redemption",
        "setting": "a derelict starship",
        "genre": "sci-fi"
    }
    
    return engine, analyzed_request, parsed_prompt

def test_generate_prompt_returns_veo_prompt(engine_and_data):
    """Tests that generate_prompt returns a VeoPrompt object."""
    engine, analyzed_request, parsed_prompt = engine_and_data
    prompt = engine.generate_prompt(analyzed_request, parsed_prompt)
    assert isinstance(prompt, VeoPrompt)

def test_cinematography_is_intentional(engine_and_data):
    """Tests that camera composition is intentionally chosen based on the story act."""
    engine, analyzed_request, parsed_prompt = engine_and_data
    prompt = engine.generate_prompt(analyzed_request, parsed_prompt)
    # Act 1 (Introduction) should be a wide, establishing shot.
    assert "establishing shot" in prompt.scenes[0].composition
    # Act 4 (Climax) should have intense close-ups.
    assert "close-up shots" in prompt.scenes[3].composition

def test_descriptions_are_enriched(engine_and_data):
    """Tests that descriptions are enriched with genre-specific adjectives and adverbs."""
    engine, analyzed_request, parsed_prompt = engine_and_data
    prompt = engine.generate_prompt(analyzed_request, parsed_prompt)
    first_scene = prompt.scenes[0]
    # Check for an adjective from the sci-fi vocab
    assert any(adj in first_scene.subject for adj in ["gleaming", "holographic", "utilitarian", "cybernetic"])
    # Check for an adverb from the sci-fi vocab
    assert any(adv in first_scene.action for adv in ["silently", "precisely"])

def test_style_is_sophisticated(engine_and_data):
    """Tests that the style prompt is a composite of multiple cinematic elements."""
    engine, analyzed_request, parsed_prompt = engine_and_data
    prompt = engine.generate_prompt(analyzed_request, parsed_prompt)
    assert "cinematic" in prompt.style
    assert "sci-fi" in prompt.style
    assert "in the style of" in prompt.style
    assert "shot on" in prompt.style
    assert any(director in prompt.style for director in ["Denis Villeneuve", "Ridley Scott"])

def test_technical_specs_are_detailed(engine_and_data):
    """Tests that the technical specs include resolution, fps, and aspect ratio."""
    engine, analyzed_request, parsed_prompt = engine_and_data
    prompt = engine.generate_prompt(analyzed_request, parsed_prompt)
    assert len(prompt.technical) >= 2 # At least resolution and one other spec
    assert any("fps" in spec for spec in prompt.technical)

def test_dialogue_is_still_simulated(engine_and_data):
    """Tests that dialogue is generated for the climax scene."""
    engine, analyzed_request, parsed_prompt = engine_and_data
    prompt = engine.generate_prompt(analyzed_request, parsed_prompt)
    assert "Zane" in prompt.dialogue
    assert "whispers" in prompt.dialogue
    assert '"It all ends now."' in prompt.dialogue
