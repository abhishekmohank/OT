import itertools

def zero_one_integer_programming(c, A, b):
    num_variables = len(c)
    combinations = list(itertools.product([0, 1], repeat=num_variables))
    optimal_value = float('-inf')
    optimal_solution = None
    
    for combination in combinations:
        if satisfies_constraints(combination, A, b):
            objective_value = calculate_objective_value(combination, c)
            if objective_value > optimal_value:
                optimal_value = objective_value
                optimal_solution = combination
                
    return optimal_solution, optimal_value

def satisfies_constraints(combination, A, b):
    num_constraints = len(A)
    for i in range(num_constraints):
        constraint_value = sum(A[i][j] * combination[j] for j in range(len(combination)))
        if constraint_value > b[i]:
            return False
    return True

def calculate_objective_value(combination, c):
    return sum(c[i] * combination[i] for i in range(len(combination)))

c = [1, 1] # Objective coefficients
A = [[3, 2], # Constraint coefficients
     [0, 1]]
b = [5, 2] # Constraint bounds

print("Integer Programming Problem:")
print("Objective function:")
for i in range(len(c)):
    print("x", i+1, "(", c[i], ")", end=" ")
    if i < len(c) - 1:
        print(" + ", end=" ")
print("\nConstraints:")
for i in range(len(A)):
    print("constraint ", i+1, ":", end=" ")
    for j in range(len(A[i])):
        print("x", j+1, "(", A[i][j], ")", end=" ")
        if j < len(A[i]) - 1:
            print(" + ", end=" ")
    print("\n")
print("Constraint bounds: [", end=" ")
for i in range(len(b)):
    print(b[i], end=" ")
    if i < len(b) - 1:
        print(", ", end=" ")
print(" ]\n")

solution, value = zero_one_integer_programming(c, A, b)
print("Optimal Solution:", solution)
print("Optimal Value:", value)