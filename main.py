import dearpygui.dearpygui as dpg
from res.Cheats import *


def button_callback(sender, app_data):
    Runes(app_data)


dpg.create_context()
dpg.create_viewport(title='Elden Trainer', width=600, height=300)

with dpg.window(label="Example Window", width=600, height=300, no_resize=True, no_title_bar=True, no_move=True):
    dpg.add_input_int(label="Rune Value", default_value=0, callback=button_callback)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.create_context()
dpg.start_dearpygui()

dpg.destroy_context()
