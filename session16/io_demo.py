import os

# print(os.getcwd())

# fout = open('data/output.txt', 'w')
# line1 = "How many roads must a man walk down\n"
# fout.write(line1)
# line2 = "Before you call him a man?\n"
# fout.write(line2)
# fout.close()

# context manager
# with open('data/output.txt', 'w') as fout:
#     line1 = "How many roads must a man walk down\n"
#     fout.write(line1)
#     line2 = "Before you call him a man?\n"
#     fout.write(line2)


# try:
#     f = open("data/output3.txt")
#     print(f.readlines())
# except:
#     print("This could be a trouble. Let's just move on!")


# print('hello')


import pickle

t = [1, 2, 3]

with open('data/saved_pickle.p', 'wb') as p:
    pickle.dump(t, p)
