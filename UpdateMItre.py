import json
import glob

for filename in glob.glob('*.json'):
    jsonFile = open(filename, "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    data["versions"]["attack"]  = "9"
    data["versions"]["navigator"]  = "4.3"
    data["versions"]["layer"]  = "4.2"

    jsonFile = open(filename, "w")
    jsonFile.write(json.dumps(data,indent=8))
    jsonFile.close()