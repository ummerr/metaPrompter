import pytest
from src.prompt_parser import PromptParser

def test_prompt_parser_initialization():
    """Tests that the PromptParser class can be instantiated."""
    parser = PromptParser()
    assert isinstance(parser, PromptParser)

def test_parse_prompt_extracts_character():
    """Tests that the parse_prompt method extracts the character from the prompt."""
    parser = PromptParser()
    parsed_prompt = parser.parse_prompt("a brave knight fighting a dragon")
    assert parsed_prompt["character"] == "a brave knight"

def test_parse_prompt_extracts_theme():
    """Tests that the parse_prompt method extracts the theme from the prompt."""
    parser = PromptParser()
    parsed_prompt = parser.parse_prompt("a brave knight fighting a dragon")
    assert parsed_prompt["theme"] == "a dragon"
