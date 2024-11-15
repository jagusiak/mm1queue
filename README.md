# M/M/1 Queue Simulation

This repository contains a simple simulation of an M/M/1 queue system. It uses a custom `MM1Queue` class to model the queue and visualize its behavior over time.

## Features

- Models a single-server queue
- Allows customizable input rates, service rates, and stopping criteria.
- Visualizes queue length over time using a step plot.

## Requirements

- Python 3.8 or higher
- Required libraries:
  - `matplotlib`
  - `numpy`


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/mm1-queue-simulation.git
   cd mm1-queue-simulation```
   
2. Install the required libraries:

   ```bash
   pip install matplotlib```
   
## Usage

Modify the parameters in the script (main.py) to fit your simulation needs:

- INCOME_RATE: Request arrival rate (requests per time unit).
- SERVICE_RATE: Request service rate (requests per time unit).
- NO_OF_REQUESTS: Total number of requests to process.


Run the simulation: `python main.py`
  
### Note

Stop criteria can be changed to check simulation time. Use `MaxRequestIncomeTime(total_time)` instead of `MaxRequestIncome(total_requests)` in queue simulation constructor.

## Output

The simulation produces a step plot showing the queue length over time. Additional information is displayed, including:

- Arrival rate (in).
- Service rate (out).
- Average wait time in seconds.

More analysis can be done by investigating `q.requests` list.
