input.onButtonPressed(Button.A, function on_button_pressed_a() {
    JoyCar.drive(FRDirection.Forward, 50)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    JoyCar.stop(StopIntensity.Intense)
})
