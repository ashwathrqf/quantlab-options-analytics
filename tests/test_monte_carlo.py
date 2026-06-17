import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from pricing.monte_carlo import price_option_mc


def main():
    price = price_option_mc(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2,
        option_type="call",
        num_simulations=100000,
        seed=42,
    )

    print(f"Call Option Premium : {price:.4f}")

    price = price_option_mc(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2,
        option_type="put",
        num_simulations=100000,
        seed=42,
    )

    print(f"Put Option Premium  : {price:.4f}")


if __name__ == "__main__":
    main()