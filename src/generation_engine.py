from typing import Dict, Any
from .prompt_structure import VeoPrompt
from .knowledge_base import KnowledgeBase
from .character_builder import CharacterBuilder

class GenerationEngine:
    """Takes the analyzed request and constructs the full 7-component VeoPrompt."""

    def __init__(self, knowledge_base: KnowledgeBase, character_builder: CharacterBuilder):
        """Initializes the GenerationEngine with its necessary tools.

        Args:
            knowledge_base (KnowledgeBase): An instance of the KnowledgeBase to access
                technical constraints.
            character_builder (CharacterBuilder): An instance of the CharacterBuilder
                for creating detailed characters.
        """
        self._knowledge_base = knowledge_base
        self._character_builder = character_builder

    def generate_prompt(self, analyzed_request: Dict[str, Any]) -> VeoPrompt:
        """Constructs a VeoPrompt from an analyzed request.

        This method orchestrates the creative assembly of the prompt, using the
        analyzed request and specialized tools.

        Args:
            analyzed_request (Dict[str, Any]): The structured output from the
                AnalysisEngine.

        Returns:
            VeoPrompt: A populated, but not yet finalized, VeoPrompt object.
        """
        return VeoPrompt(
            subject=analyzed_request.get("subject", "A generic subject"),
            action=analyzed_request.get("action", "A generic action"),
            scene=analyzed_request.get("scene", "A generic scene"),
            style="cinematic",
            dialogue="",
            sounds="",
            technical=["1080p"]
        )
