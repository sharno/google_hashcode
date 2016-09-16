__author__ = 'ademkerenci'
import main,squares

def multipliying_the_second_index_with_division(list_of_four_tuple):
    for i in range(len(list_of_four_tuple)):
        element = 1.0 / list_of_four_tuple[i][1]
        list_of_four_tuple[i] = (list_of_four_tuple[i][0],element,list_of_four_tuple[i][2],list_of_four_tuple[i][3])
    return list_of_four_tuple

def center_finder(d,r,c):
    for i in range(d/2):
        r += 1
        c += 1
    return (r,c)

def dimension_finder(one_result):
    d,r,c = int(1 / one_result[1]),one_result[2],one_result[3]
    center = center_finder(d,r,c)
    list_of_coordinates = list()
    for i in range(d):
        for j in range(d):
            list_of_coordinates.append((r+i,c+j))
    return list_of_coordinates,(d-1)/2,center


def combiner__of_codes_enis_shaynobi(enis_result,shaynobi_grid):
    solution = []
    for result in enis_result:
        coordinates_to_be_0 = dimension_finder(result)[0]
        s = dimension_finder(result)[1]
        row,column = dimension_finder(result)[2]
        for r,c in coordinates_to_be_0:
            if int(shaynobi_grid[r][c]) == 0:
                solution.append(main.erase_cell(r,c))
            shaynobi_grid[r][c] = 0
        solution.append(main.paint_square(row,column,s))
    return shaynobi_grid,solution


my_matrix = squares.from_file_create_matrix("learn_and_teach.in")
result = multipliying_the_second_index_with_division(squares.find_squares(my_matrix)[1:100])
result.sort()
N, M, grid = main.readfile("learn_and_teach.in")

grid,solution = combiner__of_codes_enis_shaynobi(result,grid)



# N, M, grid = readfile("learn_and_teach.in")
# N, M, grid = readfile("right_angle.in")
singles = main.extract_singles(grid, N, M)
stripes = main.extract_stripes(grid, N, M)
solution = main.solve_stripes(grid, N, M, stripes, singles,solution)
out = open("learn_solution.out", "w+")
# out = open("learn_solution.out", "w+")
# out = open("right_solution.out", "w+")

out.write(str(len(solution)) + "\n")
out.writelines("\n".join(solution))



