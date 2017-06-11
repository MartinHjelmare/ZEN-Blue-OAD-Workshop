# Experiment Feedback

Experiment feedback (conditional or adaptive experiments) allows the defnition of specifc rules and actions to be performed during an experiment. This allows changing the course of an experiment depending on the current system status or the nature of the acquired data on runtime. Moreover, it is possible to integrate certain tasks like data logging or starting an external application, directly into the imaging experiment. Typically, but not exclusively, such an experiment connects the image pickup with an
automatic image analysis.

* **Adaptive Acquisition Engine** allows modifying **running experiments** using Python scripts.

* Python Scripts can access the **current system status** and results from **Online Image Analysis** on runtime during the experiment.

* **Data Logging** or starting an **External Application** (Python, Fiji, MATLAB, …), directly from within the imaging experiment is possible.

![ExpFeedback Basic WorkFlow](/images/ExpFeedback_Basic_Workflow.png)
