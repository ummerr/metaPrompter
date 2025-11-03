import pytest

from src.character_builder import CharacterBuilder, Character

def test_character_builder_initialization():
    """Tests that the CharacterBuilder class can be instantiated."""
    builder = CharacterBuilder()
    assert isinstance(builder, CharacterBuilder)

def test_create_character_returns_character_object():
    """Tests that the create_character method returns a Character object."""
    builder = CharacterBuilder()
    character = builder.create_character({"name": "Zorp", "appearance": "A friendly alien"})
    assert isinstance(character, Character)
    assert character.name == "Zorp"
    assert character.appearance == "A friendly alien"
    assert character.age == "Ageless" # Default value

def test_create_character_uses_defaults():
    """Tests that the method uses default values for missing fields."""
    builder = CharacterBuilder()
    character = builder.create_character({})
    assert character.name == "Unnamed Character"
    assert character.age == "Ageless"
    assert character.appearance == "An average-looking person"
    assert character.personality == "A mysterious and intriguing personality"
    assert character.backstory == "A character with a hidden past"
