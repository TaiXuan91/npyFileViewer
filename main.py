#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
ZetCode PyQt5 tutorial
 
This example shows a tooltip on
a window and a button.
 
author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""
 
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont   
from MainWindow import MainWindow
 


         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())