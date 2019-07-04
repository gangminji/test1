import pickle

with open('data.pickle",'wb') as fw:
    with open('test.csv','r') as fr:
        for line in fr:
            l=line.strip().split(",")
            if l[2] == "Herpes":
                pickle.dump(l,fw)
