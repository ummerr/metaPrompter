from typing import List, Dict, Any

class KnowledgeBase:
    """Loads and provides access to Veo 3 technical specifications.

    This class is implemented as a singleton to ensure a single, consistent
    source of truth for technical data throughout the application.
    """
import json
import os

class KnowledgeBase:
    """Loads and provides access to Veo 3 technical specifications."""
    _instance = None
    _specs: Dict[str, Any]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(KnowledgeBase, cls).__new__(cls)
            config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
            with open(config_path, 'r') as f:
                cls._instance._specs = json.load(f)
        return cls._instance

    def get_max_duration(self) -> int:
        """Returns the maximum video duration in seconds.

        Returns:
            int: The maximum duration in seconds.
        """
        return self._specs["max_duration_seconds"]

    def get_supported_resolutions(self) -> List[str]:
        """Returns a list of supported video resolutions.

        Returns:
            List[str]: A list of supported resolutions.
        """
        return self._specs["resolutions"]
