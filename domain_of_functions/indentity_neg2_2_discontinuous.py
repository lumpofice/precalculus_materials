import numpy as np

"""We will construct f(x) = x, piecewise, on
[-2, 0] union [0.5, 2]. Then, we will output the domain and range
data to .table files that LaTeX will use to graph f. Additionally, to highlight
the domain, we will plot a reflection onto the x-axis."""


# Here is our function
f = lambda u: u


# Here is the domain of our function
xs = [
    np.arange(-2, 0, 0.01),
    np.arange(0.5, 2, 0.01)
    ]


# Here is how we use the domain and the function definition to generate our
# .table files for LaTeX
for i, j in enumerate(xs):
    with open('identity_neg2_2_discontinuous_piece_{}.table'.format(i),\
        'w') as file:
        for u in j:
            if f(u) >= -2 and f(u) <= 2:
                file.write('{:f} {:f}\n'.format(u, f(u)))
        

# Function for plotting the reflection onto the x-axis
dom_f = lambda v: 0


# Here is the domain of our function
dom_xs = [
    np.arange(-2, 0, 0.01),
    np.arange(0.5, 2, 0.01)
    ]


# Here is how we use the domain and the function definition to generate our
# .table files for LaTeX
for s, t in enumerate(dom_xs):
    with open('domain_identity_neg2_2_discontinuous_piece_{}.table'.format(s),\
        'w') as file:
        for v in t:
            if v >= -2 and v <= 2:
                file.write('{:f} {:f}\n'.format(v, dom_f(v)))