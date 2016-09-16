import math
import copy


# sharnoby

def readfile(filename):
    file = open(filename)
    header = [int(x) for x in file.readline().split()]
    rows = header[0]
    cols = header[1]
    drones = header[2]
    turns = header[3]
    max_payload = header[4]

    num_products = int(file.readline())
    weights = [int(x) for x in file.readline().split()]

    num_warehouses = int(file.readline())
    warehouses = {}
    for i in range(num_warehouses):
        coordinates = tuple(int(x) for x in file.readline().split())
        products = [int(x) for x in file.readline().split()]
        warehouses[i] = {"coordinates": coordinates, "products": products}

    num_orders = int(file.readline())
    orders = {}
    for i in range(num_orders):
        coordinates = tuple(int(x) for x in file.readline().split())
        num_items = int(file.readline())
        products = [int(x) for x in file.readline().split()]
        orders[i] = {"coordinates": coordinates, "products": products}
    
    return weights, warehouses, orders, drones, max_payload,turns

def distance(x, y):
    return int(math.ceil(math.sqrt(abs(x[0] - x[1]) + abs(y[0] - y[1]))))

def map_warehouses_to_orders(warehouses, orders):
    warehouses_copy = copy.deepcopy(warehouses)
    orders_copy = copy.deepcopy(orders)

    orders_warehouses = {}
    for o, order in orders_copy.items():
        orders_warehouses[o] = []
        for w, warehouse in warehouses_copy.items():
            dist = distance(order["coordinates"], warehouse["coordinates"])
            orders_warehouses[o].append((dist, w))
            orders_warehouses[o].sort()

    orders_best_warehouses = {}
    for o, order in orders_copy.items():
        orders_best_warehouses[o] = {}
        for w in orders_warehouses[o]:
            for product in order["products"]:
                if (warehouses_copy[w[1]]["products"][product] > 0):
                    order["products"].remove(product)
                    warehouses_copy[w[1]]["products"][product] -= 1
                    if w[1] in orders_best_warehouses[o].keys():
                        orders_best_warehouses[o][w[1]].append(product)
                    else:
                        orders_best_warehouses[o][w[1]] = [product]

    return orders_best_warehouses

def generate_solution(commands):
    solution = []
    for command in commands:
        drone = command["drone"]
        warehouse = command["warehouse"]
        delivery = command["delivery"]
        products = command["products"]
        products_set = set(products)
        for product in products_set:
            count = products.count(product)
            solution.append("{} L {} {} {}".format(drone, warehouse, product, count))
            solution.append("{} D {} {} {}".format(drone, delivery, product, count))
    return solution

def write_solution(solution, filename):
    out = open(filename + "_solution.out", "w+")
    out.write(str(len(solution)) + "\n")
    out.writelines("\n".join(solution))

#Enis



#Adam

"""
order_warehouses = {'W1':[0,0,1],'W2':[0,0,1],'W3':[0,0,1],'W4':[0,0,1]}
warehouses = {'W1':{'coordinates':(0,0)},'W2':{'coordinates':(16,0)},'W3':{'coordinates':(0,16)},'W4':{'coordinates':(16,16)}}
print center_of_mass(order_warehouses,warehouses)
"""

def center_of_mass(order_warehouses,dict_of_warehouses):
    list_of_warehouses = order_warehouses.keys()
    coordinates = [dict_of_warehouses[i]["coordinates"] for i in list_of_warehouses]
    x = [i for i,j in coordinates]
    y = [j for i,j in coordinates]
    centroid = (sum(x)/len(coordinates),sum(y)/len(coordinates))
    return centroid

#orders_best_warehouses = {"Q1":{'W1':[0,0,1],'W2':[0,0,1],'W3':[0,0,1],'W4':[0,0,1]}}
#weights = [10,5]
def calculate_delivery_load(orders_best_warehouses,weights):
    #order_drone_number = {Q1:int}
    order_drone_number = {}
    for order,inside_warehouses in orders_best_warehouses.items():
        load =0
        for warehouses in inside_warehouses.values():
            for element in warehouses:
                load+= weights[element]
        order_drone_number[order] = load
    return order_drone_number


def map_drones_warehouses(orders_best_warehouses,available_drones,capacity,weights,drone_coordinates,warehouses):
    orders_list = orders_best_warehouses.keys()
    commands = []
    for order in orders_list:
        w1_list=orders_best_warehouses[order]

        drones_list=[]
        for i,j in available_drones.items():
            drones_list.append((j,i))
        drones_list.sort()


        for wx,p_id_list in w1_list.items():
            products=[]
            capacity_now=capacity
            a_drone=drones_list[0]

            for i,j in available_drones.items():
                drones_list.append((j,i))
            drones_list.sort()

            for counter,p_id in enumerate(p_id_list) :
                p_weight = weights[p_id]
                if capacity_now>=p_weight:
                    capacity_now-=p_weight
                    products.append(p_id)
                elif counter==len(p_id_list)-1:
                    commands.append({"drone":a_drone,"warehouses":wx,"delivery":order,"products":products})
                    my_distance=distance(drone_coordinates[a_drone],warehouses[wx]["coordinates"])
                    available_drones[a_drone]+=my_distance+2*len(set(products))

                    drone_coordinates[a_drone]=(warehouses[wx]["coordinates"])


                else:

                    commands.append({"drone":a_drone,"warehouses":wx,"delivery":order,"products":products})
                    my_distance=distance(drone_coordinates[a_drone],warehouses[wx]["coordinates"])
                    available_drones[a_drone]+=my_distance+2*len(set(products))

                    drone_coordinates[a_drone]=(warehouses[wx]["coordinates"])

                    products=[]
                    capacity_now=capacity
                    a_drone=drones_list[0]

                    for i,j in available_drones.items():
                        drones_list.append((j,i))
                    drones_list.sort()
    return commands











# solution

filename = "busy_day"
# filename = "mother_of_all_warehouses"
# filename = "redundancy"

weights, warehouses, orders, drones, capacity,turns = readfile(filename + ".in")
#available drones = {1:int(t)}
available_drones ={}
drone_coordinates = {}
for i in range(drones):
    available_drones.setdefault(i,0)
    drone_coordinates.setdefault(i,warehouses[0]["coordinates"])

orders_best_warehouses = map_warehouses_to_orders(warehouses, orders)

order_drone_number=calculate_delivery_load(orders_best_warehouses, weights)
commands = map_drones_warehouses(orders_best_warehouses,available_drones,capacity,weights,drone_coordinates,warehouses)
solution = generate_solution(commands)

write_solution(solution, filename)
