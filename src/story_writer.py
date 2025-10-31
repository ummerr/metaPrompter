from typing import List, Dict, Any
from .analysis_engine import AnalysisEngine

class StoryWriter:
    """Generates a multi-scene story from a high-level user prompt."""

    def __init__(self, analysis_engine: AnalysisEngine):
        """Initializes the StoryWriter with an AnalysisEngine."""
        self._analysis_engine = analysis_engine

    def write_story(self, user_prompt: str) -> List[Dict[str, Any]]:
        """Takes a user prompt and returns a list of 5 parsed scene dictionaries."""
        # This is a placeholder implementation. A real implementation will use the
        # user_prompt to generate a more specific story.
        story_plan = [
            f"Scene 1: Introduction - A character named {user_prompt} is introduced.",
            f"Scene 2: Inciting Incident - {user_prompt} encounters a challenge.",
            f"Scene 3: Rising Action - {user_prompt} struggles with the challenge.",
            f"Scene 4: Climax - {user_prompt} confronts the challenge directly.",
            f"Scene 5: Resolution - The story of {user_prompt} concludes.",
        ]

        parsed_scenes = []
        for scene_description in story_plan:
            parsed_scenes.extend(self._analysis_engine.analyze_request(scene_description)["scenes"])
        
        return parsed_scenes
