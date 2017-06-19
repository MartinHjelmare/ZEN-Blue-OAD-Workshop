# COM-Interface

## MATLAB - Example

This application note will explain how create a workﬂow using the ZEN-MATLAB connection. The basic idea is to control everything from within MATLAB (Master).

The ZEN Image Acquisition (Slave) software is "only" doing the image acquisition. The
signal to start the experiment is send from MATLAB to ZEN.

When the experiment is fnished, the CZI data are imported into MATLAB using BioFormats and "some" simple image analysis is carried out to underline the workﬂow concept.

For more detaiuled information please goto: [Control ZEN Blue and the microscope from MATLAB](https://de.mathworks.com/matlabcentral/fileexchange/50079-control-zen-blue-and-the-microscope-from-matlab?requestedDomain=www.mathworks.com)

![COM MATLAB_Running](/images/ZEN_ML_Running.png)

![COM_MATLAB_Result](/images/ZEN_MATLAB_Result_Figure.png)
