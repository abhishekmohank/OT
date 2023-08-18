def johnsons_algorithm(Job):
    n = len(Job)
    machine1 = []
    machine2 = []
    for J in range(n):
        if Job[J][0] < Job[J][1]:
            machine1.append((Job[J], J))
        else:
            machine2.append((Job[J], J))
    machine1.sort(key=lambda x: x[0][0] - x[0][1])
    machine2.sort(key=lambda x: x[0][1] - x[0][0])

    sorted_jobs = [J[1] for J in machine1] + [J[1] for J in machine2]

    totaltime = 0
    machine1_time = 0
    for J in sorted_jobs:
        machine1_time += Job[J][0]
        totaltime = max(totaltime, machine1_time + Job[J][1])

    return sorted_jobs, totaltime

Job = [(3, 2), (1, 4), (6, 1), (2, 5), (4, 3)]
optimal_sequence, mintime = johnsons_algorithm(Job)
print("Optimal sequence:", optimal_sequence)
print("Minimum total processing time:", mintime)