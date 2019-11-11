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
            mp += profitMaximizer(jobs, worker, i)
        return mp

def profitMaximizer(jobs, worker, i):
    profit_index = 0
    for j in range(len(jobs)):
        if j >= len(jobs) or jobs[j].difficulty > worker[i]:
            if j == 0:
                return 0
            break
        if jobs[profit_index].profit < jobs[j].profit:
            profit_index = j
    return jobs[profit_index].profit

if __name__ == '__main__':
    d = [85,47,57]
    p = [24,66,99]
    w = [40,25,25]
    S = Solution()
    print(S.maxProfitAssignment(d,p,w))