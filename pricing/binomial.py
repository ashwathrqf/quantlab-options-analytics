import numpy as np

def _validate_inputs(S:float, K:float, T: float,r:float, sigma:float, option_type:str, steps:int):
    if S<=0:
        raise ValueError("Stock Price must be +ve")
    if K<=0:
        raise ValueError("Strike Price must be +ve")
    if T<=0:
        raise ValueError("Time of Expiry must be +ve")
    if sigma<=0:
        raise ValueError("Volatility must be +ve")
    if option_type.lower() not in ("call", "put"):
        raise ValueError("Option type must be 'call' or 'put'")
    if steps<=0 or not isinstance(steps, int):
        raise ValueError("Steps should be positive integer")

def _compute_parameters(S, K, T,r, sigma, option_type, steps):
    dt=T/steps
    u=np.exp(np.sqrt(dt)*sigma)
    d=1/u
    p=(np.exp(r*dt)-d)/(u-d)
    discount=np.exp(-r*dt)
    return dt,u,d,p,discount

def _generate_terminal_prices(S, K, T,r, sigma, option_type, steps):
    dt,u,d,p,discount=_compute_parameters(S, K, T,r, sigma, option_type, steps)
    terminal_prices = np.array([S*(u**(steps-i))*(d**i) for i in range(steps + 1)])
    return terminal_prices

def _compute_terminal_payoff(S, K, T,r, sigma, option_type, steps):
    terminal_prices=_generate_terminal_prices(S, K, T,r, sigma, option_type, steps)
    option_type=option_type.lower()
    if option_type=="call":
        payoff=np.maximum(terminal_prices-K,0)
    else:
        payoff=np.maximum(K-terminal_prices,0)
    return payoff

def _backward_induction(S, K, T,r, sigma, option_type, steps):
    dt,u,d,p,discount=_compute_parameters(S, K, T,r, sigma, option_type, steps)
    payoff=_compute_terminal_payoff(S, K, T,r, sigma, option_type, steps)
    for step in range(steps-1,-1,-1):
        payoff=discount*(p*payoff[:-1]+(1-p)*payoff[1:])
    return float(payoff[0])

def price_option_binomial(S, K, T,r, sigma, option_type, steps):
    _validate_inputs(S, K, T,r, sigma, option_type, steps)
    return _backward_induction(S, K, T,r, sigma, option_type, steps)
