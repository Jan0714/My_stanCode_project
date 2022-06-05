"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program makes a game called "break out".
This program set bricks, the ball, the velocity of ball,
the paddle, and all the items and conditions
which will be used in the "break out" game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 9  # Initial vertical speed for the ball.
MAX_X_SPEED = 7        # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3          # Number of attempts


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height, x=(self.window_width-paddle_width)/2,
                       y=self.window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window_width-ball_radius*2)/2, y=(self.window_height-ball_radius*2)/2)
        self.ball.filled = True
        self.window.add(self.ball)
        # Create a score board
        self.score = 0
        self.score_label = GLabel('Score:' + str(self.score))
        self.window.add(self.score_label, 0, self.score_label.height)
        # Initial lives
        self.num_lives = NUM_LIVES
        self.num_lives_label = GLabel('Lives:' + str(self.num_lives))
        self.window.add(self.num_lives_label, self.window.width-self.num_lives_label.width, self.num_lives_label.height)
        # Total number of bricks
        self.total_bricks = BRICK_ROWS * BRICK_COLS
        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.bricks = GRect(width=brick_width, height=brick_height)
                self.bricks.filled = True
                self.window.add(self.bricks, i * (brick_width + brick_spacing) - brick_spacing, brick_offset + (j * (brick_height + brick_spacing) - brick_spacing))
                if j < 2:
                    self.bricks.fill_color = 'red'
                elif j < 4:
                    self.bricks.fill_color = 'orange'
                elif j < 6:
                    self.bricks.fill_color = 'yellow'
                elif j < 8:
                    self.bricks.fill_color = 'green'
                else:
                    self.bricks.fill_color = 'blue'
        # Default initial velocity for the ball
        self.__dx = self.set_ball_velocity()
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        onmousemoved(self.set_paddle_position)
        onmouseclicked(self.start_game)
        # The switch of a game
        self.is_start_game = False
        # The object that is touched
        self.obj = None

    def start_game(self, m):
        """
        :param m: Mouse event, to control the start of the breakout game.
        """
        self.is_start_game = True

    def set_paddle_position(self, event):
        """
        :param event: Mouse event, to control the position of the paddle.
        """
        if self.paddle.width/2 <= event.x <= self.window.width-self.paddle.width/2:
            self.paddle.x = event.x-self.paddle.width/2

    def set_ball_velocity(self):
        """
        Set random X velocity.
        :return:dx
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def reset_ball(self):
        """
        Let the ball back to start point after the ball fall over the window.
        """
        self.set_ball_velocity()
        self.set_ball_position()
        self.window.add(self.ball)

    def set_ball_position(self):
        """
        Set up initial ball position.
        """
        self.ball.x = (self.window.width - BALL_RADIUS * 2) / 2
        self.ball.y = (self.window.height - BALL_RADIUS * 2) / 2

    def hit_a_object(self):
        """
        Let the ball bounce from the paddle and also let the ball remove and bounce from the bricks.
        """
        for x in range(int(self.ball.x), int(self.ball.x+self.ball.height+1), int(self.ball.height)):
            for y in range(int(self.ball.y), int(self.ball.y+self.ball.width+1), int(self.ball.width)):
                #  get 4 edge of the ball
                self.obj = self.window.get_object_at(x, y)
                if self.obj is not None:
                    if self.obj is self.score_label:
                        pass
                    elif self.obj is self.num_lives_label:
                        pass
                    elif self.obj is not self.paddle:
                        self.window.remove(self.obj)
                        self.score += 1
                        self.score_label.text = 'Score:' + str(self.score)
                        self.__dy = - self.__dy
                    else:
                        if self.__dy > 0:
                            self.__dy = - self.__dy
                    return

    def touch_wall(self):
        """
        Let the ball bounce between the walls.
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = - self.__dx
        if self.ball.y <= 0:
            self.__dy = - self.__dy
        if self.ball.y + self.ball.height >= self.window.height:
            self.num_lives -= 1
            self.num_lives_label.text = 'Lives:' + str(self.num_lives)
            self.is_start_game = False
            self.reset_ball()
            if self.num_lives == 0:
                game_over_label = GLabel('GAME OVER')
                game_over_label.font = '-60'
                game_over_label.color = 'red'
                self.window.add(game_over_label, self.window_width/2-game_over_label.width/2, self.window_height/2 + game_over_label.height)

    # Getter
    def get_dx(self):
        return self.__dx

    # Getter
    def get_dy(self):
        return self.__dy

