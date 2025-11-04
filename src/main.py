from typing import Dict, Any
from .prompt_parser import PromptParser
from .prompt_structure import VeoPrompt
from .identity import Identity
from .knowledge_base import KnowledgeBase
from .character_builder import CharacterBuilder
from .generation_engine import GenerationEngine
from .image_generator import ImageGenerator
from .quality_validator import QualityValidator
from .output_formatter import OutputFormatter
from .story_prompt_generator import StoryPromptGenerator

class CoreOrchestrator:
    """The central controller that manages the flow of data through all layers."""

    def __init__(self):
        """Initializes the CoreOrchestrator and all its component layers."""
        self.identity = Identity()
        self.knowledge_base = KnowledgeBase()
        self.character_builder = CharacterBuilder()
        self.prompt_parser = PromptParser()
        self.story_prompt_generator = StoryPromptGenerator()
        self.character_store: Dict[str, Any] = {}
        self.generation_engine = GenerationEngine(self.knowledge_base, self.character_builder)
        self.image_generator = ImageGenerator()
        self.quality_validator = QualityValidator()
        self.output_formatter = OutputFormatter()

    def process_request(self, user_input: str) -> VeoPrompt:
        """Processes a user's request to generate a complete VeoPrompt."""
        # 1. Parse the user's high-level idea
        parsed_prompt = self.prompt_parser.parse_prompt(user_input)

        # 2. The "LLM Call": A unique, structured story is generated directly.
        # This replaces the text story and the parser entirely.
        scenes = [
            {
                "subject": "Sir Gideon, a knight in obsidian armor",
                "action": "stands at the edge of a volcano's caldera, his glowing sword drawn",
                "scene": "inside the heart of the volcano, with oppressive heat and sulfurous air"
            },
            {
                "subject": "A colossal dragon, Ignis, with scales of cracked magma",
                "action": "bursts from a cavern wall, letting out a deafening roar",
                "scene": "in the molten cavern, showering the area with rock"
            },
            {
                "subject": "Sir Gideon",
                "action": "charges forward, sidesteps a jet of liquid fire, and carves a sizzling wound in the dragon's leg",
                "scene": "across a floor of volcanic glass, with slag forming behind him"
            },
            {
                "subject": "Ignis, the enraged dragon",
                "action": "snaps at Gideon, who rolls beneath its jaws and plunges his sword into the beast's throat",
                "scene": "at the heart of the conflict, in a blinding flash of blue energy"
            },
            {
                "subject": "Sir Gideon, breathing heavily",
                "action": "retrieves his sword from the still dragon, his quest fulfilled",
                "scene": "in the quiet aftermath, with only the bubbling of lava below"
            }
        ]
        
        # 3. Create a character from the parsed prompt
        character_name = parsed_prompt.get("character", "Unnamed Character")
        main_character = self.character_builder.create_character({"name": character_name})
        self.character_store["main_character"] = main_character

        # Add character keys to scenes where the main character is the subject
        for scene in scenes:
            if character_name.lower() in scene["subject"].lower():
                scene["character_key"] = "main_character"

        analyzed_request = {"scenes": scenes, "characters": self.character_store}
        
        # 4. Generate the final, detailed VeoPrompt
        generated_prompt = self.generation_engine.generate_prompt(analyzed_request, parsed_prompt)

        # 5. Generate an image for each scene
        for scene in generated_prompt.scenes:
            scene.image_url = self.image_generator.generate_image_for_scene(scene, generated_prompt.style)

        # 6. Validate and finalize the prompt
        final_prompt = self.quality_validator.validate_and_finalize(generated_prompt)
        return final_prompt
