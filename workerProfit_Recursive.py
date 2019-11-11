class job(object):
    def __init__(self, job_difficulty, job_profit):
        self.difficulty = job_difficulty
        self.profit = job_profit

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        mp = 0
        jobs = [job(difficulty[z], profit[z]) for z in range(len(difficulty))]
        jobs.sort(key=lambda x: x.difficulty)  # sort by difficulty
        for i in range(len(worker)):
            mp += profitMaximizer(jobs, worker, i, 0)
        return mp

def profitMaximizer(jobs, worker, i, j):
    if j >= len(jobs):
        return 0
    if jobs[j].difficulty > worker[i]:
        return 0                  # BOUNCE BACK
    return max(profitMaximizer(jobs, worker, i, j+1), # EXCLUDE
               jobs[j].profit)                       # INCLUDE

if __name__ == '__main__':
    d = [2,4,6,8,11]
    p = [10,20,30,40,50]
    w = [4,5,6,7]
    S = Solution()
    print(S.maxProfitAssignment(d,p,w))