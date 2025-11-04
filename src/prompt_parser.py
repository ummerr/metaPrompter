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
        """Parses the user prompt to extract character, theme, setting, and genre."""
        doc = self.nlp(user_prompt)
        
        # Default values
        parsed_data = {
            "character": "Unnamed Character",
            "theme": "an epic adventure",
            "setting": "a mysterious place",
            "genre": "cinematic"
        }

        # Extract entities, nouns, etc.
        subjects = [chunk.text for chunk in doc.noun_chunks]
        if subjects:
            parsed_data["character"] = subjects[0]

        # Simple keyword-based extraction for genre and setting
        genre_keywords = ["sci-fi", "fantasy", "horror", "comedy", "drama", "noir", "western"]
        setting_keywords = ["city", "forest", "space", "ocean", "castle", "dungeon", "cyberpunk", "steampunk", "apartment", "kingdom"]

        prompt_lower = user_prompt.lower()
        for genre in genre_keywords:
            if genre in prompt_lower:
                parsed_data["genre"] = genre
                break  # Take the first one found

        for setting in setting_keywords:
            if setting in prompt_lower:
                parsed_data["setting"] = setting
                break

        # A simple way to get a theme - find the main action/verb phrase
        root_verb = [token for token in doc if token.dep_ == "ROOT" and token.pos_ == "VERB"]
        if root_verb:
            # Find objects or clauses related to the verb to form a theme
            theme_parts = [child.text for child in root_verb[0].children if child.dep_ in ("dobj", "attr", "acomp")]
            if theme_parts:
                parsed_data["theme"] = f"{root_verb[0].text} {' '.join(theme_parts)}"
            else:
                parsed_data["theme"] = f"the adventure of {parsed_data['character']}"
        elif len(subjects) > 1:
            parsed_data["theme"] = " ".join(subjects[1:])

        return parsed_data
