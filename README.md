# BT_Task
Automation Task with Selenium

## Step 1: Set up a Virtual Environment Using the Requirements File

Begin by creating a virtual environment to isolate the project dependencies. You can achieve this by running the following command:

```bash
pip install -r requirements.txt
```

This command installs all the necessary packages specified in the `requirements.txt` file, ensuring a clean and controlled environment for your project.

## Step 2: Create an Environment File (e.g., example_env) to Securely Store Sensitive Variables

It's crucial to protect sensitive information, such as API keys or passwords. To do this, create an environment file (commonly named `.env` or something similar) where you can store these secret variables. Ensure that this file is included in your project's `.gitignore` to prevent it from being exposed in version control.

## Step 3: Activate the Python Package Library

Activate the virtual environment you created earlier. This step ensures that your Python script will use the isolated environment with the specified dependencies. The activation command typically varies depending on your operating system.

For Windows:
```bash
venv\Scripts\activate
```

For macOS and Linux:
```bash
source venv/bin/activate
```

## Step 4: Run the Script

With your virtual environment activated and secret variables securely stored in the environment file, you are ready to execute your Selenium automation script. Launch the script to perform the desired automation tasks.

These steps provide a structured approach to setting up your Selenium automation project, ensuring proper isolation of dependencies, security for sensitive data, and successful script execution.
