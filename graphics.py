import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import math
import resources as r
matplotlib.use('TkAgg')

# Initialize an instance of Tk
def wood():
    rootter = tk.Tk()

    # Initialize matplotlib figure for graphing purposes
    fig = plt.figure(1)
    dataa=[]
    secs,data=r.wood.getger()
    for i in secs:
        if i!=1:
            for j in range(i):
                dataa.append(data[secs.index(i)-1])
        
    # Special type of "canvas" to allow for matplotlib graphing
    canvas = FigureCanvasTkAgg(fig, master=rootter)
    plot_widget = canvas.get_tk_widget()
    plt.plot(dataa)
    plt.ylabel('resources, n')
    plt.xlabel('time, secs')
    # Add the plot to the tkinter widget
    plot_widget.grid(row=0, column=0)

    rootter.mainloop()
