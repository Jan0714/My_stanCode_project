"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program can show a line chart(with name, rank and years on it) when users type the names.
The rank of the name data is based on the dictionary 'name_data' in babynames.py.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """

    x_coordinate = GRAPH_MARGIN_SIZE + year_index * (width - GRAPH_MARGIN_SIZE*2)/(len(YEARS))
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # Draw the fixed background grid
    y_spacing = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK  # Calculate the spacing in y axis

    for n in range(len(lookup_names)):
        if lookup_names[n] in name_data:
            name = lookup_names[n]
            # Define the sequence of the line color
            if len(lookup_names) > len(COLORS):
                n = n % 4
            for i in range(len(YEARS)):
                year = str(YEARS[i])
                # Get the rank value and y value when the rank is smaller than max rank in certain year
                if year in name_data[name]:
                    rank = name_data[name][year]
                    y = GRAPH_MARGIN_SIZE + int(rank)*y_spacing
                # Define the rank value and y value when the rank is bigger than max rank
                else:
                    rank = "*"
                    y = GRAPH_MARGIN_SIZE + MAX_RANK*y_spacing
                x = get_x_coordinate(CANVAS_WIDTH, i)
                # Get the y value and x value in the last year
                if i > 0:
                    last_year = str(YEARS[i-1])
                    if last_year in name_data[name]:
                        rank_last_year = name_data[name][last_year]
                        y_last_year = GRAPH_MARGIN_SIZE + int(rank_last_year)*y_spacing
                    else:
                        y_last_year = GRAPH_MARGIN_SIZE + MAX_RANK*y_spacing
                    x_last_year = get_x_coordinate(CANVAS_WIDTH, i - 1)
                    canvas.create_line(x_last_year, y_last_year, x, y, width=LINE_WIDTH, fill=COLORS[n])
                canvas.create_text(x + TEXT_DX, y, text=name + " " + rank, anchor=tkinter.SW, fill=COLORS[n] )


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
