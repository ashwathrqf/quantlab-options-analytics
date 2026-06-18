import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from pricing.monte_carlo import (
    price_option_mc,
    price_option_mc_antithetic,
    price_option_mc_statistics,
)


def main():

    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.20
    option_type = "call"
    num_simulations = 100000
    seed = 42

    print("=" * 60)
    print("MONTE CARLO TEST")
    print("=" * 60)

    mc_price = price_option_mc(
        S=S,
        K=K,
        T=T,
        r=r,
        sigma=sigma,
        option_type=option_type,
        num_simulations=num_simulations,
        seed=seed,
    )

    print(f"\nStandard Monte Carlo Price : {mc_price:.6f}")

    antithetic_price = price_option_mc_antithetic(
        S=S,
        K=K,
        T=T,
        r=r,
        sigma=sigma,
        option_type=option_type,
        num_simulations=num_simulations,
        seed=seed,
    )

    print(f"Antithetic MC Price        : {antithetic_price:.6f}")

    stats = price_option_mc_statistics(
        S=S,
        K=K,
        T=T,
        r=r,
        sigma=sigma,
        option_type=option_type,
        num_simulations=num_simulations,
        seed=seed,
    )

    print("\nMonte Carlo Statistics")
    print("-" * 30)
    print(f"Price           : {stats['price']:.6f}")
    print(f"Std Error       : {stats['std_error']:.6f}")
    print(f"Margin          : {stats['margin']:.6f}")
    print(f"95% CI Lower    : {stats['lower']:.6f}")
    print(f"95% CI Upper    : {stats['upper']:.6f}")


if __name__ == "__main__":
    main()