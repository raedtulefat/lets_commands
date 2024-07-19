import os
import sys

def lets_digest(arg):
    # Define the specific files and file patterns to search for based on the argument
    file_paths = {
        'docker': [
            'config/environments/production.rb',
            'config/environments/development.rb',
            '.dockerignore',
            'docker-compose.yml',
            'Dockerfile'
        ]
    }
    
    file_types = {
        'rails': ['*.js', '*.css', '*.scss', '*.rb', '*.erb'],
        'python': ['*.py']  # Corrected to ensure all types are in a single dictionary
    }
    
    output_file = 'output.txt'

    # Open the output file
    with open(output_file, 'w') as outfile:
        if arg == 'docker':
            # Handle specific file paths for docker
            for file_path in file_paths['docker']:
                # Check if the file exists
                if os.path.exists(file_path):
                    # Write the file header
                    outfile.write(f"\n\nFile: {file_path}\n")
                    # Write the file content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        outfile.write(f.read())
                else:
                    print(f"File not found: {file_path}")
        elif arg in file_types:
            # Handle file patterns for rails and python
            extensions = file_types[arg]
            # Walk through the directory
            for root, dirs, files in os.walk('.'):
                for file in files:
                    # Check if the file matches any of the specified extensions
                    if any(file.endswith(ext.replace('*', '')) for ext in extensions):
                        file_path = os.path.join(root, file)
                        # Write the file header
                        outfile.write(f"\n\nFile: {file_path}\n")
                        # Write the file content
                        with open(file_path, 'r', encoding='utf-8') as f:
                            outfile.write(f.read())
        else:
            print(f"No configuration for argument: {arg}")
            print("Usage: lets-digest [docker|rails|python]")

def main():
    if len(sys.argv) > 1:
        lets_digest(sys.argv[1])
    else:
        print("Usage: lets-digest [docker|rails|python]")

if __name__ == "__main__":
    main()
