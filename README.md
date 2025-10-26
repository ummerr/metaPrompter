# Veo-3 Meta-Framework Implementation

This project is a Python implementation of the conceptual Veo-3 Meta-Framework. It provides a structured, layer-based architecture to transform a high-level creative idea into a detailed, 7-component prompt suitable for an advanced video generation model.

This implementation was built following a rigorous, AI-driven, Test-First Development process as outlined in the project's `ARCHITECTURE.md`.

## Features

*   **Modular, Layered Architecture:** The application is divided into distinct, single-responsibility layers:
    *   `AnalysisEngine`: Parses the initial user input.
    *   `KnowledgeBase`: Provides technical specifications for the video output.
    *   `CharacterBuilder`: Creates detailed character descriptions.
    *   `GenerationEngine`: Constructs the main prompt components.
    *   `QualityValidator`: Refines the prompt and adds negative keywords.
*   **Structured & Validated Output:** The final output is a `pydantic` validated `VeoPrompt` object, ensuring all required components are present and correctly formatted.
*   **Test-Driven Development:** The entire codebase was developed using a strict TDD methodology, with a full suite of `pytest` unit tests, ensuring high code quality and reliability.

## Installation

1.  **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd veo3-meta-framework-impl
    ```

2.  **Create a virtual environment (recommended):**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

The main entry point for the application is the `CoreOrchestrator` class. The included `run_app.py` script provides a clear example of how to use it.

To run the example from your terminal:
```sh
python3 run_app.py
```

This will execute the following logic from `run_app.py`:

```python
# run_app.py
from src.main import CoreOrchestrator

# 1. Initialize the main orchestrator
orchestrator = CoreOrchestrator()

# 2. Define your high-level idea
user_idea = "A futuristic detective exploring a rainy, neon-lit city."

# 3. Process the idea to generate the final prompt
final_prompt = orchestrator.process_request(user_idea)

# 4. Print the structured output
print("Generated VeoPrompt:")
print(final_prompt.model_dump_json(indent=2))
```

This will output a JSON object containing the structured 7-component prompt, ready for use.
