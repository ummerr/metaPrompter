from .story_writer import StoryWriter
from .prompt_parser import PromptParser
from .prompt_structure import VeoPrompt
from .identity import Identity
from .knowledge_base import KnowledgeBase
from .character_builder import CharacterBuilder
from .generation_engine import GenerationEngine
from .quality_validator import QualityValidator
from .output_formatter import OutputFormatter

class CoreOrchestrator:
    """The central controller that manages the flow of data through all layers."""

    def __init__(self):
        """Initializes the CoreOrchestrator and all its component layers."""
        self.identity = Identity()
        self.knowledge_base = KnowledgeBase()
        self.character_builder = CharacterBuilder()
        self.prompt_parser = PromptParser()
        self.story_writer = StoryWriter(self.character_builder)
        self.character_store: Dict[str, Any] = {}
        self.generation_engine = GenerationEngine(self.knowledge_base, self.character_builder)
        self.quality_validator = QualityValidator()
        self.output_formatter = OutputFormatter()

    def process_request(self, user_input: str) -> VeoPrompt:
        """Processes a user's request to generate a complete VeoPrompt."""
        parsed_prompt = self.prompt_parser.parse_prompt(user_input)
        story_data = self.story_writer.write_story(parsed_prompt)
        self.character_store.update(story_data["characters"])
        
        analyzed_request = {"scenes": story_data["scenes"], "characters": self.character_store}
        generated_prompt = self.generation_engine.generate_prompt(analyzed_request)
        final_prompt = self.quality_validator.validate_and_finalize(generated_prompt)
        return final_prompt
