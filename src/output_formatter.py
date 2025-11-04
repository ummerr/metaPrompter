from typing import Dict, Any
from .prompt_structure import VeoPrompt

class OutputFormatter:
    """Formats the VeoPrompt object into different output formats."""

    def to_dict(self, prompt: VeoPrompt) -> Dict[str, Any]:
        """Formats the prompt as a dictionary."""
        return prompt.model_dump()

    def to_string(self, prompt: VeoPrompt) -> str:
        """Formats the prompt as a string for display."""
        output = []
        for i, scene in enumerate(prompt.scenes):
            output.append(f"--- Scene {i+1} ---")
            output.append(f"Subject: {scene.subject}")
            output.append(f"Action: {scene.action}")
            output.append(f"Scene: {scene.scene}")
            output.append(f"Composition: {scene.composition}")
            output.append(f"Sounds: {scene.sounds}")
            output.append(f"Image URL: {scene.image_url}")
            output.append(f"Consistent Universe: {scene.consistent_universe}")
            output.append("")
        
        output.append("--- Prompt Details ---")
        output.append(f"Style: {prompt.style}")
        output.append(f"Dialogue: {prompt.dialogue}")
        output.append(f"Technical: {', '.join(prompt.technical)}")
        output.append(f"Negative Prompt: {prompt.negative_prompt}")
        
        return "\n".join(output)
