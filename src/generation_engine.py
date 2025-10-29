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
            "close-up shot",
            "medium shot",
            "long shot",
            "eye-level shot",
            "high-angle shot",
            "low-angle shot",
        ]

    def generate_prompt(self, analyzed_request: Dict[str, Any]) -> VeoPrompt:
        """Constructs a VeoPrompt from an analyzed request containing multiple scenes."""
        output_scenes: List[Scene] = []
        generated_sounds = []

        for scene_data in analyzed_request.get("scenes", []):
            subject = scene_data.get("subject", "A generic subject")
            action = scene_data.get("action", "A generic action")
            scene = scene_data.get("scene", "A generic scene")

            # Enhance the prompt components to be more descriptive
            enhanced_subject = f"A detailed, high-quality depiction of {subject}"
            enhanced_action = f"{action} in a visually compelling manner"
            enhanced_scene = f"set within a {scene} environment with dramatic, cinematic lighting"
            composition = random.choice(self._compositions)

            if "character" in subject.lower():
                character_details = self._character_builder.create_character({"name": subject})
                enhanced_subject += f"\n\n{character_details}"

            output_scenes.append(
                Scene(
                    subject=enhanced_subject,
                    action=enhanced_action,
                    scene=enhanced_scene,
                    composition=composition,
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
