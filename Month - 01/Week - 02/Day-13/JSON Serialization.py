'''
DEEP DIVE: 13.5 Micro-Challenge: JSON Serialization
Goal: Save a dictionary to a file. 
Deep Dive: json.dump(). JSON is the standard for data exchange. 
Note: JSON keys must be strings; Python allows integers, but JSON 
converts them.
'''

import json

data = {
    1: "Apple",
    2: "Banana",
    "price": 50,
    "available": True
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
