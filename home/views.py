from django.shortcuts import render
from django.http import HttpResponse
import plotly.graph_objects as go
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def home(request):# Sample data for 5 candles
    data = {
        'x': ['2025-01-10', '2025-01-11', '2025-01-12', '2025-01-13', '2025-01-14'],
        'open': [100, 102, 101, 103, 102],
        'high': [105, 104, 102, 106, 107],
        'low': [99, 100, 98, 101, 100],
        'close': [102, 101, 100, 105, 104]
    }

    fig = go.Figure(data=[go.Candlestick(
        x=data['x'],
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close'],
        increasing_line_color='green',
        decreasing_line_color='red',
        name='Candlestick'
    )])
    # Customize layout
    fig.update_layout(title='Candlestick Chart',
                      xaxis_title='Date',
                      margin=dict(l=0, r=0, t=0, b=0),
                      width=650,
                      height=400,
                      autosize=True,
                      yaxis_title='Price')

    # Generate HTML div for the chart
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn', config={'responsive': True})
    return render(request, 'home.html', {'graph': graph_html})
