import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
matplotlib.use('Qt5Agg')


# 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，
# 又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=1.6, height=1.8, dpi=100):
        # 创建一个Figure，
        # 注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor='#f0f0f0', constrained_layout=True)
        self.ax = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)  # 初始化父类
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
