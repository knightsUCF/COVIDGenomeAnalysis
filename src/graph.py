from bokeh.plotting import figure, output_file, show



class Graph():

    def __init__(self, title, x_label, y_label, x_start, x_end, y_start, y_end):
        output_file("corona_data.html", title="mutation rate")
        self.plot = figure(title=title, x_axis_label=x_label, y_axis_label=y_label, y_range=[y_start, y_end], x_range = [x_start, x_end])


    def AddData(self, x, y, radius, color):

        if color == 'green':
            r = 120
            g = 240
            b = 255
        if color == 'purple':
            r = 120
            g = 240
            b = 255

        self.plot.circle(x, y, size = 5, color=(r, g, b))


    def Show(self):
        show(self.plot)
