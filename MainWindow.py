import sys
from PyQt5.QtCore import QDir, Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QCheckBox, QFileDialog, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QPushButton, QSizePolicy, QSpinBox,
        QVBoxLayout, QWidget)
from PyQt5.QtWidgets import (QWidget, QGroupBox, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont   

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QCheckBox, QComboBox,
        QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QMessageBox, QMenu, QPushButton, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QVBoxLayout)
import sys
import time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from DataFrame import DataFrame

class MainWindow(QWidget):
     
    def __init__(self):
        super().__init__()
        self.initData()
        self.initUI()
        self.createSelectGroupBox()
        self.createViewGroupBox()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.selectGroupBox)
        mainLayout.addWidget(self.viewGroupBox)
        # mainLayout.addWidget(self.messageGroupBox)
        self.setLayout(mainLayout)
        
    def initData(self):
        self.dataFrame = DataFrame()


    def initUI(self):
         
        QToolTip.setFont(QFont('SansSerif', 10))
         
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        # btn = QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.resize(btn.sizeHint())
        # btn.move(50, 50)      
         
        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('NumpyViewer')   
        self.show()
    
    def createSelectGroupBox(self):
        '''
        用于文件加载模块的控制面板。
        '''
        # create groupbox
        self.selectGroupBox = QGroupBox("Select File")
        self.selectGroupBox.setFixedHeight(80)
        # create widgets
        self.selectButton = QPushButton('Select a file')
        # widgets connect
        self.selectButton.clicked.connect(self.selectButtonClicked)
        # layout
        selectLayout = QHBoxLayout()
        selectLayout.addWidget(self.selectButton)
        self.selectGroupBox.setLayout(selectLayout)    

    def createViewGroupBox(self):
        '''
        用于创建查看区，由图像和查看按钮组成。
        '''
        # create groupbox
        self.viewGroupBox = QGroupBox("View")
        # create widgets
        # self.viewBox = QLabel('Show Image') # QLabel is widget, but QPixmap is not.
        # self.viewBox.setPixmap(QPixmap('./64.png'))
        self.static_canvas = FigureCanvas(Figure(figsize=(10, 10)))
        self.viewPlot = self.static_canvas.figure.subplots()
        self.lastButton = QPushButton('Last')
        self.nextButton = QPushButton('Next')
        self.levelLabel = QLabel('level：') # Show level
        # connect buttons
        self.nextButton.clicked.connect(self.nextButtonClicked)
        self.lastButton.clicked.connect(self.lastButtonClicked)
        # layout
        viewLayout = QHBoxLayout()
        # viewLayout.addWidget(self.viewBox)
        viewLayout.addWidget(self.static_canvas)
        ## sub layout
        viewButtonsLayout = QVBoxLayout()
        viewButtonsLayout.addWidget(self.lastButton)
        viewButtonsLayout.addWidget(self.nextButton)
        viewButtonsLayout.addWidget(self.levelLabel)
        viewLayout.addLayout(viewButtonsLayout)
        self.viewGroupBox.setLayout(viewLayout)
        # self.viewLabel = QLabel("View:o")

        # self.iconComboBox = QComboBox()
        # self.iconComboBox.addItem(QIcon(':/images/bad.png'), "Bad")
        # self.iconComboBox.addItem(QIcon(':/images/heart.png'), "Heart")
        # self.iconComboBox.addItem(QIcon(':/images/trash.png'), "Trash")

        # self.showIconCheckBox = QCheckBox("Show icon")
        # self.showIconCheckBox.setChecked(True)

        # iconLayout = QHBoxLayout()
        # iconLayout.addWidget(self.iconLabel)
        # iconLayout.addWidget(self.iconComboBox)
        # iconLayout.addStretch()
        # iconLayout.addWidget(self.showIconCheckBox)
        # self.iconGroupBox.setLayout(iconLayout)    
    def update_level_label(self):
        self.levelLabel.setText('level:'+str(self.dataFrame.index))

    def selectButtonClicked(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,"选取Numpy矩阵文件","./","Numpy Files (*.npy)")   #设置文件扩展名过滤,注意用双分号间隔
        if fileName1 is not None and fileName1!='':
            self.dataFrame.path = fileName1
            self.dataFrame.ReadFile()
            self.dataFrame.index = 0
            self.dataFrame.ShowInPlot(self.viewPlot)
            self.update_level_label()
        # draw something
        # self.viewPlot = self.static_canvas.figure.subplots()
        # height, width= self.dataFrame.dataArray[0].shape
        # self.viewBox.setPixmap(QPixmap())
        # print(fileName1)
        # print(filetype)

    def nextButtonClicked(self):
        if(self.dataFrame.index+1 >= self.dataFrame.dataArray.shape[0]):
            pass
        else:
            self.dataFrame.index = self.dataFrame.index + 1
        self.dataFrame.ShowInPlot(self.viewPlot)
        self.update_level_label()

    def lastButtonClicked(self):
        if(self.dataFrame.index-1 < 0):
            pass
        else:
            self.dataFrame.index = self.dataFrame.index - 1
        self.dataFrame.ShowInPlot(self.viewPlot)
        self.update_level_label()

    # def msg(self):
    #     directory1 = QFileDialog.getExistingDirectory(self,
    #                                 "选取文件夹",
    #                                 "C:/")                                 #起始路径
    #     print(directory1)
 
    #     fileName1, filetype = QFileDialog.getOpenFileName(self,
    #                                 "选取文件",
    #                                 "C:/",
    #                                 "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
    #     print(fileName1,filetype)
 
    #     files, ok1 = QFileDialog.getOpenFileNames(self,
    #                                 "多文件选择",
    #                                 "C:/",
    #                                 "All Files (*);;Text Files (*.txt)")
    #     print(files,ok1)
 
    #     fileName2, ok2 = QFileDialog.getSaveFileName(self,
    #                                 "文件保存",
    #                                 "C:/",
    #                                 "All Files (*);;Text Files (*.txt)")
