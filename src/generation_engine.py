import random
from typing import Dict, Any, List
from .prompt_structure import VeoPrompt, Scene
from .knowledge_base import KnowledgeBase
from .character_builder import CharacterBuilder

class GenerationEngine:
    """Takes the analyzed request and constructs the full 7-component VeoPrompt."""

    def __init__(self, knowledge_base: KnowledgeBase, character_builder: CharacterBuilder):
        """Initializes the GenerationEngine with its necessary tools."""
        self._knowledge_base = knowledge_base
        self._character_builder = character_builder
        self._sound_map = {
            "cat": "cat purring, meowing",
            "dog": "dog barking, panting",
            "car": "car engine running, tires screeching",
            "rain": "rain falling, thunder rumbling",
        }
        self._compositions = [
            "A dynamic, low-angle shot that tracks with the subject's movement.",
            "A wide, sweeping shot that establishes the vastness of the environment.",
            "A tight, close-up shot that focuses on the subject's facial expressions.",
            "A smooth, panning shot that reveals a new element in the scene.",
            "A handheld, shaky-cam shot that creates a sense of urgency and realism.",
        ]

    def generate_prompt(self, analyzed_request: Dict[str, Any]) -> VeoPrompt:
        """Constructs a VeoPrompt from an analyzed request containing multiple scenes."""
        output_scenes: List[Scene] = []
        generated_sounds = []
        characters = analyzed_request.get("characters", {})

        for scene_data in analyzed_request.get("scenes", []):
            subject = scene_data.get("subject", "A generic subject")
            action = scene_data.get("action", "A generic action")
            scene = scene_data.get("scene", "A generic scene")
            consistent_universe = scene_data.get("consistent_universe", "")

            # Enhance the prompt components to be more descriptive
            if subject in characters:
                character = characters[subject]
                enhanced_subject = f"A cinematic, high-resolution shot of {character.name}, {character.appearance}, {character.personality}"
            else:
                enhanced_subject = f"A cinematic, high-resolution shot of {subject}"
            
            enhanced_action = f"performing the action: {action}"
            enhanced_scene = f"in a setting of: {scene}, with a consistent universe of: {consistent_universe}"
            composition = random.choice(self._compositions)


            output_scenes.append(
                Scene(
                    subject=enhanced_subject,
                    action=enhanced_action,
                    scene=enhanced_scene,
                    composition=composition,
                    consistent_universe=consistent_universe,
                )
            )

            # Generate sounds
            for keyword, sound in self._sound_map.items():
                if keyword in subject.lower() or keyword in action.lower():
                    generated_sounds.append(sound)

        return VeoPrompt(
            scenes=output_scenes,
            style="cinematic",
            dialogue="",
            sounds=", ".join(list(set(generated_sounds))),
            technical=[self._knowledge_base.get_supported_resolutions()[0]]
        )
