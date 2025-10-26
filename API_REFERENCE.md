# API Reference

This document provides a detailed API reference for the `src` directory, generated from the code's docstrings.

## `src.prompt_structure`

### class `VeoPrompt`
Defines the validated data structure for the final Veo 3 prompt output. This class uses pydantic for data validation to ensure that all generated prompts conform to the required 7-component format.

## `src.knowledge_base`

### class `KnowledgeBase`
Loads and provides access to Veo 3 technical specifications. This class is implemented as a singleton to ensure a single, consistent source of truth for technical data throughout the application.

#### `get_max_duration(self) -> int`
Returns the maximum video duration in seconds.
- **Returns**: `int` - The maximum duration in seconds.

#### `get_supported_resolutions(self) -> List[str]`
Returns a list of supported video resolutions.
- **Returns**: `List[str]` - A list of supported resolutions.

## `src.analysis_engine`

### class `AnalysisEngine`
Parses the user's high-level text input to identify key entities. This engine is responsible for the initial interpretation of the user's creative intent.

#### `analyze_request(self, user_input: str) -> Dict[str, Any]`
Analyzes the raw user input string. This method will eventually use NLP techniques to extract structured data. For the initial implementation, it will perform a basic keyword analysis.
- **Args**:
    - `user_input` (str): The raw user input string from the end-user.
- **Returns**: `Dict[str, Any]` - A structured dictionary representing the analyzed request.

## `src.character_builder`

### class `CharacterBuilder`
A specialized tool to create detailed character descriptions. This class uses a template to generate rich character details that can be used by the Generation Engine.

#### `create_character(self, high_level_description: Dict[str, Any]) -> str`
Creates a detailed, structured character string from a high-level description.
- **Args**:
    - `high_level_description` (Dict[str, Any]): A dictionary containing key attributes of the character, such as name, age, or role.
- **Returns**: `str` - A detailed, structured character string for use in the prompt.

## `src.generation_engine`

### class `GenerationEngine`
Takes the analyzed request and constructs the full 7-component VeoPrompt.

#### `__init__(self, knowledge_base: KnowledgeBase, character_builder: CharacterBuilder)`
Initializes the GenerationEngine with its necessary tools.
- **Args**:
    - `knowledge_base` (KnowledgeBase): An instance of the KnowledgeBase to access technical constraints.
    - `character_builder` (CharacterBuilder): An instance of the CharacterBuilder for creating detailed characters.

#### `generate_prompt(self, analyzed_request: Dict[str, Any]) -> VeoPrompt`
Constructs a VeoPrompt from an analyzed request. This method orchestrates the creative assembly of the prompt, using the analyzed request and specialized tools.
- **Args**:
    - `analyzed_request` (Dict[str, Any]): The structured output from the AnalysisEngine.
- **Returns**: `VeoPrompt` - A populated, but not yet finalized, VeoPrompt object.

## `src.quality_validator`

### class `QualityValidator`
Validates the generated VeoPrompt against rules and generates negative prompts.

#### `validate_and_finalize(self, prompt: VeoPrompt) -> VeoPrompt`
Validates and finalizes a VeoPrompt object. This method applies a set of quality rules to the generated prompt and appends a negative prompt to improve the final output quality.
- **Args**:
    - `prompt` (VeoPrompt): The VeoPrompt object to validate.
- **Returns**: `VeoPrompt` - The validated and finalized VeoPrompt object.

## `src.main`

### class `CoreOrchestrator`
The central controller that manages the flow of data through all layers.

#### `__init__(self)`
Initializes the CoreOrchestrator and all its component layers.

#### `process_request(self, user_input: str) -> VeoPrompt`
Processes a user's request to generate a complete VeoPrompt. This is the main entry point for the application. It takes a raw user string and returns a final, validated VeoPrompt.
- **Args**:
    - `user_input` (str): The user's high-level request string.
- **Returns**: `VeoPrompt` - The final, formatted VeoPrompt ready for use.
