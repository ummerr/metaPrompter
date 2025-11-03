from typing import List, Dict, Any
from .character_builder import CharacterBuilder, Character

class StoryWriter:
    """Generates a multi-scene story from a high-level user prompt."""

    def __init__(self, character_builder: CharacterBuilder):
        """Initializes the StoryWriter with a CharacterBuilder."""
        self._character_builder = character_builder

    def write_story(self, parsed_prompt: Dict[str, Any]) -> Dict[str, Any]:
        """Takes a parsed prompt and returns a story with characters and scenes."""
        character_name = parsed_prompt.get("character", "Unnamed Character")
        theme = parsed_prompt.get("theme", "an epic adventure")
        
        main_character = self._character_builder.create_character({"name": character_name})
        
        story_plan = self._generate_story_plan(main_character, theme)
        
        characters = {"main_character": main_character}
        
        return {"scenes": story_plan, "characters": characters}

    def _generate_story_plan(self, character: Character, theme: str) -> List[Dict[str, Any]]:
        """Generates a 5-scene story plan for a character."""
        story_plan = self._generate_full_story(character, theme)
        
        scenes = []
        consistent_universe = self._get_consistent_universe(character.name)
        for scene_data in story_plan:
            scene_data["consistent_universe"] = consistent_universe
            scenes.append(scene_data)
        
        return scenes

    def _generate_full_story(self, character: Character, theme: str) -> List[Dict[str, Any]]:
        """Generates a full 5-scene story for a character and theme."""
        # This is a simulation of a more powerful generative model.
        if "cat" in character.name.lower():
            return [
                {"subject": f"{character.name}, a fluffy white cat", "action": f"is peacefully napping, dreaming of {theme}", "scene": "in a sunlit, cozy apartment"},
                {"subject": "A shimmering, magical butterfly", "action": "flutters in through an open window, drawn by the dreams of {theme}", "scene": "in the apartment"},
                {"subject": f"{character.name}", "action": f"awakens and playfully chases the butterfly, inspired by {theme}", "scene": "through a maze of furniture"},
                {"subject": f"{character.name}", "action": f"leaps and gently catches the butterfly, a culmination of the dream of {theme}", "scene": "in mid-air"},
                {"subject": f"{character.name} and the butterfly", "action": f"sit together by the window, watching the sunset, their friendship a testament to {theme}", "scene": "in the apartment"},
            ]
        elif "knight" in character.name.lower():
            return [
                {"subject": f"{character.name}, a brave knight", "action": f"stands guard, ever vigilant, a symbol of the kingdom's strength and {theme}", "scene": "in a peaceful, prosperous kingdom"},
                {"subject": "A fearsome dragon", "action": f"descends from the mountains, its roar a challenge to the {theme} of the kingdom", "scene": "over the kingdom"},
                {"subject": f"{character.name}", "action": f"rides to face the dragon, his courage fueled by his dedication to {theme}", "scene": "through a dark and treacherous forest"},
                {"subject": f"{character.name}", "action": f"defeats the dragon in a fiery battle, a victory for {theme}", "scene": "in the dragon's lair"},
                {"subject": f"{character.name}", "action": f"returns to the kingdom as a hero, celebrated for preserving the {theme}", "scene": "to a cheering crowd"},
            ]
        else:
            return [
                {"subject": f"{character.name}, a renowned explorer", "action": f"discovers a treasure map, a clue to the legendary {theme}", "scene": "in a dusty, forgotten attic"},
                {"subject": f"{character.name}", "action": f"sails across the ocean, braving storms and sea monsters in pursuit of {theme}", "scene": "on a small, sturdy ship"},
                {"subject": f"{character.name}", "action": f"finds a hidden temple, the next step in the quest for {theme}", "scene": "on a mysterious, jungle-covered island"},
                {"subject": f"{character.name}", "action": f"solves an ancient riddle, unlocking the secrets of {theme}", "scene": "inside the hidden temple"},
                {"subject": f"{character.name}", "action": f"finds a treasure chest, the ultimate reward for the perilous quest for {theme}", "scene": "in a secret chamber"},
            ]

    def _get_consistent_universe(self, character_name: str) -> str:
        """Generates a consistent universe description based on the character's name."""
        if "cat" in character_name.lower():
            return "Cozy, whimsical, soft lighting, miniature world"
        elif "knight" in character_name.lower():
            return "Medieval fantasy, epic scale, high contrast lighting, gothic architecture"
        else:
            return "Adventurous, mysterious, ancient ruins, lush jungles"
