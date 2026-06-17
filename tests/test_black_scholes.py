import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from pricing.black_scholes import price_option

call = price_option(
    S=100,
    K=100,
    T=1,
    r=0.05,
    sigma=0.20,
    option_type="call",
)

put = price_option(
    S=100,
    K=100,
    T=1,
    r=0.05,
    sigma=0.20,
    option_type="put",
)

print(f"Call Price : {call:.4f}")
print(f"Put Price  : {put:.4f}")