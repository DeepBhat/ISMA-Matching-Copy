# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:56:16 2019

@author: deepb
"""

class Person:
    def __init__(self, name: str, languages: str, social: int, gender: int, gender_preference: int,\
                 time: int, year: int, landmark: int, inside: int, outside: int,\
                 go_out: int, travel: int, sports: int, close: int):
        self.name = name # full name
        self.languages = languages # languages spoken
        self.social = social # introvert or extrovert
        self.gender = gender # male, female, nb
        self.gender_preference = gender_preference # yes or no (for same mentor)
        
        self.time = time # time available - 1,2,3,4
        self.year = year # class year - 1,2,3,4,5
        self.landmark = landmark # closest landmark (encode)
        
        # Linear Scale personality
        self.inside = inside # spend time inside
        self.outside = outside # spend time outside
        self.go_out = go_out # love to socialize
        self.travel = travel # travel outside cstat
        self.sports = sports # watch sports
        self.close = close # how close to mentor
        
    