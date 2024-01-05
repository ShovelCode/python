import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)

X, Y = np.meshgrid(x, y)

Z = X + 1j * Y #Grid of complex numbers

def f(z):
    return z ** 2

output = f(Z)

plt.imshow(np.abs(output), extent=[-2, 2, -2, 2], cmap='viridis')
plt.colorbar(label='Magnitude')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Magnitude of f(z) = z^2')
plt.show() #plots the magnitude

#plotting the phase
plt.imshow(np.angle(output), extent=[-2, 2, -2, 2], cmap='twilight')
plt.colorbar(label='Phase')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Phase of f(z) = z^2')
plt.show()

