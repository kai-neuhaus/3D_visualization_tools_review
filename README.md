# 3D visualization tools review
A brief review of 3D visualization tools available that are based on Python but not exclusively. This is not a final or conlusive review.

I try to show tools that need minimal programming knowledge first.

# Paraview
[Paraview](https://www.paraview.org/) is like the other tools from [Kitware](https://www.kitware.com/) ([3DSlicer](https://www.slicer.org/), [TomViz](https://tomviz.org/)). 
Although Paraview requires not strictly programming skills, good knowledge about using processing pipes and getting used to preparing viewing tasks requires initial reading of the manual. I think Paraview can be compared somewhat to the commercial tool [Amira](https://en.wikipedia.org/wiki/Amira_(software)). 
However, in this context, Paraview provides a Python environment for scripting, which may be advantageous if trying to explore more unconventional processing methods for 3D visualization.
Some more advanced features to mention might be mesh generation, surface plotting. 
Importing a 3D volume may require some understanding of what data structures Paraview are targeting. Although we might assume that npy files can be imported, converting to vtk file format is required. 
There may be technical reasons to do so, which I did not follow up on. Converting from npy to vtk seems to be not too much effort depending on the data complexity and if certain meta-data need to pertain.


# Mayavi
Mayavi (8-11-2021) currently
