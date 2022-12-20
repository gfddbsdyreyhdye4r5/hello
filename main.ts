input.onButtonPressed(Button.A, function () {
    step += 1
    basic.pause(200)
    basic.showNumber(step)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 300, 200, 255, 199, 75, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
})
input.onGesture(Gesture.Shake, function () {
    step += 1
    basic.pause(200)
    basic.showNumber(step)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 300, 200, 255, 199, 75, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
})
let step = 0
step = 0
music.setBuiltInSpeakerEnabled(true)
input.setSoundThreshold(SoundThreshold.Loud, 150)
basic.forever(function () {
    if (input.logoIsPressed()) {
        basic.showString("reset")
        step = 0
    }
    if (input.buttonIsPressed(Button.B)) {
        step += -1
        basic.showNumber(step)
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 4042, 4041, 180, 48, 729, SoundExpressionEffect.Warble, InterpolationCurve.Curve), SoundExpressionPlayMode.UntilDone)
    }
})
