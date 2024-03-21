#||AUM||
#||Shree Ganeshaya Namaha||



Here's the Python code using plotly to read a .gii surface file from AFNI and visualize it:

Python
import nibabel as nib
import plotly.graph_objects as go

# Replace "path/to/your/file.gii" with the actual path to your file
file_path = "path/to/your/file.gii"

# Read the surface data
gii_data = nib.load(file_path)

# Extract data arrays
vertices = gii_data.darrays[0].data
triangles = gii_data.darrays[1].data

# Define colors for each vertex (optional)
colors = [100, 100, 100]  # Set a base color

# Create the mesh data
mesh = go.Mesh(
    x=vertices[:, 0],
    y=vertices[:, 1],
    z=vertices[:, 2],
    i=triangles[:, 0],
    j=triangles[:, 1],
    k=triangles[:, 2],
    vertexcolor=colors,  # Add vertex colors
)

# Create the layout
layout = go.Layout(
    title="Surface from AFNI (.gii file)",
    margin=dict(t=0),  # Adjust top margin for better viewing
)

# Create the figure
fig = go.Figure(data=[mesh], layout=layout)

# Show the plot
fig.show()



