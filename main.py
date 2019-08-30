# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:17:44 2019

@author: deepb
"""
# =============================================================================
# TO DO:
# 1. drop na
# =============================================================================



import pandas as pd
from person import Person


if __name__ ==  '__main__':
    # variables
    mentees_file = 'mentees.xlsx'
    mentors_file = 'mentors.xlsx'
    
    # importing the dataframe
    mentees_df = pd.read_excel(mentees_file)
    mentors_df = pd.read_excel(mentors_file)
    
    # Cleaning nan values
    mentees_df.dropna(subset = ["Name", "Gender"], inplace = True)
    mentors_df.dropna(subset = ["Name", "Gender"], inplace = True)
    
    # Initializing list of objects
    mentees = [None for i in range(mentees_df.shape[0])]
    mentors = [None for i in range(mentors_df.shape[0])]
    
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
    
    # Scaling values
    mentors_df["Do you like to stay inside (hanging out, reading, watching TV/movies, playing video games etc.)?"] -= 3
    mentors_df["Do you like to be outside (playing sports, exercising, running, hiking etc.)?"] -= 3
    mentors_df["Do you like to go out and be social (hanging out with friends, going to parties, etc.)? "] -= 3
    mentors_df["How much would you like to travel outside of College Station this semester?"] -= 3
    mentors_df["Do you like going to sports games?"] -= 3
    
    mentees_df["Do you like to stay inside (hanging out, reading, watching TV/movies, playing video games etc.)?"] -= 3
    mentees_df["Do you like to be outside (playing sports, exercising, running, hiking etc.)?"] -= 3
    mentees_df["Do you like to go out and be social (hanging out with friends, going to parties, etc.)? "] -= 3
    mentees_df["How much would you like to travel outside of College Station this semester?"] -= 3
    mentees_df["Do you like going to sports games?"] -= 3
    
    
    # Initialize objects
    for i, row in enumerate(mentees_df.values):
        name, languages, social, gender, gender_preference, time, year,\
        landmark, inside, outside, go_out, travel, sports, close = row
        
        mentees[i] = Person(name, languages, social, gender, gender_preference, time, year,
                           landmark, inside, outside, go_out, travel, sports, close)
        

    for i, row in enumerate(mentors_df.values):
         name, languages, social, gender, gender_preference, time, year,\
         landmark, inside, outside, go_out, travel, sports, close = row
         
         mentors[i] = Person(name, languages, social, gender, gender_preference, time, year,
                            landmark, inside, outside, go_out, travel, sports, close)

    # Initializing the dataframe
    scores_df = pd.DataFrame(columns = [mentee.name for mentee in mentees], 
                                  index = [mentor.name for mentor in mentors])
    
    # Dictionary to hold the distance scores
    distance_scores = {"Northgate" : {"Northgate" : 10, "Park West" : 7, "HEB (Texas Avenue, College Station)" : 6,
                                      "Walmart (Texas Avenue)" : 4, "Post Oak Mall" : 4, "Downtown Bryan" : 4},
                       "Park West" : {"Northgate" : 7, "Park West" : 10, "HEB (Texas Avenue, College Station)" : 7,
                                      "Walmart (Texas Avenue)" : 5, "Post Oak Mall" : 4, "Downtown Bryan" : 1},
                       "HEB (Texas Avenue, College Station)" : {"Northgate" : 6, "Park West" : 7, "HEB (Texas Avenue, College Station)" : 10,
                                      "Walmart (Texas Avenue)" : 8, "Post Oak Mall" : 8, "Downtown Bryan" : 2},
                       "Walmart (Texas Avenue)" : {"Northgate" : 4, "Park West" : 5, "HEB (Texas Avenue, College Station)" : 8,
                                      "Walmart (Texas Avenue)" : 10, "Post Oak Mall" : 6, "Downtown Bryan" : 0},
                       "Post Oak Mall" : {"Northgate" : 4, "Park West" : 4, "HEB (Texas Avenue, College Station)" : 8,
                                      "Walmart (Texas Avenue)" : 6, "Post Oak Mall" : 10, "Downtown Bryan" : 1},
                       "Downtown Brayan" : {"Northgate" : 4, "Park West" : 1, "HEB (Texas Avenue, College Station)" : 2,
                                      "Walmart (Texas Avenue)" : 0, "Post Oak Mall" : 1, "Downtown Bryan" : 10}}
    
    # Calculate the scores
    for mentor in mentors:
        for mentee in mentees:
            # Introversion/Extroversion
            social_score = mentor.social * mentee.social + 4
            
            # class year
            year_score = mentor.year * mentee.year + 6
            
            # stay inside
            inside_score = mentor.inside * mentee.inside + 4
            
            # stay outside
            outside_score = mentor.outside * mentee.outside + 4
            
            #  go_out
            go_out_score = mentor.go_out * mentee.go_out + 4
            
            #  travel
            travel_score = mentor.travel * mentee.travel + 4
            
            #  sports
            sports_score = mentor.sports * mentee.sports + 4
            
            # close
            close_score = mentor.close * mentee.close + 4
            
            # distance
            distance_score = distance_scores[mentor.landmark][mentee.landmark]
            
            # Boolean flags
            if (mentee.gender_preference or mentor.gender_preference) and mentor.gender != mentee.gender:
                total_score = 0
            elif mentee.time + mentor.time == 1:
                total_score = 0
            else:
                total_score = social_score + year_score + inside_score + outside_score + go_out_score\
                               + travel_score + sports_score + close_score + distance_score
                             
            scores_df.loc[mentor.name, mentee.name] = int(total_score)
            
    # Getting the closest match
    closest_df = pd.DataFrame(columns = ["Mentee", "Score"], index = [mentor.name for mentor in mentors])
    closest_df["Mentee"] = scores_df.idxmax(axis=1)
    closest_df["Score"] = scores_df.max(axis=1)
    
    # Exporting the dataframes
    
    
    
    
            
                
                                                       


    
            
            
            
            
            
    
        
    
    
    
    
    
    
    



    

