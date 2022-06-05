"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.


This program plays a game called "break out" in which players moving the paddle to make the ball bounce
and break all bricks!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)
        if graphics.num_lives > 0:
            if graphics.is_start_game:
                graphics.ball.move(graphics.get_dx(), graphics.get_dy())
                graphics.hit_a_object()
                graphics.touch_wall()
            if graphics.score == graphics.total_bricks:
                break


if __name__ == '__main__':
    main()
