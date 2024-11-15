from abc import ABC, abstractmethod

from queue import MM1Queue


class StopCriteria(ABC):
    @abstractmethod
    def should_stop(self, queue: MM1Queue) -> bool: ...

class TotalRequests(StopCriteria):
    def __init__(self, max_requests: int):
        self.max_requests = max_requests

    def should_stop(self, queue: MM1Queue) -> bool:
        return len(queue) >= self.max_requests

class MaxRequestIncomeTime(StopCriteria):
    def __init__(self, max_income_time: float):
        self.max_income_time = max_income_time

    def should_stop(self, queue: MM1Queue) -> bool:
        return queue.requests[-1].income_at >= self.max_income_time