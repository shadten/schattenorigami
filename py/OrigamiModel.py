# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:45:21 2023

@author: Manuel
"""
import warnings
from create_artwork_page import create_artwork_page_from_model
    

class OrigamiModel():
    __tag_list__ = ["22.5&deg", "box-pleated", "circle-packed", "color change",
                    "humanoid", "animal", "legendary creature", "spider", "insect", "object"]
    
    __artwork_pages_dir__ = "/schattenorigami/artwork_pages/"
    __CPs_dir__ = "/schattenorigami/assets/CPs/"
    __artwork_imgs_dir__ = "/schattenorigami/assets/artwork_imgs/"

    def __init__(self, name, tags,
                 version_titles, captions, nums_of_imgs, dates, papers, times,
                 grids, trivias, notes,  
                 cps, diagrams,
                 cp_file_extension="png", imgs_file_extension = "jpeg"):
        """
        Parameters
        ----------
        name : str
            Name of the model.
        tags : list of str
            List of tags. See tag_ist for all possible tags.
        version_titles : list of str
            List of the titles of different versions of this model.
            Must be of the form i,j (eg. 1.0, 2.1, etc)  
        captions : list of of list str
            List of the captions for each version. Paragraphs as different elements of a list.
        nums_of_imgs: list of int
            The number of images for each version.
        dates : list of str
            List of dates of each version.
        papers : list of str
            List of the paper used for each version
        times : list of str
            List of the times for each version
        grids : list of None or str
            List of grids for each version.
            If None, then no grid for the corresponding versions.
        trivias : list of None or str
            List of trivias for each model.
            If None, then no trivia for the corresponding versions.
        notes : list of None or str
            List of notes for each version.
            If NONE, then no note for the corresponding versions.
        cps : list of bool
            Whether the CP is available for each version
        diagrams : list of bool
            Whether diagrams are available for each version.
        cp_file_extension: str
            The file type of the CP of all versions.
        imgs_file_extension: str
            The file type of all images.
        """
                
        # check if tags are valid
        for tag in tags:
            if not tag in OrigamiModel.__tag_list__:
                raise ValueError(f"The tag '{tag}' is not in the tag_list.")
        
        # check if all paramter lengths are valid
        for k, v in zip(["captions", "dates", "papers", "times", "trivias", "notes", "grids", "cps", "diagrams"], 
                        [captions, dates, papers, times, trivias, notes, grids, cps, diagrams]):
            if v is not None and len(v) != len(version_titles):
                raise ValueError(f"Number of {k} ({len(v)}) does not match number "
                                 f"of versions ({len(version_titles)})")

        self.name = name
        self.tags = tags
        self.version_titles = version_titles
        self.captions = captions
        self.nums_of_imgs = nums_of_imgs
        self.dates = dates
        self.dates_num = [get_numeric_date(date) for date in self.dates]
        self.papers = papers
        self.times = times
        self.grids = grids
        self.trivias = trivias
        self.notes = notes
        self.cps = cps 
        self.diagrams = diagrams
        
        self.num_of_versions = len(version_titles)
        self.cp_file_extension = cp_file_extension
        self.imgs_file_extension = imgs_file_extension
        
        self.name_snake = self.name.lower().replace(' ', '_')
        self.artwork_page_path = OrigamiModel.__artwork_pages_dir__ + self.name_snake + ".html"
        self.cp_paths = self.__get_cp_paths__()
        self.img_paths = self.__get_img_paths__()

        self.tags.sort()
        
    def __get_cp_paths__(self):
        arr = []
        for version_title in self.version_titles:
            i, j = version_title.split('.')
            arr.append(OrigamiModel.__CPs_dir__ + f"{self.name_snake}_v{i}_{j}_cp.{self.cp_file_extension}")
        return arr
    
    def __get_img_paths__(self):
        res = []
        for v, version_title in enumerate(self.version_titles):
            i, j = version_title.split('.')
            arr = []
            for num in range(1, self.nums_of_imgs[v] + 1):
                arr.append(OrigamiModel.__artwork_imgs_dir__ + f"{self.name_snake}_v{i}_{j}_img{num}.{self.imgs_file_extension}")
            res.append(arr)
        return res
    
    def add_new_version(self, other):
        if not isinstance(other, OrigamiModel):
            raise ValueError(f"Cannot add object of type '{type(other)}' to "
                             f"OrigamiModel '{self.name}'.")
        if self.name != other.name:
            raise ValueError(f"Cannot add OrigamiModel by name '{other.name}' "
                             f"to OrigamiModel by name '{self.name}'. "
                             "They need to have the same name.")
        if self.cp_file_extension != other.cp_file_extension:
            raise ValueError(f"Cannot add OrigamiModels '{other.name}' with "
                             f"different CP file extensions ({other.cp_file_extension} "
                             f"and {self.cp_file_extension}.)")
        if self.imgs_file_extension != other.imgs_file_extension:
            raise ValueError(f"Cannot add OrigamiModels '{other.name}' with "
                             f"different image file extensions ({other.imgs_file_extension} "
                             f"and {self.imgs_file_extension}.)")
        
        if other.num_of_versions > 1:
            warnings.warn(f"Adding add OrigamiModel by name '{other.name}' "
                          f"with more than one version ({other.num_of_versions}) "
                          f"to OrigamiModel by name '{self.name}'.")
        if other.tags != self.tags:
            warnings.warn(f"Adding OrigamiModel by name '{other.name}' to OrigamiModel "
                          f"by name '{self.name}' with different tags. The tags "
                          f"of '{other.name}' will be lost")
            
        self.version_titles = other.version_titles + self.version_titles
        self.captions = other.captions + self.captions
        self.nums_of_imgs = other.nums_of_imgs + self.nums_of_imgs
        self.dates = other.dates + self.dates
        self.dates_num = other.dates_num + self.dates_num
        self.papers = other.papers + self.papers
        self.times = other.times + self.times
        self.grids = other.grids + self.grids
        self.trivias = other.trivias + self.trivias
        self.notes = other.notes + self.notes
        self.cps = other.cps + self.cps 
        self.diagrams = other.diagrams + self.diagrams
        
        self.num_of_versions = len(self.version_titles)

        self.cp_paths = other.cp_paths + self.cp_paths
        self.img_paths = other.img_paths + self.img_paths
    
    def to_dict(self):
        return self.__dict__
    
    # to allow sort() for the Catalogue class
    def __lt__(self, other):
        return self.name < other.name
       
    def create_artwork_page(self):
        create_artwork_page_from_model(self)


def init_model_from_dict(model_dict):
    name = model_dict["name"]
    tags = model_dict["tags"]
    version_titles = model_dict["version_titles"]
    captions= model_dict["captions"]
    nums_of_imgs = model_dict["nums_of_imgs"]
    dates = model_dict["dates"]
    papers = model_dict["papers"]
    times = model_dict["times"]
    grids = model_dict["grids"]
    trivias = model_dict["trivias"]
    notes = model_dict["notes"]
    cps = model_dict["cps"]
    diagrams = model_dict["diagrams"]
    cp_file_extension = model_dict["cp_file_extension"]
    imgs_file_extension = model_dict["imgs_file_extension"]
    
    return OrigamiModel(name, tags,
                        version_titles, captions, nums_of_imgs, dates, papers, times,
                        grids, trivias, notes,
                        cps, diagrams,
                        cp_file_extension, imgs_file_extension)     

    # return OrigamiModel(*model_dict.values())

def get_numeric_date(date):
    months = ["January", "February", "March", "April", "May", "June", "July", 
              "August", "September", "October", "November", "December"]
    month, year = date.split(' ')[:2]
    if not month in months:
        raise ValueError("date must be of the form 'Month yyyy'")
    
    return f"{year}-{months.index(month)+1}"

