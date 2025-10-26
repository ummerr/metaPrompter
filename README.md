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

## Example Usage

To run the application, execute the `run_app.py` script:

```sh
python3 run_app.py
```

This script takes a high-level idea as input and generates a structured JSON prompt as output.

### Example Input

The `run_app.py` script is pre-configured with the following input:

```python
user_idea = "A futuristic detective exploring a rainy, neon-lit city."
```

### Example Output

Running the script will produce the following JSON output:

```json
{
  "subject": "A generic subject",
  "action": "A generic action",
  "scene": "A generic scene",
  "style": "cinematic",
  "dialogue": "",
  "sounds": "",
  "technical": [
    "1080p"
  ],
  "negative_prompt": "low quality, blurry, jpeg artifacts"
}
```
