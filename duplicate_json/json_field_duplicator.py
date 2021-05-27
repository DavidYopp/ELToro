import json

"""
This script takes in the spacex twitter json file generated from our
twitter_gitter.py script and duplicates a field, writing the output back
to a json file named duplicate_json_field.json
"""

# open our json file in read mode and set it to handy variable jsonInputFile
jsonInputFile = open('spacex_popular_tweet.json', "r")

#read the data into a variable named jsondata
#the json.loads takes the file and makes it a python dict object
jsonData = json.loads(jsonInputFile.read())

#this variable will be used to hold the dict items that we pass over
#this is so that when we find our json field we are looking for
#we can prepend it back to the jsonData dict
passedOverItemsDict = {}

#a variable to specify which field you would like to duplicate
fieldToDuplicate = 'id'

#this for loop will iterate over the fields within the status section of the
#json data. It will only traverse this level of the json tree to find the
#fieldToDuplicate that was specified
for k, v in jsonData['statuses'][0].items():
    #looks for the field to duplicate by traversing over the key value pairs
    #if the key is equal to the field we are looking for...
    if k == fieldToDuplicate:
        #first add the field (key and value prepended with _ to the passedOverItemsDict
        passedOverItemsDict['_'+k] = v
        #use the .update function to basically merge the two dictionaries
        #putting the new values first (any fields that are the same will remain)
        passedOverItemsDict.update(jsonData['statuses'][0])
        #write the newly modified data to the same location that it was originally held
        jsonData['statuses'][0] = passedOverItemsDict
        #break out of the loop
        break
    #else just write the key value pair of the nonmatching field to the pass over dict.
    else:
        passedOverItemsDict[k] = v

#finally we write our newly modified json data out to a .json file
#the file is called duplicate_json_field.json and will be in the current
#working directory
with open('duplicate_json_field.json', 'w', encoding='utf-8') as f:
    json.dump(jsonData, f, ensure_ascii=False, indent=4)
