from dataclasses import dataclass


@dataclass
class Request:
    income_at: float
    service_time: float
    waiting_time: float

    @property
    def leaves_queue_at(self):
        # time when request leaves the queue
        return self.income_at + self.waiting_time
