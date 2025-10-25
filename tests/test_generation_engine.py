import pytest

# This import will fail as the module does not yet exist.
from src.generation_engine import GenerationEngine
from src.knowledge_base import KnowledgeBase
from src.character_builder import CharacterBuilder
from src.prompt_structure import VeoPrompt

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
    analyzed_request = {"raw_text": "a robot exploring a cave"}
    prompt = engine.generate_prompt(analyzed_request)
    assert isinstance(prompt, VeoPrompt)
