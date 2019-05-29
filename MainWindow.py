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

class MainWindow(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
        self.createDecouplingGroupBox()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.decouplingGroupBox)
        # mainLayout.addWidget(self.messageGroupBox)
        self.setLayout(mainLayout)
        
         
         
    def initUI(self):
         
        QToolTip.setFont(QFont('SansSerif', 10))
         
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)      
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('桥梁结构安全算法分析')   
        self.show()
    
    def createDecouplingGroupBox(self):
        '''
        用于创建震动解耦模块的控制面板。
        '''
        self.decouplingGroupBox = QGroupBox("震动解耦")

        self.iconLabel = QLabel("Icon:")

        self.iconComboBox = QComboBox()
        self.iconComboBox.addItem(QIcon(':/images/bad.png'), "Bad")
        self.iconComboBox.addItem(QIcon(':/images/heart.png'), "Heart")
        self.iconComboBox.addItem(QIcon(':/images/trash.png'), "Trash")

        self.showIconCheckBox = QCheckBox("Show icon")
        self.showIconCheckBox.setChecked(True)

        iconLayout = QHBoxLayout()
        iconLayout.addWidget(self.iconLabel)
        iconLayout.addWidget(self.iconComboBox)
        iconLayout.addStretch()
        iconLayout.addWidget(self.showIconCheckBox)
        self.decouplingGroupBox.setLayout(iconLayout)    

    def createRegressionGroupBox(self):
        '''
        用于创建温度回归模块的控制面板。
        '''
        self.iconGroupBox = QGroupBox("Tray Icon")

        self.iconLabel = QLabel("Icon:")

        self.iconComboBox = QComboBox()
        self.iconComboBox.addItem(QIcon(':/images/bad.png'), "Bad")
        self.iconComboBox.addItem(QIcon(':/images/heart.png'), "Heart")
        self.iconComboBox.addItem(QIcon(':/images/trash.png'), "Trash")

        self.showIconCheckBox = QCheckBox("Show icon")
        self.showIconCheckBox.setChecked(True)

        iconLayout = QHBoxLayout()
        iconLayout.addWidget(self.iconLabel)
        iconLayout.addWidget(self.iconComboBox)
        iconLayout.addStretch()
        iconLayout.addWidget(self.showIconCheckBox)
        self.iconGroupBox.setLayout(iconLayout)    

    def createEvaluationGroupBox(self):
        '''
        用于创建评分模块的控制面板。
        '''
        self.iconGroupBox = QGroupBox("Tray Icon")

        self.iconLabel = QLabel("Icon:")

        self.iconComboBox = QComboBox()
        self.iconComboBox.addItem(QIcon(':/images/bad.png'), "Bad")
        self.iconComboBox.addItem(QIcon(':/images/heart.png'), "Heart")
        self.iconComboBox.addItem(QIcon(':/images/trash.png'), "Trash")

        self.showIconCheckBox = QCheckBox("Show icon")
        self.showIconCheckBox.setChecked(True)

        iconLayout = QHBoxLayout()
        iconLayout.addWidget(self.iconLabel)
        iconLayout.addWidget(self.iconComboBox)
        iconLayout.addStretch()
        iconLayout.addWidget(self.showIconCheckBox)
        self.iconGroupBox.setLayout(iconLayout)    