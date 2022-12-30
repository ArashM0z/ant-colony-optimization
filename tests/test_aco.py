import numpy as np
from aco.colony import ACOConfig, run_aco


def test_aco_decreases_cost() -> None:
    rng = np.random.default_rng(0)
    coords = rng.uniform(0, 1, size=(11, 2))
    coords[0] = 0.5
    dist = np.linalg.norm(coords[:, None] - coords[None], axis=-1)
    demand = rng.uniform(0.1, 0.3, size=10)
    cfg = ACOConfig(n_ants=10, n_iterations=10, n_workers=1)
    _, _, history = run_aco(dist, demand, capacity=1.0, cfg=cfg, seed=0)
    assert history[-1] <= history[0]
