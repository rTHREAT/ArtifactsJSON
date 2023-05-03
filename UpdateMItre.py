import json
import glob

for filename in glob.glob('*.json'):
    jsonFile = open(filename, "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    data["versions"]["attack"]  = "13"
    data["versions"]["navigator"]  = "4.8.1"
    data["versions"]["layer"]  = "4.4"

    jsonFile = open(filename, "w")
    jsonFile.write(json.dumps(data,indent=8))
    jsonFile.close()
