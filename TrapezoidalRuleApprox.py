import math
import csv

PI= math.pi
CONSTANT = 2/PI

###
#(1) Getting values from csv
###
def get_csv_values():
    val = []
    file = open("A42.csv")
    for r in csv.reader(file):
        val.append(float(r[0]))
    file.close()
    return val
    
###
#(2) Converting i values to sin(Ai/n), where A ranges from [0,n] and n is the length of f values
###

def get_sin_x_values(n, k):
    i_values = [i for i in range(n)]
    # i could be 0, 1 , 2, 3, 4,.... n
    
    pi_with_index = (k * PI)/(n-1)
    #k phi / n
    
    pi_i_values = list(map(lambda i_value: i_value * pi_with_index, i_values))
    # 0 , pi/(n-1), 2pi/(n-1), 3pi/(n-1), ...., (n-1)pi/(n-1)
    
    complete_values = list(map(lambda pi_i_value: math.sin(pi_i_value), pi_i_values))
    # sin(0) , sin(pi/(n-1)), sin(2pi/(n-1)), sin(3pi/(n-1)), ...., sin((n-1)pi/(n-1))
    
    assert n == len(complete_values)
    return complete_values

##
#(3) Multiply f * sin(x) to fet the original approximation of the function.
##

def cross_fn(sin_index_values, fn_values):
    return [sin_index_value * fn_value for sin_index_value, fn_value in zip(sin_index_values, fn_values)]
    # f_0 * sin(0), f_1 * sin(pi/n), f_2 * sin(2pi/n), ....  f_n * sin(npi/n)

##
#(4) Trapezoid numerical approximation method
##
def trapezoid_fn(value):
    delta_x_values = PI/(len(value) - 1)
    total = sum(2 * value[1:-1]) + (value[0]) + (value[-1])
    return delta_x_values * total * 0.5
    #standard formula for trapezoidal method
    
##
#(5) Multiplyting the function by 2/pi to get B_k(f)
##
def get_b_fn(integral_value):
    return integral_value * CONSTANT
    # Getting b_value
    
##
#(6) Putting (1) through (5) together to get a particular b value
##
def get_b(fn_values, b_index):
    sin_values = get_sin_x_values(len(fn_values), b_index)
    trapezoid_values = cross_fn(sin_values, fn_values)
    return get_b_fn(trapezoid_fn(trapezoid_values))

##
##repeat the process to parse the test data in step 3, and the actual data in step 4
##
def main():
    csv_values = get_csv_values()
    value_res_list = []
    b_index = 1
    
    while True:
        val = get_b(csv_values, b_index)
        if round(val) <= 0:
            break
        b_index += 1
        value_res_list.append(round(val))
            
    print(value_res_list)
    print("R: " + str(len(value_res_list)))
    print(bytes(value_res_list).decode("utf-8"))
    
"""
Called the function to perform the Trapezoidal-rule approximation and get the value
"""
main()
