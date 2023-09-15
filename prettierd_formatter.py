import subprocess
import sublime

def format_with_prettierd(file_path):
    # Read the file content using Python
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()

    cmd = ["prettierd", file_path]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    formatted_code, error = process.communicate(input=file_content.encode('utf-8'))

    if process.returncode == 0:
        return formatted_code.decode('utf-8')
    else:
        sublime.error_message("Error formatting the file with prettierd.")
        return None
