import pytest
from src.analysis_engine import AnalysisEngine

def test_analysis_engine_initialization():
    """Tests that the AnalysisEngine class can be instantiated."""
    engine = AnalysisEngine()
    assert isinstance(engine, AnalysisEngine)

def test_analyze_request_parses_simple_sentence():
    """Tests that a simple sentence is parsed correctly."""
    engine = AnalysisEngine()
    user_input = "A cat is sitting on a mat."
    analysis = engine.analyze_request(user_input)
    assert len(analysis["scenes"]) == 1
    scene = analysis["scenes"][0]
    assert scene["subject"] == "A cat"
    assert scene["action"] == "is sitting on a mat."
    assert scene["scene"] == ""

def test_analyze_request_parses_complex_sentence():
    """Tests that a more complex sentence is parsed correctly."""
    engine = AnalysisEngine()
    user_input = "A fluffy white cat is gracefully chasing a small brown mouse."
    analysis = engine.analyze_request(user_input)
    assert len(analysis["scenes"]) == 1
    scene = analysis["scenes"][0]
    assert scene["subject"] == "A fluffy white cat"
    assert scene["action"] == "is gracefully chasing a small brown mouse."
    assert scene["scene"] == ""

def test_analyze_request_parses_multiple_scenes():
    """Tests that a multi-line input is parsed into multiple scenes."""
    engine = AnalysisEngine()
    user_input = "A cat on a mat.\nA dog in a bog."
    analysis = engine.analyze_request(user_input)
    assert len(analysis["scenes"]) == 2

def test_analyze_request_handles_empty_lines():
    """Tests that empty lines in the input are handled gracefully."""
    engine = AnalysisEngine()
    user_input = "A cat on a mat.\n\nA dog in a bog."
    analysis = engine.analyze_request(user_input)
    assert len(analysis["scenes"]) == 2
