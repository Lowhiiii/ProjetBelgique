def on_button_pressed_a():
    JoyCar.drive(FRDirection.FORWARD, 50)
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    JoyCar.stop(StopIntensity.INTENSE)
input.on_button_pressed(Button.B, on_button_pressed_b)