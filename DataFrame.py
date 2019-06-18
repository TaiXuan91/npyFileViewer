import numpy as np

class DataFrame(object):
    def __init__(self):
        self.path = ""
        self.index = 0
        self.dataArray = np.array([])
    
    def ReadFile(self):
        self.dataArray = np.load(self.path)
    
    def ShowInPlot(self, plot):
        plot.clear()
        plot.axis('off')
        plot.imshow(self.dataArray[self.index],'gray')
        plot.figure.canvas.draw()
