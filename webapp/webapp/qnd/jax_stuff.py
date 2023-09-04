import jax.numpy as jnp
from jax import grad 
from jax import random
import torch
from torch.distributions import Normal

x =  torch.tensor(torch.rand(2,2), requires_grad=True)
w =  torch.tensor(torch.rand(2,2), dtype = torch.complex64)
v = torch.tensor(torch.rand(2,1), requires_grad=True)
def reccur_fun(z):
    for i in range(3):
        z = torch.square(z)
    z = Normal(z, 1).rsample()
    z = torch.fft.fft(torch.matrix_exp(z*0.01)@v)
    return z

y = torch.norm(torch.matmul(w, reccur_fun(x)))
y.backward() # dy/dx
print(x.grad) # grad of y w.r.t x at the current value of x


key = random.PRNGKey(0)
y= random.uniform(key)

# def f (x):
#     y = jnp.square(x)
#     return y

def g (z):
    for i in range(3):
        z = jnp.square(z)
    return z

# random.normal(key)
# twox = grad(f, 0)
# print(twox(2.0))

gradg = grad(g)
print(gradg(1.))
