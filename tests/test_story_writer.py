import pytest
from src.story_writer import StoryWriter
from src.character_builder import CharacterBuilder, Character

def test_story_writer_initialization():
    """Tests that the StoryWriter class can be instantiated."""
    character_builder = CharacterBuilder()
    story_writer = StoryWriter(character_builder)
    assert isinstance(story_writer, StoryWriter)

def test_write_story_generates_a_story():
    """Tests that the write_story method generates a story with content."""
    character_builder = CharacterBuilder()
    story_writer = StoryWriter(character_builder)
    story_data = story_writer.write_story({"character": "a brave knight", "theme": "honor"})
    scenes = story_data["scenes"]
    assert len(scenes[0]["action"]) > 0
    assert len(scenes[0]["scene"]) > 0

def test_write_story_uses_character():
    """Tests that the write_story method uses the generated character in the scenes."""
    character_builder = CharacterBuilder()
    story_writer = StoryWriter(character_builder)
    story_data = story_writer.write_story({"character": "a brave knight", "theme": "honor"})
    main_character = story_data["characters"]["main_character"]
    assert main_character.name == "a brave knight"
    assert main_character.name in story_data["scenes"][0]["subject"]

def test_write_story_is_descriptive():
    """Tests that the generated story is descriptive."""
    character_builder = CharacterBuilder()
    story_writer = StoryWriter(character_builder)
    story_data = story_writer.write_story({"character": "a brave knight", "theme": "honor"})
    full_story_action = " ".join([s["action"] for s in story_data["scenes"]])
    assert "kingdom" in full_story_action
    assert "dragon" in full_story_action

def test_write_story_uses_theme():
    """Tests that the write_story method uses the theme to generate the story."""
    character_builder = CharacterBuilder()
    story_writer = StoryWriter(character_builder)
    story_data = story_writer.write_story({"character": "a brave knight", "theme": "honor"})
    full_story_action = " ".join([s["action"] for s in story_data["scenes"]])
    assert "honor" in full_story_action


def test_write_story_adds_consistent_universe():
    """Tests that the write_story method adds a consistent universe to each scene."""
    character_builder = CharacterBuilder()
    story_writer = StoryWriter(character_builder)
    story_data = story_writer.write_story({"character": "a brave knight", "theme": "honor"})
    scenes = story_data["scenes"]
    for scene in scenes:
        assert "consistent_universe" in scene
        assert len(scene["consistent_universe"]) > 0
