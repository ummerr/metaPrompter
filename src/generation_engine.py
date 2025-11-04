import random
from typing import Dict, Any, List
from .prompt_structure import VeoPrompt, Scene
from .knowledge_base import KnowledgeBase
from .character_builder import CharacterBuilder

class GenerationEngine:
    """Takes the analyzed request and constructs a sophisticated, Veo-optimal prompt."""

    def __init__(self, knowledge_base: KnowledgeBase, character_builder: CharacterBuilder):
        """Initializes the GenerationEngine with cinematic knowledge bases."""
        self._knowledge_base = knowledge_base
        self._character_builder = character_builder

        # Maps story act index to specific, intentional cinematography
        self._cinematography_map = {
            0: "A wide, sweeping establishing shot that showcases the vastness of the environment.", # Introduction
            1: "A dramatic dolly zoom (Vertigo effect) to create a sense of unease or revelation.", # Inciting Incident
            2: "A dynamic, low-angle tracking shot that follows the subject's determined movement.", # Rising Action
            3: "A series of rapid, intense close-up shots focusing on the character's expressions and actions.", # Climax
            4: "A slow, elegant panning shot across the landscape, settling on the thoughtful subject." # Resolution
        }

        # Provides genre-specific keywords for enriching descriptions
        self._enrichment_vocab = {
            "sci-fi": {"adjectives": ["gleaming", "holographic", "utilitarian", "cybernetic"], "adverbs": ["silently", "precisely"]},
            "fantasy": {"adjectives": ["ancient", "ethereal", "glowing", "monolithic"], "adverbs": ["majestically", "solemnly"]},
            "noir": {"adjectives": ["shadowy", "rain-slicked", "grimy", "stark"], "adverbs": ["suspiciously", "wearily"]},
            "default": {"adjectives": ["cinematic", "dramatic", "vivid"], "adverbs": ["intently", "carefully"]}
        }

        # Knowledge base for creating sophisticated style prompts
        self._style_knowledge_base = {
            "sci-fi": {
                "directors": ["Denis Villeneuve", "Ridley Scott"],
                "lighting": ["harsh neon lighting", "volumetric god rays"],
                "film_stocks": ["shot on 35mm film, Kodak Vision3 500T"],
            },
            "fantasy": {
                "directors": ["Guillermo del Toro", "Peter Jackson"],
                "lighting": ["soft, diffused natural light", "high contrast, torch-lit shadows"],
                "film_stocks": ["shot on digital, Arri Alexa, high dynamic range"],
            },
            "noir": {
                "directors": ["Alfred Hitchcock", "Orson Welles"],
                "lighting": ["single-source key light", "chiaroscuro lighting"],
                "film_stocks": ["shot on black and white 35mm film, high contrast"],
            },
            "default": {
                "directors": ["Roger Deakins"], # Cinematographer, but influential style
                "lighting": ["golden hour lighting"],
                "film_stocks": ["cinematic film grain"],
            }
        }

        self._sound_map = {
            "city": "distant sirens, traffic hum, pedestrian chatter",
            "forest": "rustling leaves, birds chirping, wind howling through trees",
            "space": "the low hum of a starship, electronic beeps, deep silence",
            "fantasy": "magical chimes, distant dragon roars, crackling fire",
            "sci-fi": "laser blasts, spaceship engines, robotic whirring, computer voice alerts",
            "rain": "heavy rain falling, thunder rumbling, water dripping",
            "default": "ambient environmental sounds, subtle musical score"
        }

    def generate_prompt(self, analyzed_request: Dict[str, Any], parsed_prompt: Dict[str, Any]) -> VeoPrompt:
        """Constructs a VeoPrompt using deep cinematic knowledge."""
        output_scenes: List[Scene] = []
        characters = analyzed_request.get("characters", {})
        genre = parsed_prompt.get("genre", "default")
        dialogue = ""

        # Get genre-specific enrichment vocab
        vocab = self._enrichment_vocab.get(genre, self._enrichment_vocab["default"])

        for i, scene_data in enumerate(analyzed_request.get("scenes", [])):
            subject = scene_data.get("subject", "A generic subject")
            action = scene_data.get("action", "A generic action")
            scene_desc = scene_data.get("scene", "A generic scene")
            consistent_universe = scene_data.get("consistent_universe", "")
            character_key = scene_data.get("character_key")

            # 1. Intentional Cinematography
            composition = self._cinematography_map.get(i, "A standard medium shot.")

            # 2. Enriched Descriptions
            adjective = random.choice(vocab["adjectives"])
            adverb = random.choice(vocab["adverbs"])

            if character_key and character_key in characters:
                character = characters[character_key]
                # Enhance the original subject, don't replace it
                original_subject = scene_data.get("subject", character.name)
                enhanced_subject = f"A {adjective}, high-resolution shot of {original_subject}, focusing on their {character.personality} nature and {character.appearance}."
            else:
                enhanced_subject = f"A {adjective}, high-resolution shot of {subject}"
            
            enhanced_action = f"{adverb}, {action}"
            enhanced_scene = f"in the {adjective} setting of: {scene_desc}"

            # Simulate dialogue for the climax (Act 4, index 3)
            if i == 3 and character_key in characters:
                dialogue = f'{characters[character_key].name} whispers {adverb}, "It all ends now."'

            # Generate sounds for the current scene
            scene_sounds = [self._sound_map.get(genre, self._sound_map["default"])]
            for keyword, sound in self._sound_map.items():
                if keyword in subject.lower() or keyword in action.lower() or keyword in scene_desc.lower():
                    scene_sounds.append(sound)
            sounds_string = ", ".join(list(set(scene_sounds)))

            output_scenes.append(
                Scene(
                    subject=enhanced_subject,
                    action=enhanced_action,
                    scene=enhanced_scene,
                    composition=composition,
                    consistent_universe=consistent_universe,
                    character_key=character_key,
                    sounds=sounds_string,
                )
            )

        # 3. Sophisticated Style Prompt
        style_kb = self._style_knowledge_base.get(genre, self._style_knowledge_base["default"])
        style_components = [
            "cinematic",
            genre,
            f"in the style of {random.choice(style_kb['directors'])}",
            random.choice(style_kb['lighting']),
            random.choice(style_kb['film_stocks'])
        ]
        style = ", ".join(style_components)

        # 4. Detailed Technical Specifications
        technical_specs = [
            random.choice(self._knowledge_base.get_supported_resolutions()),
            random.choice(["24fps", "30fps"]),
            random.choice(["16:9", "2.35:1"])
        ]
        
        return VeoPrompt(
            scenes=output_scenes,
            style=style,
            dialogue=dialogue,
            technical=list(set(technical_specs))
        )
