from typing import Dict, Any
import spacy

class PromptParser:
    """Parses the user's initial prompt to extract key information."""

    def __init__(self):
        """Initializes the PromptParser with a spaCy model."""
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading 'en_core_web_sm' model...")
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

    def parse_prompt(self, user_prompt: str) -> Dict[str, Any]:
        """Parses the user prompt to extract the main character and theme."""
        doc = self.nlp(user_prompt)
        
        # A more robust implementation would use more advanced NLP techniques.
        subjects = [chunk.text for chunk in doc.noun_chunks]
        character = subjects[0] if subjects else user_prompt
        
        theme = ""
        if len(subjects) > 1:
            theme = " ".join(subjects[1:])

        return {"character": character, "theme": theme}
