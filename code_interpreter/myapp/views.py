# file_reader/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .utils import read_pdf, read_xlsx, read_csv, read_docx
from .gpt3 import generate_code
from .executor import restricted_exec
import os
from code_interpreter import settings

def handle_uploaded_file(f, file_type):
    file_path = os.path.join(settings.MEDIA_ROOT, f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    if file_type == 'pdf':
        return read_pdf(file_path)
    elif file_type == 'xlsx':
        return read_xlsx(file_path)
    elif file_type == 'csv':
        return read_csv(file_path)
    elif file_type == 'docx':
        return read_docx(file_path)
    else:
        return "Unsupported file format"

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         file = request.FILES['file']
#         file_type = file.name.split('.')[-1].lower()
#         content = handle_uploaded_file(file, file_type)
        
#         return render(request, 'upload.html', {'content': content})
#     return render(request, 'upload.html')

def generate_and_execute_code(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_type = file.name.split('.')[-1].lower()
        content = handle_uploaded_file(file, file_type)
        
        user_prompt = request.POST.get('prompt')
        structured_prompt = f"Based on the following content from the file:\n\n{content}\n\nAnd the user's prompt:\n\n{user_prompt}\n\nGenerate Python code to accomplish the task."
        
        generated_code = generate_code(structured_prompt)
        
        execution_result, stdout_output = restricted_exec(generated_code)
        
        return render(request, 'generate_code.html', {
            'generated_code': generated_code, 
             
            'stdout_output': stdout_output
        })
    return render(request, 'generate_code.html')