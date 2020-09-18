''' This file generates a json file to be read by car_trouble.py '''

import json

T = True
F = False

t1 = ('IW', [], 0.2)
t2 = ('G', [], 0.9)
t3 = ('B', ['IW'], {T: 0.6, F: 0.9})
t4 = ('SM', ['IW'], {T: 0.5, F: 0.9})
t5 = ('R', ['B'], {T: 0.9, F: 0.1})
t6 = ('I', ['B'], {T: 0.9, F: 0.2})
t7 = ('S', ['I', 'SM', 'G'],{'TTT': 0.9, 'TTF': 0.5, 'TFT': 0.2, 'TFF': 0.1, 'FTT': 0.15, 'FTF': 0.1, 'FFT': 0.05, 'FFF': 0.01})
t8 = ('M', ['S'], {T: 0.99, F: 0.01})

li = [t1,t2,t3,t4,t5,t6,t7,t8]

with open('probabilities.json', 'w') as outfile:
    json.dump(li, outfile)
    print(li)







