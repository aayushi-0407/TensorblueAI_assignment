# File Interpreter with Code Generation and Execution

This Django project allows users to upload files in various formats (PDF, XLSX, CSV, DOCX), reads the content from these files, generates Python code based on the content and a user prompt using Anthropic's Claude API, and securely executes the generated code. The result of the execution is then displayed to the user.

## Features

- **File Upload**: Upload PDF, XLSX, CSV, or DOCX files.
- **Content Reading**: Extract content from the uploaded files.
- **Code Generation**: Generate Python code using Anthropic's Claude API based on the extracted content and user prompt.
- **Code Execution**: Securely execute the generated Python code and display the result.
- **User Interface**: Simple web interface for file upload and prompt submission.

## Prerequisites

- Python 3.6+
- Django 3.2+
- Anthropic API key
- The following Python packages:
  - `django`
  - `anthropic`
  - `PyPDF2`
  - `openpyxl`
  - `pandas`
  - `python-docx`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Django project:

    ```bash
    python manage.py migrate
    ```

5. Add your Anthropic API key to the Django settings:

    ```python
    # settings.py

    # Other settings...

    ANTHROPIC_API_KEY = 'your_valid_anthropic_api_key'
    ```

6. Create the necessary directories for file uploads:

    ```bash
    mkdir -p media/uploads
    ```

7. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and navigate to:

    - File upload and prompt submission: `http://127.0.0.1:8000/myapp/generate_code/`
    

## Project Structure

- `myapp/`
  - `views.py`: Contains the view functions for handling file uploads and code generation.
  - `utils.py`: Contains utility functions for reading content from various file formats.
  - `gpt3.py`: Contains the function for generating code using Anthropic's Claude API.
  - `executor.py`: Contains the function for securely executing the generated code.
  - `templates/`
    - `myapp/`
     
      - `generate_code.html`: Template for upload,  code generation and execution.

## Usage


 **Generate and Execute Code**:
    - Go to `http://127.0.0.1:8000/myapp/generate_code/`
    - Upload a file.
    - Enter a prompt describing what you want to achieve with the content of the file.
    - Submit the form to generate and execute the code.
    - View the generated code, execution result, and any standard output.





