import os
import subprocess
import sys

def main():
    print("CursedGPT")

    scripts = {
        "1": {
            "name": "Run Cursed GPT",
            "description": "Generate text using Cursed GPT",
            "file_name": "scripts/transformer.py"
        },
        "2": {
            "name": "Run Cursed GPT Text-to-Speech",
            "description": "Run Cursed GPT with text to speech",
            "file_name": "scripts/transformer-t2s.py"
        },
        "3": {
            "name": "Run Cursed GPT Flask Server",
            "description": "Interact with Cursed GPT using HTML and Flask",
            "file_name": "app.py"
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
        
        if user_choice.lower() == 'q':
            sys.exit()

        if user_choice in scripts:
            selected_script = scripts[user_choice]
            script_file_name = selected_script["file_name"]
            script_file_path = os.path.join(current_script_dir, script_file_name)
            
            if os.path.exists(script_file_path):
                try:
                    subprocess.Popen(["python", script_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
                except subprocess.CalledProcessError as e:
                    print(f"An error occurred while running the script: {e}")
            else:
                print(f"Script file '{script_file_name}' does not exist.")
        else:
            print("Invalid choice. Please select a valid script number.")

if __name__ == "__main__":
    main()
