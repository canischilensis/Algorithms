#https://medium.com/science-spectrum/fractals-in-code-exploring-the-mandelbrot-set-with-python-be313888cd2c

import numpy as np
import matplotlib.pyplot as plt

def create_mandelbrot_set(width=800, height=800, max_iterations=256):
    """
    Function to compute the Mandelbrot set.

    Params
    ------
    width: width of the image
    height: height of the image
    max_iterations: max number of iterations to check for divergence

    Returns
    -------
    2D array representing the Mandelbrot set
    """
    # Define the complex plane
    x_axis = np.linspace(-2, 2, width)
    y_axis = np.linspace(-2, 2, height)
    x, y = np.meshgrid(x_axis, y_axis)
    C = x + 1j * y
   
    # Initialize arrays.
    z = np.zeros(C.shape, dtype=complex)
    mandelbrot_set = np.zeros(C.shape, dtype=int)
    
    # Determine the iteration count for points in the plane.
    for i in range(max_iterations):
        # Remove points that have already diverged.
        mask = np.abs(z) < 2

        # Apply the Mandelbrot Set formula.
        z[mask] = z[mask] ** 2 + C[mask]

        # Increment the iteration count for points still in the set.
        mandelbrot_set[mask] += 1

    return mandelbrot_set

def plot_mandelbrot_set(mandelbrot_set, figsize=(6, 6)):
    """
    Function to plot the Mandelbrot set.

    Params
    ------
    mandelbrot_set: 2D array of iteration counts
    figsize: figure size for the plot
    """
    plt.figure(figsize=figsize)
    plt.title('Mandelbrot Set')
    plt.xlabel("Real(C)")
    plt.ylabel("Imaginary(C)")   
    plt.imshow(mandelbrot_set, cmap='twilight_shifted')
    plt.show()

if __name__ == "__main__":
    # Generate the Mandelbrot Set.
    mandelbrot = create_mandelbrot_set()
    
    # Plot the Mandelbrot Set.
    plot_mandelbrot_set(mandelbrot)