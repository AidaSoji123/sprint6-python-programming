import json
# Python dictionary converts to json string using dumps method
# pyhton_dict = {
#     "Name": "Aida",
#     "Age" : 28,
#     "Course Name" : "Python django"
# }
# json_string = json.dumps(pyhton_dict)
# print(json_string) 
    
    

with open("jsonparsing/data.json") as f:
    pyhton_dict = json.load(f)  
    print(pyhton_dict)