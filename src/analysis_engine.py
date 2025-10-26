from typing import Dict, Any

class AnalysisEngine:
    """Parses the user's high-level text input to identify key entities.

    This engine is responsible for the initial interpretation of the user's
    creative intent.
    """

    def analyze_request(self, user_input: str) -> Dict[str, Any]:
        """Analyzes the raw user input string.

        This method performs a basic keyword analysis by splitting the string.

        Args:
            user_input (str): The raw user input string from the end-user.

        Returns:
            Dict[str, Any]: A structured dictionary representing the analyzed request.
        """
        words = user_input.split()
        subject = " ".join(words[0:2]) if len(words) > 1 else user_input
        action = " ".join(words[2:4]) if len(words) > 3 else ""
        scene = " ".join(words[4:]) if len(words) > 4 else ""
        return {"subject": subject, "action": action, "scene": scene}
