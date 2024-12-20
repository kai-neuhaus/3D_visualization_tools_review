# 3D visualization tools review
A brief review of 3D visualization tools available that are based on Python but not exclusively. 
This is not a final or conlusive review. 

The anticipated user groups are beginners and users with little experience, which can be supported by more experienced members with more programming skills, especially in Python.

# Kitware
https://www.kitware.com/platforms/
A list of tools explained here can be found at the link.
The Kitware platforms provide an overview of more tools.

# Paraview
[Paraview](https://www.paraview.org/) is like the other tools from [Kitware](https://www.kitware.com/) ([3DSlicer](https://www.slicer.org/), [TomViz](https://tomviz.org/)). 
Although Paraview requires not strictly programming skills, good knowledge about using processing pipes and getting used to preparing viewing tasks requires initial reading of the manual. I think Paraview can be compared somewhat to the commercial tool [Amira](https://en.wikipedia.org/wiki/Amira_(software)). 
However, in this context, Paraview provides a Python environment for scripting, which may be advantageous if trying to explore more unconventional processing methods for 3D visualization.
Some more advanced features to mention might be mesh generation, surface plotting. 
Importing a 3D volume may require some understanding of what data structures Paraview are targeting. Although we might assume that npy files can be imported, converting to vtk file format is required. 
There may be technical reasons to do so, which I did not follow up on. Converting from npy to vtk seems to be not too much effort depending on the data complexity and if certain meta-data need to pertain.
(The CT data are from __University of North Carolina__ Volume Rendering Test Data Set (http://graphics.stanford.edu/data/voldata/)) 
![Paraview demo](PV_show.gif)

# Paraview in Webbrowser
It may not be a primary use case for heavy data processing but it may help to share specific 3D data views. 
Not sure if any collaborative features have been added already.
https://kitware.github.io/paraview-glance/

![Paraview demo web](PV_show_online.gif)

# TomViz 
(https://tomviz.org/docs/)
![TomViz](TomViz.gif)
[TomViz](https://tomviz.org/) seems to have the most relevant features prepared. The anticipated preprocessing for the nsOCT [[1]](#nsOCT) algorithm may also run in the provided Python version.
For inexperienced users, TomViz may be somewhat easier to use compared to Paraview.
It can load npy files, and as it is straightforward to convert mat to npy it would also work for data generated with MATLAB.
The provided Python version has a minimal set of packages related to parallel computing and in-memory communication. If any script must run in another Python version, this needs to happen over intermediate scripting.

<a id="nsOCT">[1]</a> Alexandrov, S. et al. (2021) ‘Accessing depth-resolved high spatial frequency content from the optical coherence tomography signal’, Scientific Reports, 11(1), p. 17123. doi:10.1038/s41598-021-96619-7.

# 3DSlicer
3DSlicer focuses on 3D slice visualization and is less concerned with 3D volume visualization, although also showing 3D volumes.
There seem to be many extensions available that provide additional support specific medical imaging workflows.
The documentation claims that:
"A research software platform, which allows researchers to quickly develop and evaluate new methods and distribute them to clinical users. All features are available and extensible in Python and C++. A full Python environment is provided where any Python packages can be installed and combined with built-in features. Slicer has a built-in Python console and can act as a Jupyter notebook kernel with remote 3D rendering capabilities."
(https://slicer.readthedocs.io/en/latest/user_guide/about.html)

![](3DSlicer.gif)

Importing data seems to be possible over the vtk or DICOM formats. However, converting ordinary npy files is straightforward (see example [npy2vtk_t0.py](npy2vtk_t0.py)).
The user interface is extensive but also a bit difficult at times. 
There seems to be an extensive extension database integrated, but it is not clear yet how useful this would be specifically for tissue imaging and the nsOCT method. In general, the extensions seem to provide methods for segmentation for specific medical images.
There is a MATLAB bridge extension that may be of interest [(3DSlicer ML bridge)](https://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/MatlabBridge).
For tissue imaging, the prepared views of the slices may be relevant and helpful. 
A Python console can be accessed as well which might allow to enhance viewing programmatically. 
Programmatic setup of th eview may alleviate initial difficulties for beginners and can support the data conversion to vtk.



Fedorov A., Beichel R., Kalpathy-Cramer J., Finet J., Fillion-Robin J-C., Pujol S., Bauer C., Jennings D., Fennessy F.M., Sonka M., Buatti J., Aylward S.R., Miller J.V., Pieper S., Kikinis R. 3D Slicer as an Image Computing Platform for the Quantitative Imaging Network. Magnetic Resonance Imaging. 2012 Nov;30(9):1323-41. PMID: 22770690. PMCID: PMC3466397.

# Mayavi
[working on it]

# PyVista
PyVista was not considered here as it seems to run in iPython notebooks mainly. PyVista will be only relevant if the users are accustomed to iPython and analyse data with it.

# Other
By now other tools have become available but I have not found time yet to add more details.

Maybe more noteworthy could be Napari.

But again, Napari is possibly not beginner friendly per se. Some more detailed understand about additional python packages is required before it is possible to work with it efficiently.

