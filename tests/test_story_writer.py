import pytest
from src.story_writer import StoryWriter
from src.analysis_engine import AnalysisEngine

def test_story_writer_initialization():
    """Tests that the StoryWriter class can be instantiated."""
    analysis_engine = AnalysisEngine()
    story_writer = StoryWriter(analysis_engine)
    assert isinstance(story_writer, StoryWriter)

def test_write_story_returns_5_scenes():
    """Tests that the write_story method returns a list of 5 parsed scenes."""
    analysis_engine = AnalysisEngine()
    story_writer = StoryWriter(analysis_engine)
    story = story_writer.write_story("A brave knight")
    assert isinstance(story, list)
    assert len(story) == 5
    assert isinstance(story[0], dict)
