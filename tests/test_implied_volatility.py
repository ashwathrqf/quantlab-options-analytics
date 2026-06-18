import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from pricing.black_scholes import price_option_bs
from pricing.implied_volatility import implied_volatility


def main():

    print("=" * 60)
    print("IMPLIED VOLATILITY TEST")
    print("=" * 60)

    # Known parameters
    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma_true = 0.35
    option_type = "call"

    # Generate a market price using Black-Scholes
    market_price = price_option_bs(
        S=S,
        K=K,
        T=T,
        r=r,
        sigma=sigma_true,
        option_type=option_type,
    )

    print(f"Market Price        : {market_price:.6f}")
    print(f"Actual Volatility   : {sigma_true:.4f}")

    iv = implied_volatility(
        market_price=market_price,
        S=S,
        K=K,
        T=T,
        r=r,
        sigma_guess=0.30,
        option_type=option_type,
        num_iters=100,
        tol=1e-8,
    )

    print(f"Implied Volatility  : {iv:.6f}")


if __name__ == "__main__":
    main()