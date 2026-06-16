class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        tasks = []
        # maxheap for tasks to complete
        # we want a maxheap so that the topmost element we pop
        # is the most frequent element (greedy?)
        # suboptimal to do a task that occurs less first because
        # of the constraint
        # after pushing everything to heap
        # start simulating tasks
        # a global timer so that we can know when tasks can be safely
        # repeated
        # pop from heap, this is a task we will do
        # store the popped element in a queue, with a designated
        # time when it can be safely popped from the queue
        # this simulates the constraint
        for task, frequency in frequencies.items():
            heapq.heappush_max(tasks, (frequency, task))
        
        timer = 0
        cooldown = deque()

        while tasks or cooldown:
            freq, task = None, None
            if tasks:
                freq, task = heapq.heappop_max(tasks)
            if freq and freq > 1:
                cooldown.append((freq - 1, task, timer + n))
            while cooldown and timer >= cooldown[0][2]:
                # if the timer is past the cooldown for first stack element...
                cfreq, ctask, ctimer = cooldown.popleft()
                heapq.heappush_max(tasks, (cfreq, ctask))
            timer += 1
        return timer
            