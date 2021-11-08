# 3D visualization tools review
A brief review of 3D visualization tools available that are based on Python but not exclusively. 
This is not a final or conlusive review. 

The anticipated user groups are beginners and users with little experience, which can be supported by more experienced members with more programming skills, especially in Python.

# Paraview
[Paraview](https://www.paraview.org/) is like the other tools from [Kitware](https://www.kitware.com/) ([3DSlicer](https://www.slicer.org/), [TomViz](https://tomviz.org/)). 
Although Paraview requires not strictly programming skills, good knowledge about using processing pipes and getting used to preparing viewing tasks requires initial reading of the manual. I think Paraview can be compared somewhat to the commercial tool [Amira](https://en.wikipedia.org/wiki/Amira_(software)). 
However, in this context, Paraview provides a Python environment for scripting, which may be advantageous if trying to explore more unconventional processing methods for 3D visualization.
Some more advanced features to mention might be mesh generation, surface plotting. 
Importing a 3D volume may require some understanding of what data structures Paraview are targeting. Although we might assume that npy files can be imported, converting to vtk file format is required. 
There may be technical reasons to do so, which I did not follow up on. Converting from npy to vtk seems to be not too much effort depending on the data complexity and if certain meta-data need to pertain.

![](PV_show.gif)

# TomViz 
[TomViz](https://tomviz.org/) seems to have the most relevant features prepared. The anticipated preprocessing for the nsOCT [[1]](#nsOCT) algorithm may also run in the provided Python version.
It can load npy files, and as it is straightforward to convert mat to npy it would also work for data generated with MATLAB.
The provided Python version has a minimal set of packages related to parallel computing and in-memory communication. If any script must run in another Python version, this needs to happen over intermediate scripting.

<a id="nsOCT">[1]</a> Alexandrov, S. et al. (2021) ‘Accessing depth-resolved high spatial frequency content from the optical coherence tomography signal’, Scientific Reports, 11(1), p. 17123. doi:10.1038/s41598-021-96619-7.

# 3DSlicer
3DSlicer focuses on 3D slice visualization and is less concerned with 3D volume visualization.
Importing data seems a bit of an effort as it needs to be in vtk or DICOM. The user interface is extensive but also a bit difficult at times. 
There seems to be an extensive extension database integrated, but it is not clear yet how useful this would be. In general, the extensions seem to provide methods for segmentation for specific medical images.
There is a MATLAB bridge extension that may be of interest [(3DSlicer ML bridge)](https://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/MatlabBridge).
For tissue imaging, the prepared views of the slices may be relevant and helpful. There seems sufficient access to enhance viewing programmatically, which may alleviate some of the initial data conversion to vtk and provide prepared views.

# Mayavi
Mayavi (8-11-2021) currently

# PyVista
PyVista was not considered here as it seems to run in iPython notebooks mainly. PyVista will be only relevant if the users are accustomed to iPython and analyse data with it.



