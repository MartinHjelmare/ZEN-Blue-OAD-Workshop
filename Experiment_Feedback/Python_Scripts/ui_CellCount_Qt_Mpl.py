# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\M1SRH\Documents\Projects\Experiment_Feedback\Scripts\CellCount_Qt_Mpl.ui'
#
# Created: Wed Nov 14 11:12:05 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CellCount_Qt_Mpl(object):
    def setupUi(self, CellCount_Qt_Mpl):
        CellCount_Qt_Mpl.setObjectName(_fromUtf8("CellCount_Qt_Mpl"))
        CellCount_Qt_Mpl.resize(966, 422)
        self.gridLayoutWidget = QtGui.QWidget(CellCount_Qt_Mpl)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 941, 401))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.barplot = MatplotlibWidget(self.gridLayoutWidget)
        self.barplot.setObjectName(_fromUtf8("barplot"))
        self.gridLayout.addWidget(self.barplot, 0, 1, 1, 1)
        self.sumplot = MatplotlibWidget(self.gridLayoutWidget)
        self.sumplot.setObjectName(_fromUtf8("sumplot"))
        self.gridLayout.addWidget(self.sumplot, 0, 2, 1, 1)

        self.retranslateUi(CellCount_Qt_Mpl)
        QtCore.QMetaObject.connectSlotsByName(CellCount_Qt_Mpl)

    def retranslateUi(self, CellCount_Qt_Mpl):
        CellCount_Qt_Mpl.setWindowTitle(QtGui.QApplication.translate("CellCount_Qt_Mpl", "Cell Count Widget", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibwidget import MatplotlibWidget
