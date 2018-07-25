from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

import kmedoids
import random
import math

import sys

# 3 points in dataset

def E_distance(a,b):
    return math.sqrt(abs(a[0]-b[0])**2+abs(a[1]-b[1])**2)


def auto_k_medoids():

    temp = []

    for i in range(2000):
        temp.append([random.randint(0,100),random.randint(0,100)])



    data = np.array(temp)

    D = pairwise_distances(data, metric=E_distance)

    # split into 2 clusters
    

    min_DBI = sys.maxsize
    final_M = None
    final_C = None
    k_value = -1


    for k in range(2,100):
        M, C = kmedoids.kMedoids(D, k)
        temp = []
        dic_si = {}

        DBI = []

        for point_idx in M:
            dic_si[point_idx] = sum(D[point_idx,:])/len(M)

        for point_idx in M:
            temp = []
            for point_jdx in M:
                if point_idx == point_jdx:
                    continue
                else:
                    temp.append((dic_si[point_idx]+point_jdx)/D[point_idx,point_jdx])

            DBI.append(max(temp))


        DBI = sum(DBI)/len(M)

        print(k,DBI,[list(data[item]) for item in M])

        if DBI < min_DBI:
            min_DBI = DBI
            final_M = M
            final_C = C
            k_value = k

    print(k_value,min_DBI,[list(data[item]) for item in M])




    # print('medoids:')
    # for point_idx in M:
    #     print( data[point_idx] )

    # print('')
    # print('clustering result:')
    # for label in C:
    #     for point_idx in C[label]:
    #         print('label {0}:　{1}'.format(label, data[point_idx]))


if __name__ == '__main__':
    auto_k_medoids()