import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from pricing.binomial import price_option_binomial


def main():

    print("=" * 50)
    print("BINOMIAL TREE OPTION PRICING")
    print("=" * 50)

    call_price = price_option_binomial(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20,
        option_type="call",
        steps=100,
    )

    print(f"\nCall Option Price : {call_price:.6f}")

    put_price = price_option_binomial(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20,
        option_type="put",
        steps=100,
    )

    print(f"Put Option Price  : {put_price:.6f}")


if __name__ == "__main__":
    main()