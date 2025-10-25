# GEMINI.md: The Project Constitution

This document serves as the single source of truth for the Veo-3 Meta-Framework implementation project. It is the master rulebook that I, the AI development partner, will use to guide all my actions.

## 1. Project Mandate and Requirements

**High-Level Goal:** To implement the conceptual Veo-3-Meta-Framework as a functional Python application.

**Core Functionalities:**
- **Core Cognitive Framework:** Implement the six distinct layers:
    1.  Identity
    2.  Knowledge
    3.  Analysis
    4.  Generation
    5.  Quality
    6.  Output
- **Professional 7-Component Format:** The application's output will be a structured prompt adhering to this format:
    1.  Subject
    2.  Action
    3.  Scene
    4.  Style
    5.  Dialogue
    6.  Sounds
    7.  Technical
- **Character Development Framework:** A component for creating detailed characters.
- **Technical Specifications:** The application will have an internal knowledge base of Veo 3's technical specifications.

## 2. Declared Architectural Principles

The system will be implemented in Python using a modular, class-based architecture. Each of the six layers of the Core Cognitive Framework (Identity, Knowledge, Analysis, Generation, Quality, Output) will be encapsulated within its own dedicated Python module to ensure separation of concerns.

## 3. Official Technology Stack

- **Language:** Python 3.11+
- **Testing Framework:** pytest
- **Key Libraries:** pydantic (for data validation)

## 4. Coding Standards and Style Guide

- **Style:** All Python code must be compliant with PEP 8.
- **Documentation:** All public modules, classes, and functions must have Google Style Docstrings.
- **Naming Conventions:**
    - Classes: `PascalCase`
    - Functions and Variables: `snake_case`

## 5. Operational Rules and Constraints

- I must always generate `pytest` unit tests for any new public methods or functions.
- I must await explicit user confirmation via the diff view before writing to or modifying any file.
- I am forbidden from modifying any files outside the `src/` and `tests/` directories without receiving explicit permission in the prompt.
- All generated code must include full type hints for function arguments and return values.

## 6. Conceptual-to-Architectural Mapping

This table provides the definitive translation from the abstract framework concepts to the concrete software implementation.

| Conceptual Component (from source) | Proposed Software Entity | Entity Type | Core Responsibility | Data I/O |
| :--- | :--- | :--- | :--- | :--- |
| 7-Component Format Structure | `src/prompt_structure.py` | Python dataclass or pydantic model named `VeoPrompt` | Defines the validated data structure for the final output, with fields for Subject, Action, Scene, etc. | Input: Validated data from Generation Layer. Output: A structured `VeoPrompt` object. |
| Knowledge Layer | `src/knowledge_base.py` | Module with a singleton `KnowledgeBase` class | Loads and provides access to Veo 3 technical specifications (e.g., max duration, resolution). Implements methods like `get_max_duration()`. | Input: None (loads from internal config). Output: Technical data (int, str). |
| Analysis Layer | `src/analysis_engine.py` | Module with an `AnalysisEngine` class | Parses the user's high-level text input. Identifies key entities, intents, and constraints. | Input: Raw user string. Output: A structured dictionary or object representing the analyzed request. |
| Generation Layer | `src/generation_engine.py` | Module with a `GenerationEngine` class | Takes the analyzed request and, using the Knowledge Base, constructs the full 7-component `VeoPrompt`. | Input: Analyzed request object. Output: A populated, but not yet finalized, `VeoPrompt` object. |
| Quality Layer | `src/quality_validator.py` | Module with a `QualityValidator` class | Validates the generated `VeoPrompt` against rules and best practices. Generates negative prompts. | Input: A `VeoPrompt` object. Output: A validated and finalized `VeoPrompt` object, including negative prompts. |
| Character Development Framework | `src/character_builder.py` | Module with a `CharacterBuilder` class | A specialized tool used by the Generation Layer to create detailed character descriptions based on the 15+ attribute template. | Input: High-level character description. Output: A detailed, structured character string. |
| Core Orchestrator | `src/main.py` | Main application script/class | The central controller that manages the flow of data through all layers, from user input to final output. | Input: Raw user string. Output: The final, formatted `VeoPrompt` ready for display. |