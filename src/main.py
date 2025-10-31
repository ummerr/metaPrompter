from .generation_engine import GenerationEngine
from .quality_validator import QualityValidator
from .knowledge_base import KnowledgeBase
from .character_builder import CharacterBuilder
from .prompt_structure import VeoPrompt
from .identity import Identity
from .output_formatter import OutputFormatter
from .story_writer import StoryWriter
from .analysis_engine import AnalysisEngine

class CoreOrchestrator:
    """The central controller that manages the flow of data through all layers."""

    def __init__(self):
        """Initializes the CoreOrchestrator and all its component layers."""
        self.identity = Identity()
        self.knowledge_base = KnowledgeBase()
        self.character_builder = CharacterBuilder()
        self.analysis_engine = AnalysisEngine()
        self.story_writer = StoryWriter(self.analysis_engine)
        self.generation_engine = GenerationEngine(self.knowledge_base, self.character_builder)
        self.quality_validator = QualityValidator()
        self.output_formatter = OutputFormatter()

    def process_request(self, user_input: str) -> VeoPrompt:
        """Processes a user's request to generate a complete VeoPrompt."""
        story_plan = self.story_writer.write_story(user_input)
        analyzed_request = {"scenes": story_plan}
        generated_prompt = self.generation_engine.generate_prompt(analyzed_request)
        final_prompt = self.quality_validator.validate_and_finalize(generated_prompt)
        return final_prompt
