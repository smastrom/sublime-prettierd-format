import sublime
import shutil
import subprocess
import os

def get_prettierd_path():
    settings = sublime.load_settings("Prettierd.sublime-settings")
    
    settings_path = settings.get("prettierd_path", "")
    if settings_path:
        return settings_path

    # Default behavior when not specified
    default_path = shutil.which("prettierd")
    if default_path:
        return default_path

    sublime.error_message("prettierd executable not found.")
    return None

def format_with_prettierd(content, file_path):
    prettierd_path = get_prettierd_path()
    if not prettierd_path:
        message = "prettierd path not found."
        print(message)
        sublime.error_message(message)
        return None

    cmd = [prettierd_path, "--stdin-filepath", file_path]
    
    try:
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=os.path.dirname(file_path))
        formatted_code, error = process.communicate(input=content.encode('utf-8'))
    except Exception as e:
        sublime.error_message("Failed to execute prettierd: " + str(e))
        return None

    if process.returncode == 0:
        return formatted_code.decode('utf-8')
    else:
        error_message = error.decode('utf-8') if error.decode('utf-8') else "Unknown error"
        print(error_message)
        sublime.error_message("Error formatting the file with prettierd: " + error_message)
        return None