import pytest
from src.output_formatter import OutputFormatter
from src.prompt_structure import VeoPrompt, Scene

def test_output_formatter_to_dict():
    """Tests that the to_dict method returns a dictionary."""
    formatter = OutputFormatter()
    prompt = VeoPrompt(
        scenes=[Scene(subject="a", action="b", scene="c", composition="d", consistent_universe="e")],
        style="f",
        dialogue="g",
        sounds="h",
        technical=["i"],
    )
    output_dict = formatter.to_dict(prompt)
    assert isinstance(output_dict, dict)
    assert output_dict["scenes"][0]["consistent_universe"] == "e"

def test_output_formatter_to_string():
    """Tests that the to_string method returns a formatted string."""
    formatter = OutputFormatter()
    prompt = VeoPrompt(
        scenes=[Scene(subject="a", action="b", scene="c", composition="d", consistent_universe="e")],
        style="f",
        dialogue="g",
        sounds="h",
        technical=["i"],
    )
    output_str = formatter.to_string(prompt)
    assert isinstance(output_str, str)
    assert "--- Scene 1 ---" in output_str
    assert "Subject: a" in output_str
    assert "Composition: d" in output_str
    assert "Consistent Universe: e" in output_str
    assert "Style: f" in output_str
