# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:29:11 2024

@author: seidih6290
"""

names = {
    123: 'Chris', 
    456:'Sussie', 
    789: 'Jessica', 
    963: 'Simon'
}

# scenario 1 , need to print out keys only
print("\nScen 1")



# scenario 2 , need to print out values only
print("\nScen 2")


# scenario 3 , need to print out both
print("\nScen 3")


    
# different dict, dict that has a nested dict

grades = {
    'Chris': {
        "Math": 87,
        "Sci":  99
    },
    'Sussie': {
        "Math": 77,
        "Sci":  70
    },
    'Jessica': {
        "Math": 100,
        "Sci":  99
    },
    'Simon': {
        "Math": 80,
        "Sci":  79
    }
}
# retrive the name and scores for each student and display in same line
print("\nScen 4") 





#scenaria 5 dict with nested list of dictionaries
students = {'Grade 4': [
    {"Student_name":"Chris","Math":87,"Sci": 99},
    {"Student_name":"Sussie","Math":88,"Sci": 100},
    {"Student_name":"George","Math":67,"Sci": 90}
    ],
    'Grade 5': [
    {"Student_name":"Jessica","Math":70,"Sci": 79},
    {"Student_name":"Simon","Math":80,"Sci": 80}
    ]}
print("\nScen 5")
'''display the following ( grade , student name, math and sci scores ) for each element in the nested dictionary
content for each element is to be displayed on the same line '''




