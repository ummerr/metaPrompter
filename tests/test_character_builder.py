import pytest

# This import will fail as the module does not yet exist.
from src.character_builder import CharacterBuilder

def test_character_builder_initialization():
    """Tests that the CharacterBuilder class can be instantiated."""
    builder = CharacterBuilder()
    assert isinstance(builder, CharacterBuilder)

def test_create_character_returns_string():
    """Tests that the create_character method returns a string."""
    builder = CharacterBuilder()
    character_description = builder.create_character({"name": "Zorp", "description": "A friendly alien"})
    assert isinstance(character_description, str)

def test_create_character_output_contains_name():
    """Tests that the output string contains the character's name."""
    builder = CharacterBuilder()
    character_description = builder.create_character({"name": "Zorp", "description": "A friendly alien"})
    assert "Zorp" in character_description
