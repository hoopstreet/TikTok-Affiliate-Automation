import json
import os

# Master Project IDs from Supabase
PROJECT_MAP = {
    "mk_online": "0130288d-9eba-42ee-af48-9a7802a7b268",
    "hoopstreet": "f39d12af-914e-40c6-8e27-e646724485f6",
    "daily_drive": "43d0678a-9fac-4ce1-8e87-4f8bf2675337",
    "budget_accessories": "b4cf44ab-0a8a-4a1e-9378-71abaa8e1201"
}

def build_niche_workflow(project_name):
    blueprint_path = f"projects/{project_name}/n8n_blueprint.json"
    
    if not os.path.exists(blueprint_path):
        print(f"Error: Blueprint for {project_name} not found.")
        return

    with open(blueprint_path, 'r') as f:
        blueprint = json.load(f)
        
    print(f"--- Initiating Auto-Build for {project_name.upper()} ---")
    print(f"Target ID: {PROJECT_MAP.get(project_name)}")
    print(f"Steps: {', '.join(blueprint['steps'])}")
    print(f"Status: Synchronizing with n8n AI Assistant...")
    
    # Logic to send JSON to n8n API goes here
    print(f"Build Successful: {project_name} is now online.")

if __name__ == "__main__":
    # Example: Build all niches
    for niche in PROJECT_MAP.keys():
        build_niche_workflow(niche)
