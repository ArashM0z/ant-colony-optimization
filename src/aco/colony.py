"""Multi-process Ant Colony Optimisation for VRP.

Used in our SIGSPATIAL Workshop 2022 industrial case study.
"""

from __future__ import annotations

from dataclasses import dataclass
from multiprocessing import Pool

import numpy as np


@dataclass
class ACOConfig:
    n_ants: int = 50
    n_iterations: int = 200
    alpha: float = 1.0    # pheromone exponent
    beta: float = 2.0     # heuristic exponent
    rho: float = 0.1      # evaporation rate
    q: float = 100.0      # pheromone deposit factor
    n_workers: int = 4


def _ant_construct(args: tuple) -> tuple[list[int], float]:
    distance_matrix, pheromone, alpha, beta, demand, capacity, rng_seed = args
    rng = np.random.default_rng(rng_seed)
    n = distance_matrix.shape[0]
    unvisited = list(range(1, n))
    rng.shuffle(unvisited)

    route = [0]
    current = 0
    remaining_capacity = capacity
    while unvisited:
        feasible = [j for j in unvisited if demand[j - 1] <= remaining_capacity]
        if not feasible:
            route.append(0)
            current = 0
            remaining_capacity = capacity
            continue
        eta = 1.0 / (distance_matrix[current, feasible] + 1e-9)
        tau = pheromone[current, feasible]
        weights = (tau ** alpha) * (eta ** beta)
        weights = weights / weights.sum()
        next_node = int(rng.choice(feasible, p=weights))
        route.append(next_node)
        remaining_capacity -= demand[next_node - 1]
        current = next_node
        unvisited.remove(next_node)
    route.append(0)
    cost = float(np.sum([distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1)]))
    return route, cost


def run_aco(
    distance_matrix: np.ndarray,
    demand: np.ndarray,
    capacity: float,
    cfg: ACOConfig = ACOConfig(),
    seed: int | None = None,
) -> tuple[list[int], float, list[float]]:
    """Run ACO and return (best_route, best_cost, per-iteration best costs)."""
    rng = np.random.default_rng(seed)
    n = distance_matrix.shape[0]
    pheromone = np.ones((n, n)) * 0.1
    best_route: list[int] = []
    best_cost = float("inf")
    history: list[float] = []

    with Pool(cfg.n_workers) as pool:
        for it in range(cfg.n_iterations):
            seeds = rng.integers(0, 2**31, size=cfg.n_ants)
            args = [
                (distance_matrix, pheromone, cfg.alpha, cfg.beta, demand, capacity, int(s))
                for s in seeds
            ]
            results = pool.map(_ant_construct, args)
            # Evaporate
            pheromone = pheromone * (1 - cfg.rho)
            # Deposit
            for route, cost in results:
                deposit = cfg.q / cost
                for i in range(len(route) - 1):
                    pheromone[route[i], route[i + 1]] += deposit
                    pheromone[route[i + 1], route[i]] += deposit
                if cost < best_cost:
                    best_cost = cost
                    best_route = route
            history.append(best_cost)
    return best_route, best_cost, history
