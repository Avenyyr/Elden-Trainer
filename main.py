import dearpygui.dearpygui as dpg
from res.GetPtrAddr import *


def update_text(sender, app_data):
    rune_value = pm.read_int(GetPtrAddr(gameModule + 0x03CF1558, [0x28, 0x0, 0x30, 0x6C]))
    dpg.set_value("widget_information_text", f"Rune Value: {rune_value}")


def runes(sender, app_data):
    pm.write_int(GetPtrAddr(gameModule + 0x03CF1558, [0x28, 0x0, 0x30, 0x6C]), app_data)
    update_text(sender, app_data)


dpg.create_context()
dpg.create_viewport(title='Elden Trainer', width=600, height=300, always_on_top=True)

with dpg.window(label="Example Window", width=600, height=300, no_resize=True, no_title_bar=True, no_move=True):
    with dpg.tab_bar():

        with dpg.tab(label="Cheats"):
            dpg.add_input_int(label="Rune Value", default_value=0, callback=runes)

        with dpg.tab(label="Informations"):
            dpg.add_text("Rune Value: 0", tag="widget_information_text")
            dpg.add_button(label="Refresh", callback=update_text)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.create_context()
dpg.start_dearpygui()

dpg.destroy_context()
