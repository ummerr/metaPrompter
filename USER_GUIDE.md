# User Guide: From Idea to Veo Prompt

Welcome to the Veo-3 Meta-Framework application! This guide will walk you through turning a simple creative idea into a detailed, professional prompt ready for a video generation model.

## How It Works

This tool takes your basic idea and, using a structured process, enriches it to create a comprehensive prompt. It thinks about different aspects of the scene, the characters, and the technical details for you.

## Step-by-Step Example

Let's start with a simple idea: **"a happy robot walking through a sunlit forest"**.

### 1. Running the Application

To process this idea, you would run the application (as shown in the main `README.md`). The tool takes your idea as input.

### 2. The Generated Prompt

The application will then output a structured prompt, like this:

```json
{
  "subject": "A generic subject",
  "action": "A generic action",
  "scene": "A generic scene",
  "style": "cinematic",
  "dialogue": "",
  "sounds": "",
  "technical": [
    "1080p"
  ],
  "negative_prompt": "low quality, blurry, jpeg artifacts"
}
```
*(Note: The output above is from the current placeholder implementation. A full implementation would generate a prompt more specific to the input idea.)*

### 3. Understanding the Output

The generated prompt is broken down into 7 key components. Here’s what each one means:

*   **`subject`**: Who or what is the main focus of the video? In our example, this would be "a happy robot".
*   **`action`**: What is the subject doing? Here, the action is "walking through a sunlit forest".
*   **`scene`**: What does the environment look like? This would be a more detailed description, like "A lush, green forest with tall trees, with rays of sunlight filtering through the leaves."
*   **`style`**: What is the artistic look and feel of the video? This could be "cinematic," "photorealistic," "anime," "documentary," etc.
*   **`dialogue`**: Is anyone speaking? If so, what are they saying?
*   **`sounds`**: What are the background sounds or music? For our example, this might be "birds chirping, leaves rustling under the robot's feet."
*   **`technical`**: This includes technical details for the video generation, like the desired resolution (`1080p`, `4K`) or aspect ratio (`16:9`).

The final field, **`negative_prompt`**, is also important. It tells the video model what to *avoid*, helping to prevent common issues like "blurry" or "low quality" results.

By breaking down a simple idea into this structured format, the tool helps you create a much more detailed and effective prompt, leading to a higher quality video output.
