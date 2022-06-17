input.onButtonPressed(Button.A, function () {
    basic.showString("HOLA MUNDO")
})
input.onGesture(Gesture.Shake, function () {
    icono = randint(0, 2)
    if (icono == 0) {
        basic.showIcon(IconNames.Chessboard)
    }
    if (icono == 1) {
        basic.showIcon(IconNames.Scissors)
    }
    if (icono == 2) {
        basic.showIcon(IconNames.Square)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        `)
})
let icono = 0
basic.showNumber(9)
basic.pause(100)
basic.showNumber(8)
basic.pause(100)
basic.showNumber(7)
basic.pause(100)
basic.showNumber(6)
basic.pause(100)
basic.showNumber(4)
basic.pause(100)
basic.showNumber(3)
basic.pause(100)
basic.showNumber(2)
basic.pause(100)
basic.showNumber(1)
music.setVolume(255)
music.playMelody("F A B - F A B - ", 186)
music.playMelody("F A B C5 B - - - ", 186)
music.playMelody("B C5 B G E - - - ", 186)
music.playMelody("D E G E - - - - ", 186)
basic.pause(100)
basic.showNumber(5)
basic.forever(function () {
    if (input.pinIsPressed(TouchPin.P0)) {
        basic.showIcon(IconNames.Asleep)
    } else if (input.pinIsPressed(TouchPin.P1)) {
        basic.showIcon(IconNames.Skull)
    } else if (input.pinIsPressed(TouchPin.P2)) {
        basic.showIcon(IconNames.Skull)
    } else {
    	
    }
})
