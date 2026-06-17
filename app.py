from pricing.black_scholes import price_option

price = price_option(
    S=100,
    K=100,
    T=1,
    r=0.05,
    sigma=0.2,
    option_type="call"
)

print(price)