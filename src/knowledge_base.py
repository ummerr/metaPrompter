from typing import List, Dict, Any

class KnowledgeBase:
    """Loads and provides access to Veo 3 technical specifications.

    This class is implemented as a singleton to ensure a single, consistent
    source of truth for technical data throughout the application.
    """
    _instance = None
    _specs: Dict[str, Any]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(KnowledgeBase, cls).__new__(cls)
            # In a real implementation, this would load from a configuration file.
            cls._instance._specs = {
                "max_duration_seconds": 120,
                "resolutions": ["1080p", "4K", "8K"],
                "aspect_ratios": ["16:9", "1:1", "9:16", "4:3"],
                "max_dialogue_chars": 500
            }
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
