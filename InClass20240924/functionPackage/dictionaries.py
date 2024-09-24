# dictionaries.py

from heapq import merge
from hmac import new
from multiprocessing import Value
from optparse import Values
from turtle import clear


def demo():
    """
    Demonstrate basica dictionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    # Iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)
   
    # Iterate by value
    for item in myDictionary.items():
        print(item)
        
    # Iterate by value 
    for value in myDictionary.values():
        print(value)
        
    # Add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartains"
    
    print(len(myDictionary))
    
    # Cause an exception. Add try / except logic to
    # Gracfully handle this
    try:
         print(myDictionary["Ohio State"])
    except:
        # We end up here if exceptio is throw
        # in the try block
        print("Ohio State is an invalid key!")
        
    # Remove Xavier by key and print the entire dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)
    
    # Create another dictionary called newTeams.
    # Add several key/value pairs
    # Combine that with myDictionary and print the results
    newTeams = {"Boston":"Celtics","Brooklyn":"Nets","Los Angeles":"Lakers","Orlando":"Magic","Detroit":"Pistons"}
    
    # Brute Force
    #for key in newTeams.keys():
    #    myDictionary[key] = newTeams[key]
    #print(myDictionary)
    
    #myKey.update is muchhh more elegant
    myDictionary.update(newTeams)
    print(myDictionary)
