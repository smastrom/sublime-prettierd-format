import sublime

def get_setting(view_or_window, setting_name, default_value):
    if view_or_window is not None:
        local_settings = view_or_window.settings().get("PrettierdFormat", {})
        if setting_name in local_settings:
            return local_settings[setting_name]

    return sublime.load_settings("prettierd_format.sublime-settings").get(setting_name, default_value)
