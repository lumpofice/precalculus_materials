import numpy as np

"""We will construct f(x) = (x-(1/2))/(x**2 - (1/4)) on
[0, 0.5) union (0.5, 1]. Then, we will output the domain and range
data to .table files that LaTeX will use to graph f. Additionally, to highlight
the domain, we will plot a reflection onto the x-axis."""


# Here is our function
f = lambda u: (u-(1/2))/(u**2 - (1/4))


# Here is the domain of our function
xs = [
    np.arange(0, 0.49, 0.01),
    np.arange(0.51, 1, 0.01)
    ]


# Here is how we use the domain and the function definition to generate our
# .table files for LaTeX
for i, j in enumerate(xs):
    with open('rational_0_1_piece_{}.table'.format(i), 'w') as file:
        for u in j:
            if f(u) >= (2/3) and f(u) <= 2:
                file.write('{:f} {:f}\n'.format(u, f(u)))
        

# Function for plotting the reflection onto the x-axis
dom_f = lambda v: 0


# Here is the domain of our function
dom_xs = [
    np.arange(0, 0.49, 0.01),
    np.arange(0.51, 1, 0.01)
    ]


# Here is how we use the domain and the function definition to generate our
# .table files for LaTeX
for s, t in enumerate(dom_xs):
    with open('domain_rational_0_1_piece_{}.table'.format(s), 'w') as file:
        for v in t:
            if v >= 0 and v <= 1:
                file.write('{:f} {:f}\n'.format(v, dom_f(v)))