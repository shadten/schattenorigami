# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:39:39 2023

@author: Manuel
"""
import json
from OrigamiModel import OrigamiModel, init_model_from_dict


class OrigamiModelEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, OrigamiModel):
            return obj.to_dict()
        return json.JSONEncoder.default(self, obj)   


class Catalogue():
    def __init__(self, name, model_list, savefile, no_duplicates=True):
        """
        Parameters
        ----------
        name: str
            The name of the Catalogue.
        model_list : list of OrigamiModel
            The models included in the Catalogue.
        savefile : str
            name of the json file to save to. Must end with '.json'.
        no_duplicates: bool
            If true, then Catalogue.add_model raises an error if a model is
            tried to be added with an name that already exists in the Catalogue.
        """
        if not isinstance(model_list, list):
            raise ValueError("Catalogue instance must be initialized with a list")
        self.name = name
        self.model_list = model_list
        self.__sort_models__()
        self.model_names = [model.name for model in self.model_list]
        self.no_duplicates = no_duplicates
        self.savefile = savefile

    def __sort_models__(self):
        self.model_list.sort()
    
    def __update_model_names__(self):
        self.model_names = [model.name for model in self.model_list]
    
    def add_model(self, model):
        if isinstance(model, OrigamiModel):
            if self.no_duplicates and model.name in self.model_names:
                raise ValueError(f"The model '{model.name}' does already exist "
                                 f"in the catalogue '{self.name}'")
            self.model_list.append(model)
            self.__sort_models__()
            self.__update_model_names__()
        else:
            raise ValueError(f"Cannot add object of type '{type(model)} to a "
                             "Catalogue'. It must be of type OrigamiModel.")
    
    def add_new_version(self, model):
        if isinstance(model, OrigamiModel):
            if model.name in self.model_names:
                self.get_model_by_name(model.name).add_new_version(model)
            else:
                raise ValueError(f"No model named '{model.name}' in Catalogue '{self.name}'")
        else:
            raise ValueError(f"Cannot add object of type '{type(model)}' to a "
                             "Catalogue. It must be of type OrigamiModel.")
    
    def remove_model(self, model_name):
        if model_name in self.model_names:
            model = self.get_model_by_name(model_name)
            print(model)
            self.model_list.remove(model)
            self.__update_model_names__()
            print(f"Successfully removed OrigamiModel '{model_name}' from "
                  f"Catalogue '{self.name}'. This change IS NOT YET SAVED. Use .save_to_json to save it. "
                  "And check if there exists a html artwork page that need to be removed as well.")
        else:
            raise ValueError(f"Model by name '{model_name}' does not exist in "
                             f"catalogue '{self.name}'.")
    
    def get_model_by_name(self, model_name):
        for model in self.model_list:
            if model.name == model_name:
                return model
    
    def to_dict(self):
        return self.__dict__

    def save_to_json(self):
        with open(self.savefile, "w+") as sf:
            json.dump(self.to_dict(), sf, indent=4, cls=OrigamiModelEncoder)
            

def load_catalogue_from_json(savefile):
    with open(savefile, "r") as sf:
        cat_dict = json.load(sf)

    return Catalogue(
        cat_dict["name"],
        [init_model_from_dict(model_dict) for model_dict in cat_dict["model_list"]],
        savefile)
                
    