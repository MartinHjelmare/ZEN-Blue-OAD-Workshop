# External Python Scripts for OAD

ZEN Blues used IronPython as its internal scripting language. This has several advantages but also means that some
python libraries like MatPlotLib, NumPy, SciPy, ... cannot be used directly within ZEN. For some use cases it is nvertheless
very useful to call certail "normal" python scripts from within ZEN.

Additionally Python's import functionality allows to re-use python code inside your own scripts.
