# Guided Acquistion

For a growing number of applications, it will be crucial to acquire data in a smart
way. One way to achieve this goal is to build a smart microscope, which essentially
means creating smart software workﬂows to control the hardware based on image analysis
results.

Idea or Task:

* Scan or inspect a large area (or a long period of time).
* Detect an "interesting" object.
* Acquire detailed data for every event.
* Automate the workﬂow to minimize user interference.

First of all it is important to defne what a **Object of Interest** can actually be.

* An object that meets specifc criteria regarding its parameters (size, brightness,
shape, intensity, ...)
* A specifc change of a parameter during an experiment (e.g. a cell gets really
"bright" upon ...)

It could be something quite simple. For instance one can have lots of cells, that are
stained with blue dye, and only a few of them (maybe where the transfection worked
. . . ) are also expressing GFP. The idea here would be to detect all cells that are positive
for both colors and acquire an z-Stack for every cell (blue & green) that meets those
criteria. Therefore this kind of application requires three major tasks:

1. **Define the Overview Scan Experiment.**
2. **Define the object detection rules, e.g. setup image analysis.**
3. **Define the Detailed Scan(s) to be carried out in case of a "positive"**
object.

![Guided_Acquisition_WorkFlow](/images/Guided_Acquisition_WorkFlow.png)

## OAD User Dialog for Guided Acquistion

![Guided_Acquisition_WorkFlow Dialog](/images/Guided_Acquisition_Dialog_anno.png)
