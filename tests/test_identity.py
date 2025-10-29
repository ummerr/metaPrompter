import pytest
from src.identity import Identity

def test_identity_initialization():
    """Tests that the Identity class can be instantiated and has the correct attributes."""
    identity = Identity()
    assert isinstance(identity, Identity)
    assert identity.name == "Veo-3 Meta-Framework"
    assert identity.version == "0.1.0"
    assert "framework for generating high-quality prompts" in identity.description
