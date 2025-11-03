from pydantic import BaseModel, Field
from typing import List

class Scene(BaseModel):
    """Represents a single scene within a larger narrative."""
    subject: str = Field(description="The primary subject of the scene.")
    action: str = Field(description="The action being performed by the subject.")
    scene: str = Field(description="The description of the scene and environment.")
    composition: str = Field(description="Description of the camera composition and relative spacing.")
    consistent_universe: str = Field(description="Descriptive tags that define the core visual style of the world.")

class VeoPrompt(BaseModel):
    """Defines the validated data structure for the final Veo 3 prompt output.

    This class uses pydantic for data validation to ensure that all generated
    prompts conform to the required 7-component format and can support multiple scenes.
    """
    scenes: List[Scene] = Field(description="A list of scenes that make up the video.")
    style: str = Field(description="The artistic or cinematic style of the video.")
    dialogue: str = Field(description="Any dialogue spoken in the scene.")
    sounds: str = Field(description="Description of background sounds or music.")
    technical: List[str] = Field(description="Technical specifications like resolution or aspect ratio.")
    negative_prompt: str = Field(description="Elements to exclude from the generation.", default="low quality, blurry, jpeg artifacts")
