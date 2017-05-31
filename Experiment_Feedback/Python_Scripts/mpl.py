#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Functionality to use matplotlib figures in PySide GUIs. """

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import os
import matplotlib
from warnings import simplefilter

# Ignore warnings from matplotlib about fonts not being found.
simplefilter("ignore", UserWarning)

# Load our matplotlibrc file.
matplotlib.rc_file(os.path.join(os.path.dirname(__file__), "matplotlibrc"))

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt4 import QtCore, QtGui


class MPLWidget(FigureCanvas):
    """
    A widget to contain a matplotlib figure.
    """

    def __init__(self, parent=None, toolbar=False, tight_layout=True,
        autofocus=False, background_hack=True, **kwargs):
        """
        A widget to contain a matplotlib figure.

        :param autofocus: [optional]
            If set to `True`, the figure will be in focus when the mouse hovers
            over it so that keyboard shortcuts/matplotlib events can be used.
        """
        super(MPLWidget, self).__init__(Figure())

        self.figure = Figure(tight_layout=tight_layout)
        #self.figure = Figure(tight_layout=tight_layout, figsize=(12,12))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(parent)

        # Focus the canvas initially.
        self.canvas.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.canvas.setFocus()

        self.toolbar = None

        if autofocus:
            self._autofocus_cid = self.canvas.mpl_connect(
                "figure_enter_event", self._focus)


        self.figure.patch.set_facecolor([v/255. for v in
            self.palette().color(QtGui.QPalette.Window).getRgb()[:3]])

        return None


    def _focus(self, event):
        """ Set the focus of the canvas. """
        self.canvas.setFocus()
