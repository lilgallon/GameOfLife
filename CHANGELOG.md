## Changelog
Some commit may not appear here since it fix / add little things.

### Legend :
❌ Removed | ✔️ Added | 💫 Fixed | ✨ Improved | 🏗️ Unfinished

### Update #1 (version 0) :
- ✔ Grid class

### Update #2 (version 0) :
- ✔ Main file
- ✔ Graphics utility
- ✔ Cell class
- 🏗️ Grid

### Update #3 (version 0) :
- ✔ Grid rules
- ✔ Basic mouse interaction

### Update #4 (version 0) :
- 🏗️ Advanced interaction (move with keyboard / zoom with mouse wheel / day increment with left mouse click)

### Update #5 (version 0) :
- 🏗️ Advanced interaction (move with right mouse click)

### Update #6 (version 0) :
- ✔ Feature to add a new cell with the mouse
- ✨ Changed interaction (move with mouse left click, add a cell with mouse right click, day increment with space bar)
- ✨ Grid doing 19x19 grid instead of 20x20 (python range(a,b) takes values from a to b-1 included)
- 💫 Resizing

### Update #7 (version 0) :
- ✨ Improved interaction (right click on a living cell kills it)
- 💫 Fixed __eq__ method of cell

### Update #8 (version 0) : Beginning of the optimization
- ✨ Inverted line and column to match with x and y order
- ✨ Changed "cells" list to "alive_entities" and added a "dead_entities" list that contains every dead entity that could get alive with rule #2, because
it is pointless to consider the other cells as dead since they will never get alive (no living cell is near).
- ✨ Optimized update_cell cell method ( gained len(cells) iterations )
- ✨ Optimized movement by adding an origin parameter to the grid drawer instead of moving every living cell ( gained len(cells) iterations)
- ✨ Optimized is_alive method ( gained ~= len(cells) iterations )

### Update #9 (version 0) :
- 💫 Fixed add / remove entity on the cursor that always created a new cell instead of killing it if it is alive
- ✨ Interaction: it is now possible to add / remove entities by keeping left click down