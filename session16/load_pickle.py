import pickle

with open('data/saved_pickle.p', 'rb') as p:
    t = pickle.load(p)


print(t)
print(type(t))
