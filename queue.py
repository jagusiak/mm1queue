from helpers import random_service_time
from request import Request



class MM1Queue:
    def __init__(self, income_rate: float, service_rate: float, stop_criteria: StopCriteria):
        self.income_rate = income_rate
        self.service_rate = service_rate
        self.stop_criteria = stop_criteria
        self.requests = []

    def run(self) -> "MM1Queue":
        time = 0
        waiting_time = 0

        while not self.stop_criteria.should_stop(self):
            next_income_time = random_service_time(self.income_rate)
            time += next_income_time
            waiting_time = max(0, waiting_time - next_income_time)
            request = Request(
                income_at=time,
                service_time=random_service_time(self.service_rate),
                waiting_time=waiting_time,
            )
            waiting_time += request.service_time
            self.requests.append(request)

        return self

    def queue_length(self):
        # generator that yields tuple (time, queue_length)
        t, r_in, r_out, l = 0, 0, 0, len(self)

        while r_out < l:
            yield t, r_in - r_out
            if r_in < l and (
                r_out == l
                or self.requests[r_in].income_at <= self.requests[r_out].leaves_queue_at
            ):
                t = self.requests[r_in].income_at
                r_in += 1
            else:
                t = self.requests[r_out].leaves_queue_at
                r_out += 1
        yield t, r_in - r_out

    @property
    def queue_length_vectorized(self):
        # returns tuple of two lists: time and queue length
        return tuple(zip(*self.queue_length()))

    @property
    def average_wait_time(self):
        return sum(r.waiting_time for r in self) / len(self)

    def __iter__(self):
        return iter(self.requests)

    def __len__(self):
        return len(self.requests)
