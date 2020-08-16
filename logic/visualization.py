import plotly.express as px


def fig_ensemble(data):
    fig = px.histogram(data,
                       x='value',
                       nbins=len(data.value.unique()),
                       template='plotly_dark'
                       )
    fig.update_layout(title_text='Histogram Sentiment Analysis',
                      bargap=0.3)
    fig.show()
