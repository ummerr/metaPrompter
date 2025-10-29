from .prompt_structure import VeoPrompt

class QualityValidator:
    """Validates the generated VeoPrompt against rules and generates negative prompts."""

    def validate_and_finalize(self, prompt: VeoPrompt) -> VeoPrompt:
        """Validates and finalizes a VeoPrompt object, checking each scene and generating negative prompts."""
        if not prompt.scenes:
            raise ValueError("Prompt must contain at least one scene.")

        for i, scene in enumerate(prompt.scenes):
            if len(scene.subject.strip()) == 0:
                raise ValueError(f"Subject cannot be empty in scene {i+1}.")

        # Generate context-aware negative prompts
        negative_prompts = [prompt.negative_prompt]
        if "photorealistic" in prompt.style.lower():
            negative_prompts.append("cartoon, anime, 3d render")
        
        if any("person" in scene.subject.lower() for scene in prompt.scenes):
            negative_prompts.append("deformed, ugly, disfigured")

        prompt.negative_prompt = ", ".join(filter(None, negative_prompts))

        return prompt
