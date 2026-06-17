import plotly.graph_objects as go


def convergence_plot(convergence_prices, black_scholes_price):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=list(range(1, len(convergence_prices) + 1)),
            y=convergence_prices,
            mode="lines",
            name="Monte Carlo",
        )
    )

    fig.add_hline(
        y=black_scholes_price,
        line_dash="dash",
        annotation_text="Black-Scholes",
    )

    fig.update_layout(
        title="Monte Carlo Convergence",
        xaxis_title="Number of Simulations",
        yaxis_title="Estimated Option Price",
        template="plotly_dark",
        height=450,
    )

    return fig