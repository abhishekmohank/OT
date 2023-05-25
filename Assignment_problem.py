import numpy as np

def hungarian_algorithm(cost_matrix):
    # Step 1: Subtract the minimum value from each row and column
    cost_matrix = np.array(cost_matrix)
    n = cost_matrix.shape[0]
    
    min_val = np.min(cost_matrix)
    cost_matrix -= min_val
    
    # Step 2: Identify the minimum number of lines to cover all zeros
    mask_matrix = np.zeros_like(cost_matrix, dtype=bool)
    row_covered = np.zeros(n, dtype=bool)
    col_covered = np.zeros(n, dtype=bool)
    lines = np.zeros(2 * n, dtype=bool)
    
    step = 1
    while step != -1:
        if step == 1:
            # Step 3: Cover all zeros with the minimum number of lines
            for i in range(n):
                for j in range(n):
                    if cost_matrix[i, j] == 0 and not row_covered[i] and not col_covered[j]:
                        mask_matrix[i, j] = True
                        row_covered[i] = True
                        col_covered[j] = True
                        
            if np.sum(row_covered) == n:
                step = -1  # No more steps needed, go to final step
            else:
                step = 2
        
        elif step == 2:
            # Step 4: Find an uncovered zero and prime it
            row = 0
            col = 0
            done = False
            
            while not done:
                i, j = np.unravel_index(np.argmax(cost_matrix * (1 - mask_matrix)), cost_matrix.shape)
                
                if not row_covered[i] and not col_covered[j]:
                    mask_matrix[i, j] = True
                    
                    # Step 5: Find a starred zero in the same row
                    star_col = np.argmax(mask_matrix[i])
                    
                    if np.any(mask_matrix[:, star_col]):
                        row_covered[i] = True
                        col_covered[star_col] = False
                    else:
                        done = True
                        step = 3
                        row = i
                        col = j
                else:
                    cost_matrix[i, j] = np.inf
        
        elif step == 3:
            # Step 6: Construct a series of alternating primes and stars
            path = [(row, col)]
            done = False
            
            while not done:
                star_row = np.argmax(mask_matrix[:, path[-1][1]])
                
                if not np.any(mask_matrix[star_row]):
                    done = True
                else:
                    star_col = np.argmax(mask_matrix[star_row])
                    path.append((star_row, star_col))
                
                    prime_row = np.argmax(mask_matrix[path[-1][0]])
                    path.append((prime_row, path[-1][1]))
            
            # Step 7: Augment the path
            for i, j in path:
                if mask_matrix[i, j]:
                    mask_matrix[i, j] = False
                else:
                    mask_matrix[i, j] = True
            
            row_covered.fill(False)
            col_covered.fill(False)
            lines.fill(False)
            
            for i in range(n):
                for j in range(n):
                    if mask_matrix[i, j]:
                        row_covered[i] = True
                        col_covered[j] = True
            
            step = 1
    
    # Step 8: Calculate the minimum cost and generate the assignment
    assignment = np.zeros((n, 2), dtype=int)
    min_cost = 0
    
    for i in range(n):
        j = np.argmax(mask_matrix[i])
        assignment[i] = (i, j)
        min_cost += cost_matrix[i, j]
    
    # Step 9: Add the minimum value subtracted in Step 1
    min_cost += (n * min_val)
    
    return assignment, min_cost


# Example usage
cost_matrix = [[4, 1, 3],
               [2, 0, 5],
               [3, 2, 2]]

assignment, min_cost = hungarian_algorithm(cost_matrix)
print("Assignment:", assignment)
print("Minimum Cost:", min_cost)
