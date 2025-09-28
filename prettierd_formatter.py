import sublime
import shutil
import subprocess
import os
import sys

from .utils import get_setting

def get_prettierd_path(view_or_window):
    settings_path = get_setting(view_or_window, "prettierd_path", "")
    if settings_path:
        return settings_path

    # Default behavior when not specified
    default_path = shutil.which("prettierd")
    if default_path:
        return default_path

    sublime.error_message("prettierd executable not found.")
    return None

def format_with_prettierd(view_or_window, content, file_path):
    prettierd_path = get_prettierd_path(view_or_window)
    if not prettierd_path:
        message = "prettierd path not found."
        print(message)
        sublime.error_message(message)
        return None

    cmd = [prettierd_path, file_path]

    env = os.environ.copy()
    # Force disable colored output.
    # See: https://github.com/fsouza/prettierd/issues/790
    env['NO_COLOR'] = '1'

    try:
        if sys.platform == 'win32':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        else:
            startupinfo = None
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, cwd=os.path.dirname(file_path),
                                   startupinfo=startupinfo, env=env)
        formatted_code, error = process.communicate(input=content.encode('utf-8'))
    except Exception as e:
        sublime.error_message("Failed to execute prettierd: " + str(e))
        return None

    if process.returncode == 0:
        return formatted_code.decode('utf-8')
    else:
        error_message = error.decode('utf-8')
        if not error_message:
            error_message = formatted_code.decode('utf-8')
        if not error_message:
            error_message = "Unknown error"
        print(error_message)
        sublime.error_message("Error formatting the file with prettierd: " + error_message)
        return None
