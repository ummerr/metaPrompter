class Identity:
    """Defines the core identity and purpose of the metaprompting framework."""

    def __init__(self):
        self._name = "Veo-3 Meta-Framework"
        self._version = "0.1.0"
        self._description = "A framework for generating high-quality prompts for the Veo 3 model."

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def description(self) -> str:
        return self._description
