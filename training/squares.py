__author__ = 'berkcoban'
#!/usr/bin/env python
#-*-coding:utf-8-*-
import math
def from_file_create_matrix(file_name):
    my_file = open(file_name)

    my_matrix = []

    row,column = my_file.readline().split()
    (row,column)=(int(row),int(column))

    for i in my_file:
        my_list = []
        for k in i:
            if k == ".":

                my_list.append((0,0,0))

            if k == "#":

                my_list.append((1,1,1))
        my_matrix.append(my_list)
    my_file.close()

    for row_index,a_row in enumerate(my_matrix):
        for cou_index,an_element in enumerate(a_row):
            a_tuple=my_matrix[row_index][cou_index]
            #if there is something in the left
            if cou_index-1>=0:
                a_tuple= (my_matrix[row_index][cou_index-1][0]+a_tuple[0],a_tuple[1],a_tuple[2]+my_matrix[row_index][cou_index-1][0])

            if row_index-1>=0:
                a_tuple= (a_tuple[0],my_matrix[row_index-1][cou_index][1]+a_tuple[1],a_tuple[2]+my_matrix[row_index-1][cou_index][1])

            if cou_index-1>=0 and row_index-1>=0 :
                #left = my_matrix[row_index][cou_index-1][0]
                #up = my_matrix[row_index-1][cou_index][1]
                diagonol = my_matrix[row_index-1][cou_index-1][2]
                a_diagonol = +diagonol+a_tuple[2]

                a_tuple = (a_tuple[0],a_tuple[1],a_diagonol)

            my_matrix[row_index][cou_index] = a_tuple

            #print row_index,cou_index,an_element, my_matrix[row_index][cou_index]

    return my_matrix



def score_matrix(x1,y1,dimension,my_matrix):

    x2 = x1+dimension-1
    y2 = y1 + dimension-1

    diagonal_big= my_matrix[x2][y2][2]
    if x2-dimension<0:
        diagonal_up=0
    else:
        diagonal_up = my_matrix[x2-dimension][y2][2]
    if y2-dimension<0:
        diagonal_left=0
    else:
        diagonal_left = my_matrix[x2][y2-dimension][2]
    if x2-dimension<0 or y2-dimension<0:
        diagonal_small=0
    else:
        diagonal_small = my_matrix[x2-dimension][y2-dimension][2]

    total_cell = dimension * dimension


    closed_cell = diagonal_big-diagonal_left-diagonal_up+diagonal_small
    #print (closed_cell)
    #print (diagonal_big,diagonal_left,diagonal_up,diagonal_small)

    cost = total_cell - closed_cell + 1

    return cost


def find_squares(my_matrix):

    # 2S+1 is formula to calculate one side of square
    # biggest value of 2S+1 can be dimension of matrix


    biggest_number = (min (len (my_matrix),len(my_matrix[0])) - 1)/2
    # S which is a side of square should be a integer
    biggest_number = math.floor(biggest_number)
    # square_list = [(cost,x,y,dimension)...]
    square_list=[]
    for i in range(int(biggest_number)):
        dimension=(2*(i+1))+1
        square_list.extend(slide_square((len(my_matrix),len(my_matrix[0])),dimension))

    return square_list

def slide_square(my_matrix_size,dimension):
    # for a given dimension and size of matrix return list of all possible matrixes start points
    # input (x,y,dimension)
    # return (start_point_X,start_point_Y,dimension)
    x = 0 # number of rows
    y = 0 # number of columns

    square_list = []

    # slide over row
    while x+dimension <= my_matrix_size[0]:
        # slide over column
        while y+dimension <= my_matrix_size[1]:
            score=score_matrix(x,y,dimension,my_matrix)
            square_list.append((score,dimension,x,y))
            y+=1
        x+=1
        y = 0

    return square_list

my_matrix = from_file_create_matrix("learn_and_teach.in")
#print (find_squares(my_matrix)[1:1000])

#TESTING
# for r in my_matrix:
#     stritn = ""
#     for c in r:
#         stritn+=str(c) + " "
#     print (stritn)
#     print ("\n")
# print (find_squares(my_matrix)[:])