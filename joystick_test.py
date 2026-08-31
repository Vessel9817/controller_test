'''
Fork of: https://github.com/pyglet/pyglet/blob/master/examples/input/joystick.py
Complete with AV8R Flight Stick calibrated joystick, buttons, switches, dials, z-rotation and deadzone
'''

import pyglet
import math

# TODO Configure joystick deadzone?

# TODO Add z-rotation controls

# TODO Configure device manager?

#pyglet.input.win32._di_device_manager._recheck_devices()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE=(255, 0, 255)

joysticks = pyglet.input.get_joysticks()
assert joysticks, 'No joystick device is connected'
joystick = joysticks[0]
joystick.open()

window = pyglet.window.Window(width=800, height=800)
batch = pyglet.graphics.Batch()

window.set_caption('Joystick Test')

# Labels
pyglet.text.Label('Buttons:', x=15, y=window.height - 25, font_size=14, batch=batch, color=WHITE)
pyglet.text.Label('D-pad:', x=window.width - 125, y=window.height - 25, font_size=14, batch=batch, color=WHITE)

button_labels = []
button_shapes = []
rows = len(joystick.buttons) + 1 # +1 for custom button

for i in range(len(joystick.buttons)):
    y = window.height - 50 - 25 * (i % rows)
    x = 35 + 60 * (i // rows)
    label = pyglet.text.Label(f'{i}:', x=x, y=y, font_size=14, anchor_x='right', batch=batch, color=WHITE)
    button_labels.append(label)
    shape = pyglet.shapes.Rectangle(x + 10, y + 1, 10, 10, batch=batch, color=RED)
    button_shapes.append(shape)

# Adding custom dial
y = window.height - 25 * (rows + 1)
x = 35
custom_label = pyglet.text.Label(f'{rows-1}:', x=x, y=y, font_size=14, anchor_x='right', batch=batch, color=WHITE)
custom_dial = pyglet.shapes.Rectangle(x + 10, y + 1, 10, 10, batch=batch, color=RED)

joystick_rect = pyglet.shapes.Rectangle(window.width // 2, window.height // 2, 10, 10, batch=batch, color=PURPLE)
joystick_rect.anchor_position = joystick_rect.width // 2, joystick_rect.height // 2
d_pad_empty_rects = tuple(
    pyglet.shapes.Rectangle(window.width - 75, window.height - 100, 10, 10, batch=batch, color=RED)
    for _ in range(9)
)
d_pad_rect = pyglet.shapes.Rectangle(window.width - 75, window.height - 100, 10, 10, batch=batch, color=BLUE)

@window.event
def on_draw():
    window.clear()
    batch.draw()
    x = round((.5 * joystick.x + 1), 2) * window.width / 2
    y = round((-.5 * joystick.y + 1), 2) * window.height / 2
    rx = (.5 * joystick.rx + 1) * 60
    ry = (-.5 * joystick.ry + 1) * 60
    z = joystick.z * 50

    # Axes
    joystick_rect.position = x, y
    joystick_rect.anchor_position = joystick_rect.width // 2, joystick_rect.height // 2
    joystick_rect.width = 10 + rx + z
    joystick_rect.height = 10 + ry + z

    # Buttons
    for i in range(len(joystick.buttons)):
        rect = button_shapes[i]
        rect.color = GREEN if joystick.buttons[i] else RED

    # Dial
    custom_dial.color = GREEN if not (joystick.buttons[-1] or joystick.buttons[-2]) else RED

    # D-pad (hat)
    d_pad_rect.position = (window.width - 100 + joystick.hat_x * 50), (window.height - 100 + joystick.hat_y * 50)

    for i, rect in enumerate(d_pad_empty_rects):
        x, y = (i % 3) - 1, (i // 3) - 1
        rect.position = (window.width - 100 + x * 50), (window.height - 100 + y * 50)

    # Z-rotation (twisting joystick)
    colour = math.floor(25 + 0.9 * (255/2 * (joystick.rz + 1)))
    joystick_rect.color = (colour, colour, colour)

pyglet.app.run()
