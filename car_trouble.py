''' This program makes use of the aima-python github repo. 
    Specifically it uses 'probability4e.ipynb' -> ('prob.py') '''

# Example query: IW=true,B=false,R=false

from prob import *

T = True
F = False

def convert_elem(elem):
    if elem == 'true': return T
    if elem == 'false': return F
    if elem == 'TTT': return (T, T, T)
    if elem == 'TTF': return (T, T, F)
    if elem == 'TFT': return (T, F, T)
    if elem == 'TFF': return (T, F, F)
    if elem == 'FTT': return (F, T, T)
    if elem == 'FTF': return (F, T, F)
    if elem == 'FFT': return (F, F, T)
    if elem == 'FFF': return (F, F, F)
    return elem

def convert_dict(bool_dict, keys):
    cdict = {}
    for elem in bool_dict:
        cdict[convert_elem(elem)] = bool_dict[elem] 
    return cdict

def get_prob():
    import json
    f = open('probabilities.json')
    data = json.load(f)
    f.close()
    return data

def get_bn():
    bn = BayesNet() 
    prob = get_prob()
    for node in prob:
        if isinstance(node[2], dict):
            bn.add(node[0], node[1], convert_dict(node[2], node[2].keys()))
        else:
            bn.add(node[0], node[1], node[2])
    return bn


def get_variable(name, bn):
    prob = get_prob()
    if name == prob[0][0]:
        return bn.variables[0]
    if name == prob[1][0]:
        return bn.variables[1]
    if name == prob[2][0]:
        return bn.variables[2]
    if name == prob[3][0]:
        return bn.variables[3]
    if name == prob[4][0]:
        return bn.variables[4]
    if name == prob[5][0]:
        return bn.variables[5]
    if name == prob[6][0]:
        return bn.variables[6]
    if name == prob[7][0]:
        return bn.variables[7]
    else:
        raise Exception("No such variable: {}".format(name))
             
def get_evidence(nodes, vals, bn):
    d = {}
    i = 0
    for n in nodes:
        node = get_variable(n, bn)
        d[node] = vals[i]
        i = i+1
    return d

def calc_prob(bn, evidence):
    ans = 0
    for (row, p) in joint_distribution(bn).items():
        if matches_evidence(row, evidence, bn):
            ans = ans + p
    return ans


def main():
    prob = get_prob
    bn = get_bn()
    query_nodes = []
    query_vals = []

    q = input("Enter your query: ")
    q = q.split(",")
    for cond in q:
        cond_split = cond.split("=")
        query_nodes.append(cond_split[0])
        if cond_split[1] == "true":
            val = True
        else:
            val = False
        query_vals.append(val)

    e = get_evidence(query_nodes, query_vals, bn)
    print(calc_prob(bn, e))


main()


