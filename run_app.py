# run_app.py
from src.main import CoreOrchestrator

# 1. Initialize the main orchestrator
orchestrator = CoreOrchestrator()

# 2. Define your high-level idea
user_idea = "A futuristic detective exploring a rainy, neon-lit city."

# 3. Process the idea to generate the final prompt
final_prompt = orchestrator.process_request(user_idea)

# 4. Print the structured output
print("Generated VeoPrompt:")
print(final_prompt.model_dump_json(indent=2))
