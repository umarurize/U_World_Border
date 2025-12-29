import os
import json


def load_lang_data(lang_dir: str) -> dict:
    zh_CN_file_path = os.path.join(lang_dir, "zh_CN.json")
    en_US_file_path = os.path.join(lang_dir, "en_US.json")

    if not os.path.exists(zh_CN_file_path):
        with open(zh_CN_file_path, "w", encoding="utf-8") as f:
            zh_CN = {

            }
            json_str = json.dumps(zh_CN, indent=4, ensure_ascii=False)
            f.write(json_str)

    if not os.path.exists(en_US_file_path):
        with open(en_US_file_path, "w", encoding="utf-8") as f:
            en_US = {
                "message.error": "",
                "message.over_world_border": "You are not allowed to cross the world border...",

                "button.close": "Close",
                "button.back": "Back",
                "button.back_to_previous": "Back to previous",

                "main_form.title": "U-World-border - main form",
                "main_form.content": "Please select a function...",
                "main_form.button.world_border": "World Border",
                "main_form.button.reload_config": "Reload configurations",

                "world_border_form.title": "World Border",

                "reload_config_form.textinput1.placeholder": "Input a integer...",
                "reload_config_form.textinput2.placeholder": "Input a integer...",
                "reload_config_form.textinput3.placeholder": "Input a positive integer...",
                "reload_config_form.title": "Reload configurations",
                "reload_config_form.submit_button": "Reload",
                "reload_config.message.success": "Successfully reloaded configurations...",

                "overworld": "Overworld",
                "nether": "Nether",
                "theend": "The End",

                "enabled": "Enabled",
                "disabled": "Disabled",

                "center_pos": "Center position",
                "radius": "Radius",

            }
            json_str = json.dumps(en_US, indent=4, ensure_ascii=False)
            f.write(json_str)

    lang_data = {}

    for lang in os.listdir(lang_dir):
        lang_name = lang.strip(".json")

        lang_file_path = os.path.join(lang_dir, lang)

        with open(lang_file_path, "r", encoding="utf-8") as f:
            lang_data[lang_name] = json.loads(f.read())

    return lang_data
