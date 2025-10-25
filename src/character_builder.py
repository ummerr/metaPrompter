from typing import Dict, Any

class CharacterBuilder:
    """A specialized tool to create detailed character descriptions.

    This class uses a template to generate rich character details that can be
    used by the Generation Engine.
    """

    def create_character(self, high_level_description: Dict[str, Any]) -> str:
        """Creates a detailed, structured character string from a high-level description.

        Args:
            high_level_description (Dict[str, Any]): A dictionary containing key
                attributes of the character, such as name, age, or role.

        Returns:
            str: A detailed, structured character string for use in the prompt.
        """
        name = high_level_description.get("name", "Unnamed Character")
        description = high_level_description.get("description", "")
        return f"A character named {name}. {description}".strip()
