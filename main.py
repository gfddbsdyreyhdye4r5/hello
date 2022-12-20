def on_gesture_shake():
    global step
    step += 1
    basic.pause(200)
    basic.show_number(step)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
            300,
            200,
            255,
            199,
            75,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

step = 0
step = 0
music.set_built_in_speaker_enabled(True)
input.set_sound_threshold(SoundThreshold.LOUD, 150)

def on_forever():
    def on_button_pressed_a():
        basic.show_string("Pls Subscribe!")
    input.on_button_pressed(Button.A, on_button_pressed_a)

    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    basic.pause(200)
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    basic.pause(200)
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    basic.pause(200)
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    music.play_tone(415, music.beat(BeatFraction.QUARTER))
    music.play_tone(370, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    music.play_tone(415, music.beat(BeatFraction.QUARTER))
    music.play_tone(370, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    basic.pause(200)
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    basic.pause(200)
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    basic.pause(200)
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    music.play_tone(415, music.beat(BeatFraction.QUARTER))
    music.play_tone(370, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    basic.pause(100)
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    basic.pause(200)
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    basic.pause(500)
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    basic.pause(200)
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.WHOLE))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    basic.pause(200)
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    basic.pause(200)
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    basic.pause(200)
    music.play_tone(277, music.beat(BeatFraction.DOUBLE))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    basic.pause(200)
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    basic.pause(200)
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    basic.pause(200)
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.DOUBLE))
    basic.pause(200)
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    basic.pause(200)
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.DOUBLE))

    def on_forever():
        pass
    basic.forever(on_forever)

    global step
    if input.logo_is_pressed() and step > 100:
        basic.show_string("reset")
        step = 0
    if input.button_is_pressed(Button.A):
        music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
                4042,
                4041,
                180,
                48,
                729,
                SoundExpressionEffect.WARBLE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.UNTIL_DONE)
basic.forever(on_forever)
