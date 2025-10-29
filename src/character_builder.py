from typing import Dict, Any

class CharacterBuilder:
    """A specialized tool to create detailed character descriptions."""

    def create_character(self, high_level_description: Dict[str, Any]) -> str:
        """Creates a detailed, structured character string from a high-level description."""
        character_template = {
            "name": high_level_description.get("name", "Unnamed Character"),
            "age": high_level_description.get("age", "Ageless"),
            "appearance": high_level_description.get("appearance", "An average-looking person"),
            "personality": high_level_description.get("personality", "A mysterious and intriguing personality"),
            "backstory": high_level_description.get("backstory", "A character with a hidden past"),
        }

        return (
            f"Character Name: {character_template['name']}\n"
            f"Age: {character_template['age']}\n"
            f"Appearance: {character_template['appearance']}\n"
            f"Personality: {character_template['personality']}\n"
            f"Backstory: {character_template['backstory']}"
        )
