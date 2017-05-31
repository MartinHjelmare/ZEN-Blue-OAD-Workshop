# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\TFS\Doc\3-ZIS\3-Development\Discussions\ExperimentFeedback\Release_DVD\Python_Scripts_for_Data_Display\Ratio_Online_Plot2.ui'
#
# Created: Mon Sep 22 14:47:00 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Ratio_Online_Plot(object):
    def setupUi(self, Ratio_Online_Plot):
        Ratio_Online_Plot.setObjectName(_fromUtf8("Ratio_Online_Plot"))
        Ratio_Online_Plot.resize(966, 422)
        self.gridLayoutWidget = QtGui.QWidget(Ratio_Online_Plot)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 941, 401))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ratioplot = MatplotlibWidget(self.gridLayoutWidget)
        self.ratioplot.setObjectName(_fromUtf8("ratioplot"))
        self.gridLayout.addWidget(self.ratioplot, 0, 1, 1, 1)

        self.retranslateUi(Ratio_Online_Plot)
        QtCore.QMetaObject.connectSlotsByName(Ratio_Online_Plot)

    def retranslateUi(self, Ratio_Online_Plot):
        Ratio_Online_Plot.setWindowTitle(_translate("Ratio_Online_Plot", "Ratio Online", None))

from matplotlibwidget import MatplotlibWidget
