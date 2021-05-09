import numpy
from scipy import linalg
import matplotlib.pyplot as pyplot



def SVD(image, a):
   
    U, s_values, V = numpy.linalg.svd(image)

    S = numpy.diag(s_values)
    S = S[:a,:a]

    U = U[:,:a] 
    V = V[:a,:]

    SVD_value_1=numpy.dot(U, S)
    SVD_value_2=numpy.dot(SVD_value_1, V)
    
    return SVD_value_2


image = pyplot.imread("clown.bmp")

iteration=1
range=2
figure_1 = pyplot.figure()

while range < 128:

    compressed = SVD(image, range)
    figure_1.add_subplot(3, 2, iteration)

    pyplot.imshow(compressed, cmap = "gray")


    iteration += 1
    range *= 2

pyplot.show()
figure_1.savefig("clown_svd.png")
pyplot.close()