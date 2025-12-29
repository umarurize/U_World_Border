import os
import math
import json

from endstone import Player, ColorFormat

from endstone.plugin import Plugin
from endstone.command import Command, CommandSender
from endstone.form import ActionForm, ModalForm, TextInput, Toggle
from endstone.event import event_handler, PlayerMoveEvent

from endstone_u_world_border.lang import load_lang_data


current_dir = os.getcwd()

first_dir = os.path.join(current_dir, "plugins", "u-world-border")

if not os.path.exists(first_dir):
    os.mkdir(first_dir)

config_data_file_path = os.path.join(first_dir, "config.json")

lang_dir = os.path.join(first_dir, "lang")

if not os.path.exists(lang_dir):
    os.mkdir(lang_dir)


class u_world_border(Plugin):
    api_version = "0.10"

    def __init__(self):
        super().__init__()

        # load data: config.json
        if not os.path.exists(config_data_file_path):
            with open(config_data_file_path, "w") as f:
                config_data = {
                    "overworld": {
                        "is_enabled": False,
                        "center_pos": [0, 0],
                        "radius": 10000
                    },
                    "nether": {
                        "is_enabled": False,
                        "center_pos": [0, 0],
                        "radius": 10000
                    },
                    "theend": {
                        "is_enabled": False,
                        "center_pos": [0, 0],
                        "radius": 10000
                    }
                }
                json_str = json.dumps(config_data, indent=4, ensure_ascii=False)
                f.write(json_str)
        else:
            with open(config_data_file_path, "r") as f:
                config_data = json.loads(f.read())

        self.config_data = config_data

        # load data: lang
        self.lang_data = load_lang_data(lang_dir)

    def on_enable(self):
        self.register_events(self)

        self.logger.info(
            f"{ColorFormat.YELLOW}"
            f"U-World-Border is enabled..."
        )

    commands = {
        "ubd": {
            "description": "Call out the main form of U-World-Border...",
            "usages": ["/ubd"],
            "permissions": ["u_world_border.command.ubd"]
        }
    }

    permissions = {
        "u_world_border.command.ubd": {
            "description": "Call out the main form of U-World-Border...",
            "default": True
        }
    }

    def on_command(self, sender: CommandSender, command: Command, args: list[str]):
        if command.name == "ubd":
            if not isinstance(sender, Player):
                sender.send_message(
                    f"{ColorFormat.RED}"
                    f"This command can only be executed by a player..."
                )

                return

            main_form = ActionForm(
                title=f"{ColorFormat.BOLD}{ColorFormat.LIGHT_PURPLE}"
                      f"{self.get_text(sender, 'main_form.title')}",
                content=f"{ColorFormat.GREEN}"
                        f"{self.get_text(sender, 'main_form.content')}"
            )

            main_form.add_button(
                f"{ColorFormat.YELLOW}"
                f"{self.get_text(sender, 'main_form.button.world_border')}",
                icon="textures/ui/worldsIcon",
                on_click=self.world_border
            )

            if sender.is_op:
                main_form.add_button(
                    f"{ColorFormat.YELLOW}"
                    f"{self.get_text(sender, 'main_form.button.reload_config')}",
                    icon="textures/ui/icon_setting",
                    on_click=self.reload_configuration
                )

            if self.server.plugin_manager.get_plugin("zx_ui") is None:
                main_form.on_close = None

                main_form.add_button(
                    f"{ColorFormat.YELLOW}"
                    f"{self.get_text(sender, 'button.close')}",
                    icon="textures/ui/cancel",
                    on_click=None
                )
            else:
                main_form.on_close = self.back_to_zx_ui

                main_form.add_button(
                    f"{ColorFormat.YELLOW}"
                    f"{self.get_text(sender, 'button.back')}",
                    icon="textures/ui/refresh_light",
                    on_click=self.back_to_zx_ui
                )
            sender.send_form(main_form)

    def world_border(self, player: Player):
        content = ""

        for key, value in self.config_data.items():
            content += (
                f"{ColorFormat.GREEN}"
                f"[{self.get_text(player, key)}]\n"
            )

            if value["is_enabled"]:
                content += (
                    f"{self.get_text(player, 'enabled')}\n"
                )
            else:
                content += (
                    f"{ColorFormat.RED}"
                    f"{self.get_text(player, 'disabled')}\n"
                )

            center_pos = value["center_pos"]

            content += (
                f"{ColorFormat.GREEN}"
                f"{self.get_text(player, 'center_pos')}: "
                f"{ColorFormat.WHITE}"
                f"[{center_pos[0]}, ~, {center_pos[1]}]\n"
            )

            radius = value["radius"]

            content += (
                f"{ColorFormat.GREEN}"
                f"{self.get_text(player, 'radius')}: "
                f"{ColorFormat.WHITE}"
                f"{radius}\n"
                f"\n"
            )

        world_border_form = ActionForm(
            title=f"{ColorFormat.BOLD}{ColorFormat.LIGHT_PURPLE}"
                  f"{self.get_text(player, 'world_border_form.title')}",
            content=content,
            on_close=self.back_to_main_form
        )

        world_border_form.add_button(
            f"{ColorFormat.YELLOW}"
            f"{self.get_text(player, 'button.back_to_previous')}",
            icon="textures/ui/refresh_light",
            on_click=self.back_to_main_form
        )

        player.send_form(world_border_form)

    def reload_configuration(self, player: Player):
        controls_list = []

        for key, value in self.config_data.items():
            toggle = Toggle(
                label=f"{ColorFormat.GREEN}"
                      f"{self.get_text(player, key)}"
            )

            if value["is_enabled"]:
                toggle.default_value = True
            else:
                toggle.default_value = False

            controls_list.append(toggle)

            center_pos = value["center_pos"]

            textinput1 = TextInput(
                label=f"{ColorFormat.GREEN}"
                      f"{self.get_text(player, 'center_pos')} X",
                placeholder=self.get_text(player, "reload_config_form.textinput1.placeholder"),
                default_value=f"{center_pos[0]}"
            )

            controls_list.append(textinput1)

            textinput2 = TextInput(
                label=f"{ColorFormat.GREEN}"
                      f"{self.get_text(player, 'center_pos')} Z",
                placeholder=self.get_text(player, "reload_config_form.textinput2.placeholder"),
                default_value=f"{center_pos[1]}"
            )

            controls_list.append(textinput2)

            radius = value["radius"]

            textinput3 = TextInput(
                label=f"{ColorFormat.GREEN}"
                      f"{self.get_text(player, 'radius')}",
                placeholder=self.get_text(player, "reload_config_form.textinput3.placeholder"),
                default_value=f"{radius}"
            )

            controls_list.append(textinput3)

        reload_config_form = ModalForm(
            title=f"{ColorFormat.BOLD}{ColorFormat.LIGHT_PURPLE}"
                  f"{self.get_text(player, 'reload_config_form.title')}",
            controls=controls_list,
            submit_button=f"{ColorFormat.YELLOW}"
                          f"{self.get_text(player, 'reload_config_form.submit_button')}",
            on_close=self.back_to_main_form
        )

        def on_submit(p: Player, json_str: str):
            data = json.loads(json_str)

            try:
                overworld_center_pos_x = int(data[1])
                overworld_center_pos_z = int(data[2])
                overworld_radius = int(data[3])

                nether_center_pos_x = int(data[5])
                nether_center_pos_z = int(data[6])
                nether_radius = int(data[7])

                theend_center_pos_x = int(data[9])
                theend_center_pos_z = int(data[10])
                theend_radius = int(data[11])
            except:
                p.send_message(
                    f"{ColorFormat.RED}"
                    f"{self.get_text(p, 'message.error')}"
                )

                return

            if (
                overworld_radius <= 0
                or
                nether_radius <= 0
                or
                theend_radius <= 0
            ):
                p.send_message(
                    f"{ColorFormat.RED}"
                    f"{self.get_text(p, 'message.error')}"
                )

                return

            self.config_data["overworld"]["is_enabled"] = data[0]
            self.config_data["overworld"]["center_pos"] = [
                overworld_center_pos_x,
                overworld_center_pos_z
            ]
            self.config_data["overworld"]["radius"] = overworld_radius

            self.config_data["nether"]["is_enabled"] = data[4]
            self.config_data["nether"]["center_pos"] = [
                nether_center_pos_x,
                nether_center_pos_z
            ]
            self.config_data["nether"]["radius"] = nether_radius

            self.config_data["theend"]["is_enabled"] = data[8]
            self.config_data["theend"]["center_pos"] = [
                theend_center_pos_x,
                theend_center_pos_z
            ]
            self.config_data["theend"]["radius"] = theend_radius

            self.save_config_data()

            p.send_message(
                f"{ColorFormat.YELLOW}"
                f"{self.get_text(p, 'reload_config.message.success')}"
            )

        reload_config_form.on_submit = on_submit

        player.send_form(reload_config_form)

    @event_handler
    def on_player_move(self, e: PlayerMoveEvent):
        dimension = e.player.dimension.name.lower()

        if self.config_data[dimension]["is_enabled"]:
            center_pos = self.config_data[dimension]["center_pos"]

            radius = self.config_data[dimension]["radius"]

            to_pos = [
                math.floor(e.to_location.x),
                math.floor(e.to_location.z)
            ]

            distance = math.floor(((center_pos[0]-to_pos[0])**2 + (center_pos[1]-to_pos[1])**2)**0.5)

            if distance > radius:
                e.cancel()

                e.player.send_message(
                    f"{ColorFormat.RED}"
                    f"{self.get_text(e.player, 'message.over_world_border')}"
                )

    def save_config_data(self):
        with open(config_data_file_path, "w+") as f:
            json_str = json.dumps(self.config_data, indent=4, ensure_ascii=False)
            f.write(json_str)

    def back_to_zx_ui(self, player: Player):
        player.perform_command("cd")

    def back_to_main_form(self, player: Player):
        player.perform_command("ubd")

    def get_text(self, player: Player, text_key: str) -> str:
        player_lang = player.locale

        try:
            if self.lang_data.get(player_lang) is None:
                text_value = self.lang_data["en_US"][text_key]
            else:
                if self.lang_data[player_lang].get(text_key) is None:
                    text_value = self.lang_data["en_US"][text_key]
                else:
                    text_value = self.lang_data[player_lang][text_key]

            return text_value
        except Exception as e:
            self.logger.error(
                f"{ColorFormat.RED}"
                f"{e}"
            )

            return text_key



