def on_button_pressed_a():
    for index in range(2):
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.show_arrow(ArrowNames.SOUTH)
        basic.show_arrow(ArrowNames.SOUTH_WEST)
        basic.show_arrow(ArrowNames.WEST)
        basic.show_arrow(ArrowNames.NORTH_WEST)
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_string("Target received, engage ready")
        radio.set_transmit_power(7)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for index2 in range(2):
        basic.show_arrow(ArrowNames.NORTH_WEST)
        basic.show_arrow(ArrowNames.WEST)
        basic.show_arrow(ArrowNames.SOUTH_WEST)
        basic.show_arrow(ArrowNames.SOUTH)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    pass
radio.on_received_value(on_received_value)

basic.show_arrow(ArrowNames.NORTH)