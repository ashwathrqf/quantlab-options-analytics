import numpy as np
from scipy.stats import norm

def _validate_inputs(S:float, K:float, T: float,r:float, sigma:float, option_type:str):
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
    pass

def _compute_d1_d2(S:float, K:float, T: float,r:float, sigma:float):
    d1=(np.log(S/K)+T*(r+sigma**2/2))/sigma*np.sqrt(T)
    d2=d1-sigma*np.sqrt(T)

    return d1,d2

def price_option(S:float, K:float, T: float,r:float, sigma:float, option_type:str):
    """
    Prices a European call or put option using the Black-Scholes model.

    Parameters
    ----------
    S : float
        Current stock price.
    K : float
        Strike price.
    T : float
        Time to maturity in years.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility of the underlying asset.
    option_type : str
        'call' or 'put'.

    Returns
    -------
    float
        Option price.
    """
    
    _validate_inputs(S, K, T, r, sigma, option_type)
    option_type=option_type.lower()
    d1, d2 = _compute_d1_d2(S, K, T, r, sigma)
    discount_factor=np.exp(-r*T)
    if option_type=="call":
        price=S*norm.cdf(d1)-K*discount_factor*norm.cdf(d2)
    else:
        price=-S*norm.cdf(-d1)+K*discount_factor*norm.cdf(-d2)
    return float(price)

