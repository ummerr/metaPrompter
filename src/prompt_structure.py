from pydantic import BaseModel, Field
from typing import List

class VeoPrompt(BaseModel):
    """Defines the validated data structure for the final Veo 3 prompt output.

    This class uses pydantic for data validation to ensure that all generated
    prompts conform to the required 7-component format.
    """
    subject: str = Field(description="The primary subject of the scene.")
    action: str = Field(description="The action being performed by the subject.")
    scene: str = Field(description="The description of the scene and environment.")
    style: str = Field(description="The artistic or cinematic style of the video.")
    dialogue: str = Field(description="Any dialogue spoken in the scene.")
    sounds: str = Field(description="Description of background sounds or music.")
    technical: List[str] = Field(description="Technical specifications like resolution or aspect ratio.")
    negative_prompt: str = Field(description="Elements to exclude from the generation.", default="")
