import numpy as np

from pricing.black_scholes import price_option_bs
from pricing.greeks import calculate_greeks

def _validate_inputs(market_price:float,S:float,K:float,T:float,r:float,sigma_guess:float,option_type:str,num_iters:int,tol:float):
    if market_price<=0:
        raise ValueError("Market Price must be +ve")
    if S<=0:
        raise ValueError("Stock Price must be +ve")
    if K<=0:
        raise ValueError("Strike Price must be +ve")
    if T<=0:
        raise ValueError("Time of Expiry must be +ve")
    if r<0:
        raise ValueError("Rate of Interest must be +ve")
    if sigma_guess<=0:
        raise ValueError("Volatility guess must be +ve")
    if option_type.lower() not in ("call", "put"):
        raise ValueError("Option type must be 'call' or 'put'")
    if num_iters<=0 or not isinstance(num_iters,int):
        raise ValueError("Number of NR Iterations must be +ve integer")
    if tol<=0:
        raise ValueError("NR tolerance must be +ve")

def _compute_error(market_price,S,K,T,r,sigma,option_type):
    price_bs=price_option_bs(S,K,T,r,sigma,option_type)
    error=price_bs-market_price
    return float(error)

def _newton_step(market_price,S,K,T,r,sigma,option_type,num_iters=10000,tol=0.001):
    for _ in range(num_iters):
        error=_compute_error(market_price,S,K,T,r,sigma,option_type)
        vega=calculate_greeks(S,K,T,r,sigma,option_type)["vega"]
        if abs(vega) < 1e-10:
            raise ValueError("Vega too small. Newton-Raphson cannot continue.")
        if abs(error)<tol:
            break
        sigma-=error/vega
    return float(max(sigma,1e-6))

def implied_volatility(market_price,S,K,T,r,sigma_guess,option_type,num_iters,tol):
    _validate_inputs(market_price,S,K,T,r,sigma_guess,option_type,num_iters,tol)
    return _newton_step(market_price,S,K,T,r,sigma_guess,option_type,num_iters,tol)

    



