import logging, application
from pyglet import window, input
from version import name, version
from keyboard import keyboard, modes
from accessibility import ao2

logger = logging.getLogger(__name__)

window = window.Window(caption = '%s version %s' % (name, version))

def cycle_modifiers():
 """Cycle through the list of modifiers."""
 application.modifier_index += 1
 if application.modifier_index >= len(application.modifiers):
  application.modifier_index = 0
 key = application.modifiers[application.modifier_index]
 ao2.speak('%s%s' % (key, ' pressed' if key in keyboard.pressed else ''), interrupt = True)

def toggle_modifier():
 keyboard.toggle(application.modifiers[application.modifier_index])

def change_mode():
 keyboard.mode += 1
 if keyboard.mode >= len(modes):
  keyboard.mode = 0
 ao2.speak(modes[keyboard.mode])

def toggle_speech():
 keyboard.speak = not keyboard.speak
 ao2.speak('Speech %s.' % ('enabled' if keyboard.speak else 'disabled'))

buttons = {
 0: lambda: keyboard.press('Down'),
 1: lambda: keyboard.press('Right'),
 2: lambda: keyboard.press('Left'),
 3: lambda: keyboard.press('Up'),
 4: cycle_modifiers,
 5: toggle_modifier,
 6: change_mode,
 7: lambda: keyboard.send('BackSpace'),
 8: lambda: keyboard.send(application.grid[application.grid_y][application.grid_x]),
 9: lambda: keyboard.send('Return'),
 10: lambda: keyboard.send('space')
}

class JoystickEvents(object):
 def on_joybutton_release(self, joystick, button):
  if button in buttons:
   buttons[button]()
  else:
   ao2.speak(str(button))
 def on_joyhat_motion(self, joystick, hat_x, hat_y):
  """Joystick hat was pressed."""
  ao2.speak('%s, %s.' % (x, y))

joysticks = []
for j in input.get_joysticks():
 logger.info('Found joystick %s.', j.device.name)
 joysticks.append(j)
 j.open()
 j.push_handlers(JoystickEvents())

@window.event
def on_close():
 for j in joysticks:
  logger.info('Closing joystick %s.', j.device.name)
  j.close()
  for p in keyboard.pressed:
   logger.info('Releasing key %s.', p)
   keyboard.toggle(p)

