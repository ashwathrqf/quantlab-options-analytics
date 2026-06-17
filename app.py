from pricing.black_scholes import price_option_bs

price_bs = price_option_bs(
    S=100,
    K=100,
    T=1,
    r=0.05,
    sigma=0.2,
    option_type="call"
)

print(price)