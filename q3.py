import numpy as np

vector1 = np.array([1,2,-1])
vector2 = np.array([1,2,1])
A = np.array([[-2,1,4],[1,1,1],[4,1,-2]])

def n(vector):
    x=np.linalg.norm(vector)
    y=vector/x
    return y

for i in range(5):
    vector1 = np.dot(A, vector1)
    vector1=n(vector1)

    value1=np.dot(np.transpose(vector1),A)
    value1=np.dot(value1,vector1)

    print('1. eigenvector, iteration', i+1,":", vector1)
    print('1. eigenvalue, iteration',i+1, ":",value1)
    print("")

print("----------------")

for i in range(5):
    vector2 = np.dot(A, vector2)
    vector2=n(vector2)

    value2=np.dot(np.transpose(vector2),A)
    value2=np.dot(value2,vector2)

    print('2. eigenvector, iteration',i+1, ":", vector2)
    print('2. eigenvalue, iteration', i+1,":",value2)
    print("")
