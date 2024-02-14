import os
import subprocess
import json

def main():
    with open('config.json') as json_file:
        config_data = json.load(json_file)

    # Get the project name from the JSON data
    app_name = config_data.get('Config', {}).get('AppName', 'default_app')

    # Print the actual app name value
    print(app_name)

    scripts = {
        "1": {
            "name": "Run 'transformer.py'",
            "description": "Generate text using Cursed GPT",
            "file_name": "scripts/transformer.py"
        },
        "2": {
            "name": "Run 'transformer-t2s.py'",
            "description": "Run SynthiaGPT with text to speech",
            "file_name": "scripts/transformer_t2s.py"
        },
        "3": {
            "name": "Run 'transformer-s2t2s.py'",
            "description": "Run SynthiaGPT with speech to text to speech",
            "file_name": "scripts/transformer_s2t2s.py"
        },
        "4": {
            "name": "Run 'app.py'",
            "description": "Interact with SynthiaGPT using HTML and Flask",
            "file_name": "app.py"
        },
        "5": {
            "name": "Run 'transformer-webcam.py",
            "description": "Interact with SynthiaGPT using a webcam and mic",
            "file_name": "scripts/transformer_webcam.py"
        },
        "00": {
            "name": "Run 'Install Dependencies'",
            "description": "Install dependencies",
            "file_name": "scripts/install_dependencies.py"
        },
        "default": {
            "name": "Redirect to Main",
            "description": "Redirect to Main",
            "file_name": "redirect.py"
        }
    }

    current_script_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("\nAvailable Scripts:")
        for key, script_info in scripts.items():
            print(f"{key}: {script_info['name']} - {script_info['description']}")
        
        user_choice = input("Enter the number of the script you want to run (or 'q' to quit): ").strip()
        
        if user_choice == 'q':
            break
        
        if user_choice in scripts:
            selected_script = scripts[user_choice]
            script_file_name = selected_script["file_name"]
            script_file_path = os.path.join(current_script_dir, script_file_name)
            
            if os.path.exists(script_file_path):
                try:
                    subprocess.run(["python", script_file_path])
                except Exception as e:
                    print(f"An error occurred while running the script: {e}")
            else:
                print(f"Script file '{script_file_name}' does not exist.")
        else:
            print("Invalid choice. Please select a valid script number.")

if __name__ == "__main__":
    main()
