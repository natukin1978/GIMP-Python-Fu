import os
from gimpfu import *

def fill_areas(image, drawable):
    pdb.gimp_edit_fill(drawable, BACKGROUND_FILL)
    pdb.gimp_selection_invert(image)
    pdb.gimp_edit_fill(drawable, FOREGROUND_FILL)
    pdb.gimp_selection_none(image)

    filename = image.filename
    base_dir, basename = os.path.split(filename)
    new_dir = os.path.join(base_dir, "mask_inpaint_face")
    new_filename = os.path.join(new_dir, basename)

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    pdb.gimp_file_save(image, drawable, new_filename, new_filename)
    pdb.gimp_image_clean_all(image)
    pdb.gimp_image_delete(image)

register(
    "fill_areas",
    "Fill selected area with background color, and outside with foreground color",
    "Fill selected area with background color, and outside with foreground color",
    "Your Name",
    "Your Name",
    "2023",
    "<Image>/Filters/MyScripts/Make mask with save",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None),
    ],
    [],
    fill_areas,
    menu="<Image>/Filters/MyScripts")

main()
