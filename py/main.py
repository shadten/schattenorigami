# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:59:07 2023

@author: Manuel
"""
from OrigamiModel import OrigamiModel
from Catalogue import load_catalogue_from_json

# ----- MODEL PARAMETERS HERE -----
name = "Pholcus phalangioides" # str
tags = ["box-pleated", "spider"] # str
version_titles = ["1.0"] # str
captions = [
    [
         "Honestly, this model was quite a handful.",
         "Initially I wanted to design a simple little model of a not-too-detailed little spider.",
         "But in order to make the legs very long relative to the body, I had to make the body very small. That resulted in a lot of excess paper which, because I didn't want to waste it, led me to give the spider some eggs to take care of. In the end, the model turned out way more tedious to fold than I anticipated and the collapse with single tissue was a mess.",
         "Meanwhile I almost had a mental breakdown* spending an unreasonably huge amount of time fixing errors in the CP where there weren't any, because ORIPA went insane.",
         "Fortunately, it all turned out ok in the end, so I'm counting that as a win."
    ],
] # str 
nums_of_imgs = [2] # int
dates= ["August 2020"] # str
papers = ["34 cm square of single tissue"] # str
times = ["~4 hours"] # str
grids = None # None or str
trivias = [None] # str
notes = ["Diagonal reference line (light blue) at 22.5° through the center, gray corners folded inwards"] # str
cps = [True] # bool
diagrams = [False] # bool

cp_file_extension="png"
imgs_file_extension="jpg"

# ----- FLAGS -----
do_new_model = True# bool
do_new_version = False# bool
























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
