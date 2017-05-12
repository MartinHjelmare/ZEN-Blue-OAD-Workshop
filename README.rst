==================================
ZEN Blue OAD Workshop
==================================

OAD and Automated Microscopy – Smart Acquisition Strategies and Automation Tools
ZEN Blue is an open, flexible and powerful image acquisition platform that allows controlling a wide range of microscopes system. Additionally it offers various tools to automate workflows including acquisition and image analysis tasks.
Since that linkage and the automation of such workflows becomes increasingly ZENTo fulfill those demands the ZEN Blue platform offers various features and options, which are combined inside a concept called Open Application Development (OAD). It main components are:

*    Open CZI image data format
*    Python Scripting
*    Interfaces to ZEN
*    Experiment Feedback   

The workshop will give an overview about the various options and use cases allowing the user to start automating their workflows. Different examples will be explained in detail and during hands-on sessions.


Requirements
----------------------
* `ZEN Blue 2.3 <https://www.zeiss.com/microscopy/int/products/microscope-software/zen.html>`_
* `Python 3 (optional) <http://www.python.org>`_
* `BioFormatsRead Scripts (optional) <https://github.com/sebi06/BioFormatsRead>`_
* `MATLAB (optional) <https://www.mathworks.com/products/matlab.html>`_

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

References
----------
(1)  CZI - Image format for microscopes
     http://www.zeiss.com/czi
(2)  The OME-TIFF format.
     http://www.openmicroscopy.org/site/support/file-formats/ome-tiff

Screenshots
-----------

.. figure:: images/Guided_Acquisition.png
   :align: center
   :alt:

.. figure:: images/Guided_Acquisition_Workflow.png
   :align: center
   :alt:

.. figure:: images/Guided_Acquisition_schematic.png
   :align: center
   :alt:

Disclaimer
----------
*   Remark: Please use at your own risk.

:Author: Sebastian Rhode

:Version: 2017.05.02
