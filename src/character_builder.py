from typing import Dict, Any
from pydantic import BaseModel, Field

class Character(BaseModel):
    """Represents a character in the story."""
    name: str = Field(description="The character's name.")
    age: str = Field(description="The character's age.")
    appearance: str = Field(description="A description of the character's appearance.")
    personality: str = Field(description="A description of the character's personality.")
    backstory: str = Field(description="The character's backstory.")

class CharacterBuilder:
    """A specialized tool to create detailed character descriptions."""

    def create_character(self, high_level_description: Dict[str, Any]) -> Character:
        """Creates a detailed, structured character object from a high-level description."""
        return Character(
            name=high_level_description.get("name", "Unnamed Character"),
            age=high_level_description.get("age", "Ageless"),
            appearance=high_level_description.get("appearance", "An average-looking person"),
            personality=high_level_description.get("personality", "A mysterious and intriguing personality"),
            backstory=high_level_description.get("backstory", "A character with a hidden past"),
        )
