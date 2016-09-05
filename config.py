"""Program configuration."""

def get_grid_width(l):
 """Get the width of the key grid."""
 x = 0
 while True:
  x += 1
  if x ** 2 > l:
   return x

keys = [*list('abcdefghijklmnopqrstuvwxyz1234567890'),
 'comma',
 'period',
 'apostrophe',
 'semicolon',
 'slash',
 'equal',
 'minus',
 'bracketleft',
 'bracketright',
 'backslash',
 'grave',
 'Page_Up',
 'Page_Down',
 'Home',
 'End',
 'Tab',
 'Escape',
 'Delete'
]

for x in range(12):
 keys.append('F%s' % (x + 2))

grid_width = get_grid_width(len(keys))

