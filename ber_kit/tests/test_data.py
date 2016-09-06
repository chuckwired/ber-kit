import json

#TODO: Add required data for the tests

class DrainData():
    all_apps = json.loads("""{"apps": [ {"id": "/service1", "instances": 1 } ] }""")

class UndrainData():
    all_apps = json.loads("""{}""")
