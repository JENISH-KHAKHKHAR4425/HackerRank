# Job Scheduling Problem using Greedy Approach

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs, n):
    # Step 1: Sort jobs by descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Initialize time slots
    result = [False] * n
    job_order = ['-1'] * n

    # Step 3: Assign jobs to the latest possible free slot
    for job in jobs:
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not result[j]:
                result[j] = True
                job_order[j] = job.job_id
                break

    return job_order

# Driver Code
if __name__ == "__main__":
    jobs = [
        Job('J1', 2, 100),
        Job('J2', 1, 19),
        Job('J3', 2, 27),
        Job('J4', 1, 25),
        Job('J5', 3, 15)
    ]
    n = len(jobs)
    order = job_scheduling(jobs, n)
    print("Job Order for Maximum Profit:", [job for job in order if job != '-1'])
