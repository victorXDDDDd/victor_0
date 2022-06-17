def on_button_pressed_a():
    basic.show_string("HOLA MUNDO")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global icono
    icono = randint(0, 2)
    if icono == 0:
        basic.show_icon(IconNames.CHESSBOARD)
    if icono == 1:
        basic.show_icon(IconNames.SCISSORS)
    if icono == 2:
        basic.show_icon(IconNames.SQUARE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_leds("""
        . # . # .
                # # # # #
                # # # # #
                . # # # .
                . . # . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

icono = 0
basic.show_number(9)
basic.pause(100)
basic.show_number(8)
basic.pause(100)
basic.show_number(7)
basic.pause(100)
basic.show_number(6)
basic.pause(100)
basic.show_number(4)
basic.pause(100)
basic.show_number(3)
basic.pause(100)
basic.show_number(2)
basic.pause(100)
basic.show_number(1)
music.set_volume(255)
music.play_melody("F A B - F A B - ", 186)
music.play_melody("F A B C5 B - - - ", 186)
music.play_melody("B C5 B G E - - - ", 186)
music.play_melody("D E G E - - - - ", 186)
basic.pause(100)
basic.show_number(5)

def on_forever():
    if input.pin_is_pressed(TouchPin.P0):
        basic.show_icon(IconNames.ASLEEP)
    else:
        if input.pin_is_pressed(TouchPin.P1):
            basic.show_icon(IconNames.SKULL)
        else:
            if input.pin_is_pressed(TouchPin.P2):
                basic.show_icon(IconNames.SKULL)
            else:
                pass
basic.forever(on_forever)

# hola xd