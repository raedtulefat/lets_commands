GPT: https://chatgpt.com/c/eece4d79-b0bf-4ba9-8872-5edb5265f65f

# Lets-commands

`lets-commands` is a collection of command-line tools designed to facilitate various daily tasks for developers. This package currently includes the `lets-digest` command, which aggregates contents of specific types of files into a single file for easy review.

## Features

- **lets-digest**: Aggregates and outputs the contents of specified file types into a single file. Supported arguments include `docker`, `rails`, and `python`, each handling a distinct set of file patterns.

## Installation

Follow these steps to install `lets-commands` on any machine:

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Step-by-step Installation

1. Clone the repository or download the source code:

   ```bash
   git clone https://your-repository-url/lets_commands.git
   cd lets_commands
   ```

2. Install the package using pip:

   ```bash
   pip install .
   ```

   Alternatively, if you do not have write permissions to the Python site-packages directory, you can install locally using:

   ```bash
   pip install . --user
   ```

### Verifying Installation

After installation, you can verify that the package is installed correctly by checking the availability of the `lets-digest` command:

````bash
which lets-digest

## Adding New Commands

To add new commands to the `lets-commands` package, follow the structured approach below. We'll use the addition of a new command `lets-hello` as an example, which simply prints "Hello World" when executed.

### Step 1: Create Command Script

1. Navigate to the `lets_commands` directory.
2. Create a new subdirectory for your command if it does not already exist. For our example, if you are adding `lets-hello`, create a directory named `lets_hello`:
    ```bash
    mkdir lets_hello
    ```
3. Inside the `lets_hello` directory, create a Python script `hello.py`:
    ```bash
    touch lets_hello/hello.py
    ```
4. Edit `hello.py` to include the following Python code:
    ```python
    def main():
        print("Hello World")

    if __name__ == "__main__":
        main()
    ```

### Step 2: Update Package Setup

1. Open `setup.py` located in the root directory of your package.
2. Add an entry point for the new command in the `entry_points` section of the `setup()` function. This tells `setuptools` how to create an executable command that points to your function. For the `lets-hello` command, add:
    ```python
    entry_points={
        'console_scripts': [
            'lets-digest=lets_digest.digest:main',
            'lets-hello=lets_hello.hello:main'  # Add this line
        ]
    },
    ```

### Step 3: Install the Updated Package

After updating `setup.py`, you need to reinstall the package to reflect the changes:
```bash
pip install . --upgrade
````
