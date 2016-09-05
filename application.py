"""Application storage."""

modifiers = [
 'shift',
 'control',
 'alt',
 'windows',
]

modifier_index = 0 # The current position in the modifiers list.

grid_x = 0 # The x position in the key grid.
grid_y = 0 # The y position in the key grid.

from config import keys, grid_width

grid = []

for x in range(grid_width):
 if not keys:
  break
 row = []
 for y in range(grid_width):
  try:
   row.append(keys.pop(0))
  except IndexError:
   break
 grid.append(row)

