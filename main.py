# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:17:44 2019

@author: deepb
"""
# =============================================================================
# TO DO:
# 1. correct the encoding for nearest landmark
# 2. fix mentor data types
# =============================================================================



import pandas as pd
import numpy as np
from person import person


if __name__ ==  '__main__':
    # variables
    mentees_file = 'mentees.xlsx'
    mentors_file = 'mentors.xlsx'
    
    # importing the dataframe
    mentees_df = pd.read_excel(mentees_file)
    mentors_df = pd.read_excel(mentors_file)
    
    mentees = []
    mentors = []
    
    # Data Preprocessing
    
    # Encoding categorical values
    codes = {"Do you identify more as an introvert or an extrovert?" : {"Introvert" : -1, 
                                                                        "Extrovert" : 1},
             "Gender" : {"Male" : 1, "Female" : -1, "Non-binary" : 0},
             "Would you prefer a mentor the same gender as yourself?" : {"I don't mind having a mentor of a different gender" : 0,
                                                                         "Yes": 1},
             "Would you prefer a mentee the same gender as yourself?" : {"I don't mind having a mentee of a different gender" : 0,
                                                                         "Yes": 1},
             "What's your time availability like?" : {"Pretty much free outside of class" : 3, 
                                                      "Occasionally free during the week, but mainly weekends" : 2,
                                                      "Only free during the week" : 1,
                                                      "Only free during weekends" : 0},
             "Which class year are you?" : {"Graduate Student" : 2,
                                            "Senior" : 1,
                                            "Junior" : 0,
                                            "Sophomore" : -1,
                                            "Freshman" : -2},
             "What's the closest landmark to your home?" : {"Northgate" : 0,
                                                            "Park West" : 1,
                                                            "HEB (Texas Avenue, College Station)" : 2,
                                                            "Walmart (Texas Avenue)" : 3,
                                                            "Post Oak Mall" : 4,
                                                            "Downtown Bryan" : 5},
             "How close do you want to be with your mentor?" : {"Talking daily, hanging out multiple times per week" : 2,
                                                                "Talking often, hanging out roughly once per week" : 1,
                                                                "Talking sometimes, hanging out every few weeks" : -1,
                                                                "Talking when necessary, hanging out a few times during the semester" : -2},
             "How close do you want to be with your mentee?" : {"Talking daily, hanging out multiple times per week" : 2,
                                                                "Talking often, hanging out roughly once per week" : 1,
                                                                "Talking sometimes, hanging out every few weeks" : -1,
                                                                "Talking when necessary, hanging out a few times during the semester" : -2}
             }

    mentees_df.replace(codes, inplace = True)
    mentors_df.replace(codes, inplace = True)
    
    # 
    
    
    
    
    
    
    



    

