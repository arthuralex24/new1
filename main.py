def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
