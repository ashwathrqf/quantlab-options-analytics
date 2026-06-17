import numpy as np
import plotly.graph_objects as go


def payoff_diagram(strike, option_type):
    stock_prices = np.linspace(0.5 * strike, 1.5 * strike, 200)

    option_type = option_type.lower()

    if option_type == "call":
        payoff = np.maximum(stock_prices - strike, 0)
    else:
        payoff = np.maximum(strike - stock_prices, 0)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=stock_prices,
            y=payoff,
            mode="lines",
            name=f"{option_type.capitalize()} Payoff",
        )
    )

    fig.add_hline(y=0, line_dash="dash", opacity=0.5)
    fig.add_vline(x=strike, line_dash="dash", opacity=0.5)

    fig.update_layout(
        title="Option Payoff at Expiry",
        xaxis_title="Stock Price at Expiry",
        yaxis_title="Payoff",
        template="plotly_dark",
        height=450,
    )

    return fig