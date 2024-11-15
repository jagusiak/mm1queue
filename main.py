from queue import MM1Queue
import matplotlib.pyplot as plt
from stop_criteria import TotalRequests

TIME_UNIT = "s"

NO_OF_REQUESTS = 100

INCOME_RATE = 2
SERVICE_RATE = 2.5


if __name__ == "__main__":
    q = MM1Queue(
        INCOME_RATE,
        SERVICE_RATE,
        stop_criteria=TotalRequests(NO_OF_REQUESTS)
    ).run()

    plt.step(*q.queue_length_vectorized, where="mid", label="Queue state")
    plt.xlabel(f"Time {TIME_UNIT}")
    plt.ylabel("Queue Length")
    plt.title(
        f"[M/M/1] in: {q.income_rate:.2f} req/{TIME_UNIT}, out: {q.service_rate:.2f} req/{TIME_UNIT}, avg wait t: {q.average_wait_time:.2f}s"
    )

    plt.legend()
    plt.show()
