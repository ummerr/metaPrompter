from .analysis_engine import AnalysisEngine
from .generation_engine import GenerationEngine
from .quality_validator import QualityValidator
from .knowledge_base import KnowledgeBase
from .character_builder import CharacterBuilder
from .prompt_structure import VeoPrompt
from .identity import Identity
from .output_formatter import OutputFormatter

class CoreOrchestrator:
    """The central controller that manages the flow of data through all layers."""

    def __init__(self):
        """Initializes the CoreOrchestrator and all its component layers."""
        self.identity = Identity()
        self.knowledge_base = KnowledgeBase()
        self.character_builder = CharacterBuilder()
        self.analysis_engine = AnalysisEngine()
        self.generation_engine = GenerationEngine(self.knowledge_base, self.character_builder)
        self.quality_validator = QualityValidator()
        self.output_formatter = OutputFormatter()

    def process_request(self, user_input: str) -> VeoPrompt:
        """Processes a user's request to generate a complete VeoPrompt.

        This is the main entry point for the application. It takes a raw user
        string and returns a final, validated VeoPrompt.

        Args:
            user_input (str): The user's high-level request string.

        Returns:
            VeoPrompt: The final, formatted VeoPrompt ready for use.
        """
        analyzed_request = self.analysis_engine.analyze_request(user_input)
        generated_prompt = self.generation_engine.generate_prompt(analyzed_request)
        final_prompt = self.quality_validator.validate_and_finalize(generated_prompt)
        return final_prompt
