# file_reader/executor.py

import builtins
import io
import sys

def restricted_exec(code, globals_dict=None):
    safe_builtins = {
        'print': print,
        'range': range,
        'len': len,
        'int': int,
        'float': float,
        'str': str,
        'list': list,
        'dict': dict,
        'set': set,
        'tuple': tuple,
        'bool': bool,
        'True': True,
        'False': False,
        'None': None,
    }

    if globals_dict is None:
        globals_dict = {}

    globals_dict['__builtins__'] = safe_builtins

    # Capture standard output
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        exec(code, globals_dict)
        output = new_stdout.getvalue()
    except Exception as e:
        output = str(e)
    finally:
        sys.stdout = old_stdout

    return globals_dict.get('result', 'Code executed successfully.'), output
