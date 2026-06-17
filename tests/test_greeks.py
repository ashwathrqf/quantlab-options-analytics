import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from pricing.greeks import calculate_greeks


def main():
    greeks = calculate_greeks(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2,
        option_type="call",
    )

    print("\n===== CALL OPTION GREEKS =====")
    print(f"Delta : {greeks['delta']:.6f}")
    print(f"Gamma : {greeks['gamma']:.6f}")
    print(f"Vega  : {greeks['vega']:.6f}")
    print(f"Theta : {greeks['theta']:.6f}")
    print(f"Rho   : {greeks['rho']:.6f}")

    greeks = calculate_greeks(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2,
        option_type="put",
    )

    print("\n===== PUT OPTION GREEKS =====")
    print(f"Delta : {greeks['delta']:.6f}")
    print(f"Gamma : {greeks['gamma']:.6f}")
    print(f"Vega  : {greeks['vega']:.6f}")
    print(f"Theta : {greeks['theta']:.6f}")
    print(f"Rho   : {greeks['rho']:.6f}")


if __name__ == "__main__":
    main()