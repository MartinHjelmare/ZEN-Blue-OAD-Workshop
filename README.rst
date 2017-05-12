==================================
ZEN Blue OAD Workshop
==================================

OAD and Automated Microscopy – Smart Acquisition Strategies and Automation Tools
ZEN Blue is an open, flexible and powerful image acquisition platform that allows controlling a wide range of microscopes system. Additionally it offers various tools to automate workflows including acquisition and image analysis tasks. Since that linkage and the automation of such workflows becomes increasingly ZENTo fulfill those demands the ZEN Blue platform offers various features and options, which are combined inside a concept called Open Application Development (OAD). It main components are:

*    Open CZI image data format
*    Python Scripting
*    Interfaces to ZEN
*    Experiment Feedback   
The workshop will give an overview about the various options and use cases allowing the user to start automating their workflows. Different examples will be explained in detail and during hands-on sessions.

:Author: Sebastian Rhode

:Version: 2017.05.02

Important Requirements
----------------------
* `Python 2 or 3 <http://www.python.org>`_
* `Numpy <http://www.numpy.org>`_
* `Matplotlib <http://www.matplotlib.org>`_
* `python-bioformats <https://github.com/CellProfiler/python-bioformats>`_
* `BioFormats package <http://downloads.openmicroscopy.org/bio-formats/>`_
* `javabridge <https://pypi.python.org/pypi/javabridge>`_
* `czifile <http://www.lfd.uci.edu/~gohlke/code/czifile.py.html>`_
* `tifffile <http://www.lfd.uci.edu/~gohlke/code/tifffile.py.html>`_

Notes
-----
The package is still under development and was mainly tested with CZI files.

The python-bioformats package includes loci_tool.jar but it is also possible to use the latest bioformats_package.jar.
Currently the 5.1.10 or the 5.4.1 version of bioformats_package.jar is used.

The new 5.4.1 version of the BioFormats library offers various new features for reading especially CZI images,
which are currently not fully supported by python-bioformats. But most of the functionality should work without any problems.

Some more information can be found at: `python-and-bioformats <http://slides.com/sebastianrhode/python-and-bioformats/fullscreen>`_

Important Remark: Not all function where tested to work with Python 3 yet.

Acknowledgements
----------------
*   The ZEN Reserach & Developemt Team
*   Christoph Gohlke from providing the czifile.py and tifffile.py.
*   The Cellprofiler team for providing python-bioformats.
*   The OME people for creating BioFormats.

References
----------
(1)  CZI - Image format for microscopes
     http://www.zeiss.com/czi
(2)  The OME-TIFF format.
     http://www.openmicroscopy.org/site/support/file-formats/ome-tiff
(3)  Read microscopy images to numpy array with python-bioformats.
     http://ilovesymposia.com/2014/08/10/read-microscopy-images-to-numpy-arrays-with-python-bioformats/

Screenshots
-----------

.. figure:: images/BFRead_Test.png
   :align: center
   :alt:

.. figure:: images/OME-XML_output.png
   :align: center
   :alt:

.. figure:: images/testwell96_planetable_XYZ-Pos.png
   :align: center
   :alt:

Disclaimer
----------
*   Remark: Please use at your own risk.
