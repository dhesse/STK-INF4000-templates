import unittest
import requests

class ServerTests(unittest.TestCase):
    def test_get_json(self):
        json = requests.get('http://localhost:5000/data.json').json()
        knwon_json = { "x": { "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
                              "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                              "10": 10, "11": 11, "12": 12, "13": 13,
                              "14": 14, "15": 15, "16": 16, "17": 17,
                              "18": 18, "19": 19 },
                       "y": { "0": 0.32797344, "1": 0.24651086, "2":
                              2.48196793, "3": 2.15542269, "4":
                              3.85308687, "5": 5.34399642, "6":
                              6.20893099, "7": 5.67906586, "8":
                              9.18233268, "9": 9.44169552, "10":
                              10.33510592, "11": 11.75765219, "12":
                              12.46384419, "13": 12.48009362, "14":
                              14.39153645, "15": 15.12273801, "16":
                              16.24443402, "17": 16.54217248, "18":
                              17.49921914, "19": 18.613513 } }
        self.assertEqual(json, knwon_json)

    def test_predict(self):
        json = requests.get('http://localhost:5000/predict.json').json()
        knwon_json = [
            19.991856164578955, 
            20.98931250272933, 
            21.986768840879705
        ]
        self.assertEqual(json, knwon_json)
             
