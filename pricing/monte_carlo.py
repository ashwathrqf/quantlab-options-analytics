import numpy as np

def _validate_inputs(S:float, K:float, T: float,r:float, sigma:float, option_type:str, num_simulations:int, seed:int):
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
    if num_simulations%1!=0 or num_simulations<=0:
        raise ValueError("Number of Simulations must be positive and an integer") 
    if seed%1!=0 or seed<=0:
        raise ValueError("Seed must be positive and an integer")   

def _generate_terminal_prices(S:float, K:float, T: float,r:float, sigma:float, option_type:str, num_simulations:int, seed:int):
    rng=np.random.default_rng(seed)
    Z=rng.standard_normal(num_simulations)
    terminal_prices=S*np.exp((r-sigma**2/2)*T+sigma*Z*np.sqrt(T))

    return terminal_prices

def _generate_terminal_prices_antithetic(S:float, K:float, T: float,r:float, sigma:float, option_type:str, num_simulations:int, seed:int):
    rng=np.random.default_rng(seed)
    Z=rng.standard_normal(num_simulations//2)

    Z=np.concatenate([Z,-Z])

    terminal_prices_antithetic=S*np.exp((r-sigma**2/2)*T+sigma*Z*np.sqrt(T))

    return terminal_prices_antithetic


def _compute_payoff(K,terminal_prices,option_type):

    option_type=option_type.lower()

    if option_type=="call":
        payoff=np.maximum(terminal_prices-K,0)
    else:
        payoff=np.maximum(K-terminal_prices,0)
    
    return payoff

def price_option_mc(S:float, K:float, T: float,r:float, sigma:float, option_type:str, num_simulations:int, seed:int):
    _validate_inputs(S, K, T,r, sigma, option_type, num_simulations, seed)
    terminal_prices=_generate_terminal_prices(S, K, T,r, sigma, option_type, num_simulations, seed)
    payoff=_compute_payoff(K,terminal_prices,option_type)
    discount_factor=np.exp(-r*T)
    price=discount_factor*np.mean(payoff)

    return float(price)

def convergence_curve(S,K,T,r,sigma,option_type,num_simulations,seed=42):
    _validate_inputs(S,K,T,r,sigma,option_type,num_simulations,seed=42)
    terminal_prices=_generate_terminal_prices(S,K,T,r,sigma,option_type,num_simulations,seed=42)
    payoff=_compute_payoff(K,terminal_prices,option_type)
    running_mean = np.cumsum(payoff) / np.arange(1, len(payoff) + 1)
    running_mean *= np.exp(-r * T)
    return running_mean

def _compute_confidence_interval(payoff, r,T):
    discounted=payoff*np.exp(-r*T)
    mean=np.mean(discounted)
    std=np.std(discounted,ddof=1)
    se=std/np.sqrt(len(discounted))
    margin=1.96*se
    lower=mean-margin
    upper=mean+margin

    return {
        "price":mean,
        "std_error":se,
        "margin":margin,
        "lower":lower,
        "upper":upper,
        "confidence":0.95
    }
def price_option_mc_statistics(S:float, K:float, T: float,r:float, sigma:float, option_type:str, num_simulations:int, seed:int):
    _validate_inputs(S,K,T,r,sigma,option_type,num_simulations,seed=42)
    terminal_prices=_generate_terminal_prices(S,K,T,r,sigma,option_type,num_simulations,seed=42)
    payoff=_compute_payoff(K,terminal_prices,option_type)
    return _compute_confidence_interval(payoff,r,T)

def price_option_mc_antithetic(S:float, K:float, T: float,r:float, sigma:float, option_type:str, num_simulations:int, seed:int):
    _validate_inputs(S,K,T,r,sigma,option_type,num_simulations,seed=42)
    terminal_prices=_generate_terminal_prices_antithetic(S, K, T,r, sigma, option_type, num_simulations, seed)
    payoff=_compute_payoff(K,terminal_prices,option_type)
    discount_factor=np.exp(-r*T)
    price=discount_factor*np.mean(payoff)

    return float(price)   

