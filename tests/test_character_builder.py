import pytest

from src.character_builder import CharacterBuilder

def test_character_builder_initialization():
    """Tests that the CharacterBuilder class can be instantiated."""
    builder = CharacterBuilder()
    assert isinstance(builder, CharacterBuilder)

def test_create_character_returns_detailed_string():
    """Tests that the create_character method returns a detailed string."""
    builder = CharacterBuilder()
    character_description = builder.create_character({"name": "Zorp", "appearance": "A friendly alien"})
    assert isinstance(character_description, str)
    assert "Zorp" in character_description
    assert "Appearance: A friendly alien" in character_description
    assert "Age: Ageless" in character_description # Default value

def test_create_character_uses_defaults():
    """Tests that the method uses default values for missing fields."""
    builder = CharacterBuilder()
    character_description = builder.create_character({})
    assert "Unnamed Character" in character_description
    assert "Ageless" in character_description
    assert "An average-looking person" in character_description
    assert "A mysterious and intriguing personality" in character_description
    assert "A character with a hidden past" in character_description
