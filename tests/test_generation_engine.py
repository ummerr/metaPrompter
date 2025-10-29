import pytest

from src.generation_engine import GenerationEngine
from src.knowledge_base import KnowledgeBase
from src.character_builder import CharacterBuilder
from src.prompt_structure import VeoPrompt, Scene

def test_generation_engine_initialization():
    """Tests that the GenerationEngine can be instantiated with its dependencies."""
    kb = KnowledgeBase()
    cb = CharacterBuilder()
    engine = GenerationEngine(knowledge_base=kb, character_builder=cb)
    assert isinstance(engine, GenerationEngine)

def test_generate_prompt_returns_veo_prompt_object():
    """Tests that the generate_prompt method returns an instance of VeoPrompt."""
    kb = KnowledgeBase()
    cb = CharacterBuilder()
    engine = GenerationEngine(knowledge_base=kb, character_builder=cb)
    analyzed_request = {"scenes": [{"subject": "a robot", "action": "exploring", "scene": "a cave"}]}
    prompt = engine.generate_prompt(analyzed_request)
    assert isinstance(prompt, VeoPrompt)
    assert isinstance(prompt.scenes, list)

def test_generate_prompt_creates_scenes_from_request():
    """Tests that the generate_prompt method correctly creates scenes from the analyzed request."""
    kb = KnowledgeBase()
    cb = CharacterBuilder()
    engine = GenerationEngine(knowledge_base=kb, character_builder=cb)
    analyzed_request = {
        "scenes": [
            {"subject": "A happy robot", "action": "walking through", "scene": "a sunlit forest"},
            {"subject": "A sad robot", "action": "sitting by", "scene": "a lonely moon"}
        ]
    }
    prompt = engine.generate_prompt(analyzed_request)
    assert len(prompt.scenes) == 2
    assert isinstance(prompt.scenes[0], Scene)
    assert analyzed_request["scenes"][0]["subject"] in prompt.scenes[0].subject
    assert analyzed_request["scenes"][1]["subject"] in prompt.scenes[1].subject

def test_generate_prompt_uses_knowledge_base():
    """Tests that the generate_prompt method uses the knowledge base for technical specs."""
    kb = KnowledgeBase()
    cb = CharacterBuilder()
    engine = GenerationEngine(knowledge_base=kb, character_builder=cb)
    analyzed_request = {"scenes": [{"subject": "a robot", "action": "exploring", "scene": "a cave"}]}
    prompt = engine.generate_prompt(analyzed_request)
    assert prompt.technical[0] == kb.get_supported_resolutions()[0]

def test_generate_prompt_calls_character_builder():
    """Tests that the generate_prompt method calls the character builder when appropriate."""
    kb = KnowledgeBase()
    cb = CharacterBuilder()
    engine = GenerationEngine(knowledge_base=kb, character_builder=cb)
    analyzed_request = {"scenes": [{"subject": "A mysterious character", "action": "walks", "scene": "a dark alley"}]}
    prompt = engine.generate_prompt(analyzed_request)
    assert "Character Name: A mysterious character" in prompt.scenes[0].subject

def test_generate_prompt_generates_composition():
    """Tests that the generate_prompt method generates a composition for each scene."""
    kb = KnowledgeBase()
    cb = CharacterBuilder()
    engine = GenerationEngine(knowledge_base=kb, character_builder=cb)
    analyzed_request = {"scenes": [{"subject": "a robot", "action": "exploring", "scene": "a cave"}]}
    prompt = engine.generate_prompt(analyzed_request)
    assert prompt.scenes[0].composition is not None
    assert len(prompt.scenes[0].composition) > 0

def test_generate_prompt_generates_sounds():
    """Tests that the generate_prompt method generates sounds based on keywords."""
    kb = KnowledgeBase()
    cb = CharacterBuilder()
    engine = GenerationEngine(knowledge_base=kb, character_builder=cb)
    analyzed_request = {"scenes": [{"subject": "a cat", "action": "playing", "scene": "a garden"}]}
    prompt = engine.generate_prompt(analyzed_request)
    assert "cat purring, meowing" in prompt.sounds
