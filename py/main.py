# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:59:07 2023

@author: Manuel
"""
from OrigamiModel import OrigamiModel
from Catalogue import load_catalogue_from_json

# ----- MODEL PARAMETERS HERE -----
name = "Cyclommatus metallifer" # str
tags = ["box-pleated", "insect"] # str
version_titles = ["1.2", "1.1", "1.0"] # str
captions = [
    [
         "I changed the scutellum (the little triangle on the back) of the beetle a bit so it's narrower compared to the previous version and made some other small revisions."
    ],
    [
         "A refold of my original design. I made some slight changes to the cp and tried to give it an overall better shaping."
    ],
    [
        "There are a lot of origami models of this particular beetle, so I thought I could give it a try as well and I'm pretty happy with how it turned out!" 
    ]
] # list of str   
nums_of_imgs = [5, 4, 3] # int
dates= ["September 2019", "April 2019", "January 2019"] # str
papers = ["33 cm square of double tissue", "30 cm square of double tissue", "30 cm square of double tissue"] # str
times = ["~6.5 hours", "~8 hours", "~5 hours"] # str
grids = ["48x48 with"]*3 # None or str
trivias = ["This model (which I submitted along with my Redback Spider) won Paper for Water's BugBattle contest in the original design category.", None, None] # None or str
notes = ["Additional details shown only on the left half of the CP"]*3 # str
cps = [True, True, True] # bool
diagrams = [False, False, False] # bool

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
