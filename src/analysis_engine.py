from typing import Dict, Any
import spacy

class AnalysisEngine:
    """Parses the user's high-level text input to identify key entities."""

    def __init__(self):
        """Initializes the AnalysisEngine and loads the spaCy model."""
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading 'en_core_web_sm' model...")
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

    def analyze_request(self, user_input: str) -> Dict[str, Any]:
        """Analyzes the raw user input string for multiple scenes using NLP."""
        scene_inputs = user_input.strip().split('\n')
        scenes = []
        for scene_input in scene_inputs:
            if not scene_input.strip():
                continue
            
            doc = self.nlp(scene_input)
            
            subjects = [chunk.text for chunk in doc.noun_chunks]
            subject = subjects[0] if subjects else ""
            
            action = ""
            if subject:
                action = scene_input.replace(subject, "", 1).strip()
            
            scenes.append({"subject": subject, "action": action, "scene": ""})
        return {"scenes": scenes}
