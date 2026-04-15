# Ant Colony Optimisation for VRP

Multi-process Ant Colony Optimisation used as a classical baseline in our SIGSPATIAL 2022 industrial case-study paper.

## Implementation

- Configurable α (pheromone exponent), β (heuristic exponent), ρ (evaporation), Q (deposit).
- Constructs solutions in parallel via `multiprocessing.Pool`.
- Standard pheromone evaporate + deposit per iteration.
- Capacity-feasible neighbour selection at each step.

## Use

```python
import numpy as np
from aco import ACOConfig, run_aco

dist = np.array(...)        # (N+1, N+1)
demand = np.array(...)      # (N,)
best_route, best_cost, history = run_aco(dist, demand, capacity=1.0,
                                         cfg=ACOConfig(n_ants=50, n_iterations=200))
```

<!-- notes 2022-02 -->

<!-- notes 2022-03 -->

<!-- notes 2022-05 -->

<!-- notes 2022-06 -->

<!-- notes 2022-08 -->

<!-- notes 2022-10 -->

<!-- maint 2025-01-15 -->

<!-- maint 2025-02-24 -->

<!-- maint 2025-04-03 -->

<!-- maint 2025-05-13 -->

<!-- maint 2025-06-20 -->

<!-- maint 2025-07-30 -->

<!-- maint 2025-09-06 -->

<!-- maint 2025-10-15 -->

<!-- maint 2025-11-24 -->

<!-- maint 2024-01-21 -->

<!-- maint 2024-03-12 -->

<!-- maint 2024-05-03 -->

<!-- maint 2024-06-25 -->

<!-- maint 2024-08-16 -->

<!-- maint 2024-10-06 -->

<!-- maint 2024-11-27 -->

<!-- maint 2023-01-30 -->

<!-- maint 2023-04-05 -->

<!-- iter 2023-05-08-09 -->

<!-- iter 2023-05-08-11 -->

<!-- iter 2023-05-08-13 -->

<!-- iter 2023-05-08-15 -->

<!-- iter 2023-05-08-17 -->

<!-- iter 2023-05-08-19 -->

<!-- iter 2023-10-02-09 -->

<!-- iter 2023-10-02-11 -->

<!-- iter 2023-10-02-13 -->

<!-- iter 2023-10-02-15 -->

<!-- iter 2023-10-02-17 -->

<!-- iter 2023-10-02-19 -->

<!-- iter 2023-10-02-21 -->

<!-- iter 2024-02-19-09 -->

<!-- iter 2024-02-19-11 -->

<!-- iter 2024-02-19-13 -->

<!-- iter 2024-02-19-15 -->

<!-- iter 2024-02-19-17 -->

<!-- iter 2024-02-19-19 -->

<!-- iter 2024-02-19-21 -->

<!-- iter 2024-09-02-09 -->

<!-- iter 2024-09-02-11 -->

<!-- iter 2024-09-02-13 -->

<!-- iter 2024-09-02-15 -->

<!-- iter 2024-09-02-17 -->

<!-- iter 2024-09-02-19 -->

<!-- iter 2024-09-02-21 -->

<!-- iter 2024-09-02-22 -->

<!-- iter 2026-02-23-09 -->

<!-- iter 2026-02-23-11 -->

<!-- iter 2026-02-23-13 -->

<!-- iter 2026-02-23-15 -->

<!-- iter 2026-02-23-17 -->

<!-- iter 2026-02-23-19 -->

<!-- iter 2026-02-23-21 -->

<!-- m 2023-09-25T23:31:00-06:00 -->

<!-- m 2024-09-11T15:56:00-06:00 -->

<!-- m 2023-08-24T14:40:00-06:00 -->

<!-- m 2025-08-03T19:31:00-06:00 -->

<!-- m 2026-03-22T17:16:00-06:00 -->

<!-- m 2023-11-08T21:00:00-06:00 -->

<!-- m 2025-01-12T22:10:00-06:00 -->

<!-- m 2023-09-02T16:36:00-06:00 -->

<!-- m 2023-12-24T18:34:00-06:00 -->

<!-- m 2023-12-20T21:12:00-06:00 -->

<!-- m 2026-04-07T15:03:00-06:00 -->

<!-- m 2025-06-17T15:11:00-06:00 -->

<!-- m 2024-02-23T22:19:00-06:00 -->

<!-- m 2023-09-26T19:26:00-06:00 -->

<!-- m 2025-02-07T23:52:00-06:00 -->

<!-- m 2023-02-10T21:32:00-06:00 -->

<!-- m 2026-01-20T17:12:00-06:00 -->

<!-- m 2023-07-05T20:32:00-06:00 -->

<!-- m 2026-04-13T15:08:00-06:00 -->

<!-- m 2026-04-15T17:58:00-06:00 -->
