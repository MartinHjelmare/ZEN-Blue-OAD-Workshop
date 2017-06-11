# OAD - General Concept and Key Features

* **Open Application Development (OAD)** uses powerful **Python Scripts** to **simplify, customize** and **automate** your workflows.

* The **CZI-API for .NET / C++** and **BioFormats (CZIReader)** allow easy access to CZI files from many external applications.

* **Analyze** and **Exchange** data with applications like **Fiji, Python, Knime, CellProfiler, Icy, MATLAB, Excel** and …

* Create **"smart"** experiments with **Experiment Feedback** and modify the acquisition **On-the-fly** based on **Online Image Analysis** and **External Inputs**.

## General Remarks

In order to understand the following explanations, it is useful to clarify some things firsts to avoid misunderstandings.

* ZEN Blue is programmed in C# and therefore part of the .NET world of Microsoft.

* To access ZEN objects (DLLs & Co) via the so-called Simple API from within an OAD macro ZEN uses IronPython as its scripting language, which is the .NET implementation of Python.

* From IronPython one automatically has the option to use .NET libraries. This can save a lot of work since one does not have to re-invent the wheel.

* An external application is a program that runs on the same or on a different machine. Typical applications that are useful in the context of ZEN are Fiji, Icy, Python, MATLAB, KNIME, CellProfiler, and Excel.

* ZEN offers its own integrated development environment (IDE) to create, record and debug your own Open Application development (OAD) scripts.

* The CZIReader is a part of the BioFormats library, that is used to read CZI files directly into Fiji and various other SW packages (Python, CellProfiler, KNIME, MATLAB, Icy, Columbus, …). 


## OAD - Overview about interfaces

![OAD Overview](/images/OAD_Overview.png)

## ZEN Macro Interface

![OAD - ZEN Macro Interface](/images/ZEN_Macro_Interface.png)
