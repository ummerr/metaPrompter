import pytest

# This import will fail, which is the goal of the RED step in TDD.
from src.knowledge_base import KnowledgeBase

def test_knowledge_base_is_singleton():
    """Tests that the KnowledgeBase class correctly implements the singleton pattern."""
    kb1 = KnowledgeBase()
    kb2 = KnowledgeBase()
    assert kb1 is kb2, "KnowledgeBase should be a singleton, but different instances were created."

def test_get_max_duration_returns_integer():
    """Tests that the get_max_duration method returns an integer value as specified in the architecture."""
    kb = KnowledgeBase()
    max_duration = kb.get_max_duration()
    assert isinstance(max_duration, int)
    assert max_duration > 0

def test_get_supported_resolutions_returns_list_of_strings():
    """Tests that get_supported_resolutions method returns a list of strings."""
    kb = KnowledgeBase()
    resolutions = kb.get_supported_resolutions()
    assert isinstance(resolutions, list)
    assert all(isinstance(res, str) for res in resolutions)
    assert len(resolutions) > 0
