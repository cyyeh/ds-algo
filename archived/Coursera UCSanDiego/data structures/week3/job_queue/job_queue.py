# python3
import heapq

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        if self.num_workers >= len(self.jobs):
            for i in range(len(self.jobs)):
                self.assigned_workers[i] = i
                self.start_times[i] = 0
        else:
            # (next_free_time_for_the_worker, worker_index)
            next_free_time_list = [(0, i) for i in range(self.num_workers)]

            for i in range(self.num_workers):
                self.assigned_workers[i] = i
                self.start_times[i] = 0
                next_free_time_list[i] = (self.jobs[i], i)

            heapq.heapify(next_free_time_list)

            for i in range(self.num_workers, len(self.jobs)):                
                self.assigned_workers[i] = next_free_time_list[0][1]
                self.start_times[i] = heapq.heapreplace(next_free_time_list, (next_free_time_list[0][0] + self.jobs[i], next_free_time_list[0][1]))[0]            

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

