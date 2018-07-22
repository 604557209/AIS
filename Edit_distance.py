# -*- coding: utf-8 -*-
def edit(str1, str2):  #编辑距离
    matrix = [[i+j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1] == str2[j-1]:
                d = 0
            else:
                d = 1
            matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+d)
 
    return matrix[len(str1)][len(str2)]


def dice(str1,str2):  #Dice系数
    inset = set(str1)&set(str2)
    return len(inset)/(len(str1)+len(str2))



def Jaccard(str1,str2):  #Jaccard distance
    inset = set(str1)&set(str2)
    return len(inset)/(len(str1)+len(str2)-len(inset))

                         


if __name__ == '__main__':
    print(edit("湖北省武汉市武汉理工大学010","武汉理大学"))
    print(dice("湖北省武汉市武汉理工大学010","武汉理大学"))