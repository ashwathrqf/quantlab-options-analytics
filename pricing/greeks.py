import numpy as np
from scipy.stats import norm

from pricing.black_scholes import _compute_d1_d2

def calculate_greeks(S,K,T,r,sigma,option_type):
    option_type=option_type.lower()
    d1,d2=_compute_d1_d2(S,K,T,r,sigma)
    common_term=(S*norm.pdf(d1)*sigma)/(2*np.sqrt(T))

    if option_type=="call":
        delta=norm.cdf(d1)
        theta=-common_term-r*K*np.exp(-r*T)*norm.cdf(d2)
        rho=K*T*np.exp(-r*T)*norm.cdf(d2)        
    else:
        delta=norm.cdf(d1)-1
        theta=-common_term+r*K*np.exp(-r*T)*norm.cdf(-d2)
        rho=-K*T*np.exp(-r*T)*norm.cdf(-d2)
    
    gamma=norm.pdf(d1)/(S*sigma*np.sqrt(T))

    vega=S*np.sqrt(T)*norm.pdf(d1)

    return {
        "delta":delta,
        "gamma":gamma,
        "vega":vega,
        "theta":theta,
        "rho":rho,
    }


