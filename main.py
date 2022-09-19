import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np

N = 1000
x = np.linspace(0, 1, N)
z = 20 * np.sin(2 * np.pi * 3 * x) + 100 * np.exp(x)
error = 10 * np.random.randn(N)
t = z + error

M = 100
F = []
for i in range(0, N):
    f = [x[i] ** j for j in range(0, M + 1)]
    F.append(f)
F = np.array(F)
MP = np.linalg.pinv(F)
W = MP.dot(t)
Y = F.dot(W)

M = 10
FF = np.empty((N, M + 1))
for i in range(0, N):
    for j in range(0, M + 1):
        if j % 2 == 0:
            FF[i][j] = np.cos((j // 2) * x[i])
        else:
            FF[i][j] = np.sin(((j // 2) + 1) * x[i])
FF = np.array(FF)
MPf = np.linalg.pinv(FF)
Wf = MPf.dot(t)
Yf = FF.dot(Wf)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=Y, name='y(x, w)'))
fig.add_trace(go.Scatter(x=x, y=z, name='z(x)'))
fig.add_trace(go.Scatter(x=x, y=t, mode="markers", name='target'))
fig.update_layout(title="Polynom deg 1")
# fig.show()
fig.write_html("C:/Users/26067/PycharmProjects/ML1/pol100.html")

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=Yf, name='y(x, w)'))
fig.add_trace(go.Scatter(x=x, y=z, name='z(x)'))
fig.add_trace(go.Scatter(x=x, y=t, mode="markers", name='target'))
fig.update_layout(title="Fourier deg 1")
# fig.show()
fig.write_html("C:/Users/26067/PycharmProjects/ML1/four10.html")
