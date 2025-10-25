from .prompt_structure import VeoPrompt

class QualityValidator:
    """Validates the generated VeoPrompt against rules and generates negative prompts."""

    def validate_and_finalize(self, prompt: VeoPrompt) -> VeoPrompt:
        """Validates and finalizes a VeoPrompt object.

        This method applies a set of quality rules to the generated prompt and
        appends a negative prompt to improve the final output quality.

        Args:
            prompt (VeoPrompt): The VeoPrompt object to validate.

        Returns:
            VeoPrompt: The validated and finalized VeoPrompt object.
        """
        # This is a placeholder implementation. A real implementation would have
        # more sophisticated validation logic.
        if len(prompt.subject.strip()) == 0:
            raise ValueError("Subject cannot be empty.")

        prompt.negative_prompt = "low quality, blurry, jpeg artifacts"
        return prompt
