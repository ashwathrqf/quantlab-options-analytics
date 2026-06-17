import streamlit as st
import pandas as pd

from pricing.black_scholes import price_option_bs
from pricing.monte_carlo import (
    price_option_mc,
    convergence_curve,
)
from pricing.greeks import calculate_greeks

from visualization.payoff import payoff_diagram
from visualization.convergence import convergence_plot


# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Options Pricing Engine",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📈 Options Pricing Engine")
st.caption(
    "European Option Pricing • Black-Scholes • Monte Carlo • Greeks"
)

st.divider()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("⚙️ Parameters")

st.sidebar.subheader("Option")

option_type = st.sidebar.selectbox(
    "Option Type",
    ["call", "put"],
)

st.sidebar.subheader("Market")

S = st.sidebar.slider(
    "Stock Price (S)",
    min_value=1.0,
    max_value=300.0,
    value=100.0,
)

K = st.sidebar.slider(
    "Strike Price (K)",
    min_value=1.0,
    max_value=300.0,
    value=100.0,
)

T = st.sidebar.slider(
    "Time to Expiry (Years)",
    min_value=0.1,
    max_value=5.0,
    value=1.0,
)

sigma = (
    st.sidebar.slider(
        "Volatility (%)",
        1,
        100,
        20,
    )
    / 100
)

r = (
    st.sidebar.slider(
        "Risk-Free Rate (%)",
        0,
        20,
        5,
    )
    / 100
)

st.sidebar.subheader("Simulation")

num_simulations = st.sidebar.slider(
    "Monte Carlo Simulations",
    min_value=1000,
    max_value=500000,
    value=100000,
    step=1000,
)

# ----------------------------------------------------
# Pricing
# ----------------------------------------------------

bs_price = price_option_bs(
    S=S,
    K=K,
    T=T,
    r=r,
    sigma=sigma,
    option_type=option_type,
)

mc_price = price_option_mc(
    S=S,
    K=K,
    T=T,
    r=r,
    sigma=sigma,
    option_type=option_type,
    num_simulations=num_simulations,
    seed=42,
)

greeks = calculate_greeks(
    S=S,
    K=K,
    T=T,
    r=r,
    sigma=sigma,
    option_type=option_type,
)

# ----------------------------------------------------
# Metrics
# ----------------------------------------------------

error = abs(bs_price - mc_price)
percentage_error = error / bs_price * 100

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Black-Scholes",
        f"{bs_price:.4f}",
    )

with c2:
    st.metric(
        "Monte Carlo",
        f"{mc_price:.4f}",
    )

with c3:
    st.metric(
        "Difference",
        f"{error:.4f}",
        f"{percentage_error:.2f}%",
    )

# ----------------------------------------------------
# Greeks
# ----------------------------------------------------

st.subheader("Greeks")

greeks_df = pd.DataFrame(
    {
        "Greek": list(greeks.keys()),
        "Value": [round(v, 6) for v in greeks.values()],
    }
)

st.dataframe(
    greeks_df,
    hide_index=True,
    width="stretch",
)

st.divider()

# ----------------------------------------------------
# Charts
# ----------------------------------------------------

left, right = st.columns(2)

with left:
    payoff_fig = payoff_diagram(
        strike=K,
        option_type=option_type,
    )

    st.plotly_chart(
        payoff_fig,
        width="stretch",
    )

with right:

    convergence = convergence_curve(
        S=S,
        K=K,
        T=T,
        r=r,
        sigma=sigma,
        option_type=option_type,
        num_simulations=num_simulations,
        seed=42,
    )

    convergence_fig = convergence_plot(
        convergence,
        bs_price,
    )

    st.plotly_chart(
        convergence_fig,
        width="stretch",
    )