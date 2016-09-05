"""The keyboard class. Contains OS-specific key names and actions."""

import application
from subprocess import Popen, PIPE
from accessibility import ao2

mode_arrows = 'Arrow Keys'
mode_typing = 'Typing mode'

modes = [
 mode_arrows,
 mode_typing
]

class Keyboard(object):
 def __init__(self):
  self.mode = 0
  self.pressed = [] # The pressed keys.
  self.modifier_names = {
   'shift': 'Shift_L',
   'control': 'Control_L',
   'alt': 'Alt_L',
   'windows': 'Super_L'
  }
  self.key_names = {
   'Left': 'left arrow',
   'Up': 'up arrow',
   'Right': 'right arrow',
   'Down': 'down arrow',
   'Page_Up': 'page up',
   'Page_Down': 'page down',
   'Delete': 'forward delete',
   'bracketleft': 'left bracket',
   'bracketright': 'right bracket'
  }
 
 def _send(self, key):
  """Send a key."""
  key += '\n'
  p = Popen(['xte'], stdin = PIPE)
  p.communicate(key.encode())
 
 def toggle(self, key):
  """Toggle the state of a modifier key."""
  key_name = self.modifier_names.get(key, key)
  if key in self.pressed:
   self.pressed.remove(key)
   self._send('keyup %s' % key_name)
   action = 'released'
  else:
   self.pressed.append(key)
   self._send('keydown %s' % key_name)
   action = 'pressed'
  ao2.speak('%s %s.' % (key, action), interrupt = True)
 
 def send(self, key):
  """Send a single key."""
  self._send('key %s' % key)
 
 def press(self, key):
  """Press one of the arrow keys depending on mode."""
  if modes[self.mode] == mode_arrows:
   self.send(key)
  else:
   if key == 'Up':
    application.grid_y = max(0, application.grid_y - 1)
   elif key == 'Down':
    application.grid_y = min(application.grid_y + 1, len(application.grid) - 1)
   elif key == 'Left':
    application.grid_x = max(0, application.grid_x - 1)
   elif key == 'Right':
    application.grid_x = min(application.grid_x + 1, len(application.grid[application.grid_y]) - 1)
   if application.grid_x >= len(application.grid[application.grid_y]):
    application.grid_x = len(application.grid[application.grid_y]) - 1
   ao2.speak(self.get_friendly_name(application.grid[application.grid_y][application.grid_x]), interrupt = True)
 
 def get_friendly_name(self, key):
  """Get a human-readable name for key."""
  return self.key_names.get(key, key.replace('_', ' '))

keyboard = Keyboard()

