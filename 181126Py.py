import numpy as np
from qutip import *

q1 = basis(2, 0)
q2 = basis(2, 1)

q3 = tensor(q1, q2)

# sigmax() portas quanticas
# sigmay()
# sigmaz()

H = hadamard_transform(1)
I = qeye(2)

HI = tensor(H,I)
resultado = HI *q3

sx = sigmax()
delta = 0.1 * 3 * np.pi
h = -delta / 2.0 * sx
