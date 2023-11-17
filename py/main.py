# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:59:07 2023

@author: Manuel
"""
from OrigamiModel import OrigamiModel
from Catalogue import load_catalogue_from_json

# ----- MODEL PARAMETERS HERE -----
name = "Light up your path" # str
tags = ["box-pleated", "humanoid"] # str
version_titles = ["1.0"] # str
captions = [
    [
         "One of the reasons why I love origami, and particularly designing my own models, is because you can make any vision and idea become real.",
         "The structure is a variation of my model 'my best friend'. I made use of the paper on the lower right corner (creating a ribbon), so it's more efficient.",
         "Aimed a flashlight at the lantern to make it look like it's glowing (which turned out being trickier than I thought it would be)."
         
    ],
] # list of str   
nums_of_imgs = [2] # int
dates= ["June 2019"] # str
papers = ["30 cm square of wenzhou rice paper"] # str
times = ["~6 hours"] # str
grids = ["42x42"] # None or str
trivias = [None] # None or str
notes = [None] # str
cps = [True] # bool
diagrams = [False] # bool

cp_file_extension = "png"
imgs_file_extension = "jpg"

# ----- FLAGS -----
do_new_model = True # bool
do_new_version = False # bool
























# -----------------------------------------------------------------------------
# ----- DO THE STUFF -----
if do_new_version == do_new_model:
    raise ValueError("Flags don't work out. Exactly one of them has to be set true")
    
model = OrigamiModel(name, tags,
                     version_titles, captions, nums_of_imgs, dates, papers, times,
                     grids,
                     trivias, notes,
                     cps, diagrams,
                     cp_file_extension=cp_file_extension, imgs_file_extension=imgs_file_extension)
artworks = load_catalogue_from_json("../artworks.json")

if do_new_model:
    artworks.add_model(model)
else:
    artworks.add_new_version(model)

artworks.save_to_json()
artworks.get_model_by_name(model.name).create_artwork_page()
