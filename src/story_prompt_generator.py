from typing import Dict, Any

class StoryPromptGenerator:
    """Generates a detailed prompt for a creative AI to write a unique story."""

    def generate_story_prompt(self, parsed_prompt: Dict[str, Any]) -> str:
        """Takes a parsed prompt and constructs a story-writing prompt."""
        
        prompt = f"""As a creative AI, please write a unique, short, 5-act story based on the following elements. The story must be exactly five paragraphs long, with each paragraph corresponding to one act.

- Genre: {parsed_prompt.get('genre', 'cinematic')}
- Setting: {parsed_prompt.get('setting', 'a mysterious place')}
- Theme: {parsed_prompt.get('theme', 'an epic adventure')}
- Main Character: {parsed_prompt.get('character', 'an unnamed protagonist')}

The five acts are:
1. **Introduction:** Introduce the main character and their world, establishing a sense of normalcy.
2. **Inciting Incident:** A specific event that disrupts the character's world and kicks off the plot.
3. **Rising Action:** The character attempts to deal with the new situation, but faces challenges and the stakes are raised.
4. **Climax:** The story's peak, where the character confronts the main conflict head-on.
5. **Resolution:** The immediate aftermath of the climax, showing the result of the character's actions and the new state of their world.

Please write a compelling narrative with a clear beginning, middle, and end, ensuring each paragraph strictly represents its corresponding act."""
        
        return prompt
