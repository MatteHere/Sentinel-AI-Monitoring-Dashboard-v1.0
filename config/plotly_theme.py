import plotly.graph_objects as go


def apply_plotly_theme(fig, title):
    fig.update_layout(
        title=dict(
            text=title,
            x=0.02,
            xanchor="left",
            font=dict(
                size=18,
                color="#111827",
                family="Inter",
            ),
        ),

        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",

        font=dict(
            color="#111827",
            family="Inter",
            size=12,
        ),

        margin=dict(
            l=45,
            r=25,
            t=60,
            b=40,
        ),

        hoverlabel=dict(
            bgcolor="#FFFFFF",
            bordercolor="#E5E7EB",
            font=dict(color="#111827"),
        ),

        legend=dict(
            orientation="h",
            y=1.05,
            x=1,
            xanchor="right",
            bgcolor="rgba(255,255,255,0)",
            font=dict(color="#111827"),
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        linecolor="#CBD5E1",
        tickfont=dict(color="#334155"),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="#E5E7EB",
        zeroline=False,
        linecolor="#CBD5E1",
        tickfont=dict(color="#334155"),
    )

    return fig