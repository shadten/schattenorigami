# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:59:07 2023

@author: Manuel
"""
from OrigamiModel import OrigamiModel
from Catalogue import load_catalogue_from_json

# ----- MODEL PARAMETERS HERE -----
name = "My best friend" # str
tags = ["box-pleated", "humanoid", "color change"] # str
version_titles = ["2.0", "1.0"] # str
captions = [
    [
        "I finally took the time to revise this model. There's still a lot of room for improvements so I'll go back to it every once a while.",
        "This model was originally named 'My best friend' v.2', as it is a simple revision of the previos version. After someone made the suggestion on the original instagram post-LINK-, I changed the name to 'Sadako' as a tribute to Sadako Sasaki. The Wikipedia-LINK- article reads:",
        "Sadako Sasaki [...] was a Japanese girl who was 2 years old when an American atomic bomb was dropped on Hiroshima on August 6, 1945, near her home next to the Misasa Bridge but survived. Sasaki became one of the most widely known hibakusha---a Japanese term meaning \"bomb-affected person\". She is remembered through the story of the one thousand origami cranes she folded before her death, and is to this day a symbol of the innocent victims of nuclear warfare."
    ],
    [
        "I had the idea of designing a person holding a traditional crane some time ago, but wasn't able to do it; I'm glad to say I was able to now!",
        "I adopted the head (with slight variations) from Chen Xiao's 'walking in the rain', since I really liked it. I'll probabaly use it again in future designs.",
        "The third picture shows a refold of the design to see what it looks like with a different shaping."
    ]

] # list of str   
nums_of_imgs = [2, 3] # int
dates= ["August 2019", "October 2018"] # str
papers = ["35 cm square of double tissue", "30-35 cm square of double tissue"] # str
times = ["~8 hours", "~4 hours"] # str
grids = ["50x50", "42x42"] # None or str
trivias = ["Originally titled 'My best friend v.2'", None] # None or str
notes = [None, None] # str
cps = [True, True] # bool
diagrams = [False, False] # bool

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
