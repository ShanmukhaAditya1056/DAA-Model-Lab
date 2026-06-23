class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def schedule_jobs(jobs, max_deadline):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    slots = [False] * (max_deadline + 1)
    scheduled_jobs = [None] * (max_deadline + 1)
    
    total_profit = 0
    count_jobs = 0
    for job in jobs:
        for j in range(min(max_deadline, job.deadline), 0, -1):
            if not slots[j]:
                slots[j] = True
                scheduled_jobs[j] = job.job_id
                total_profit += job.profit
                count_jobs += 1
                break

    final_schedule = [job for job in scheduled_jobs if job is not None]
    
    return final_schedule, total_profit

job_data = [
    Job('J1', 4, 20),
    Job('J2', 1, 10),
    Job('J3', 1, 40),
    Job('J4', 1, 30)
]

schedule, profit = schedule_jobs(job_data, 4)
print(f"Scheduled Jobs Sequence: {schedule}")
print(f"Maximum Profit Earned: {profit}")