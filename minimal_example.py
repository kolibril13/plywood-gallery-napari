# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "napari[all]",
#     "scikit-image",
# ]
# ///


# import sample data
from skimage.data import cells3d

import napari

# create a `Viewer` and `Image` layer here
viewer, image_layer = napari.imshow(cells3d())

# print shape of image datas
print(image_layer.data.shape)

# start the event loop and show the viewer
napari.run()

# header of this script was generated with uv add --script foo.py scikit-image "napari[all]"ion_Modern