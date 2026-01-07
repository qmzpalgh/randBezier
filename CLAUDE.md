# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Animated bezier curve visualization. The curve's anchor points and control points move around the screen using random acceleration values, creating organic flowing motion.

## Running

### Python (Pygame)
```
pip install pygame
python rand_bezier.py
```
Press ESC to exit.

### Processing (original)
Open `randBezier.pde` in Processing IDE or:
```
processing-java --sketch=. --run
```

## Architecture

Both versions share the same logic:
- **4 bezier points**: Each has position and velocity vectors
- **Motion system**: Random acceleration applied each frame; velocities update positions; boundary collision reverses velocity
- **Rendering**: Cubic bezier curve drawn with fade effect for trail visualization

### Python (`rand_bezier.py`)
- Uses Pygame for windowing and drawing
- `bezier_point()`: Calculates cubic bezier interpolation
- `draw_bezier()`: Renders curve as line segments
- Fade effect via semi-transparent overlay surface

### Processing (`randBezier.pde`)
- PVector ArrayList with interleaved position/velocity storage
- Built-in `bezierVertex()` for curve rendering
