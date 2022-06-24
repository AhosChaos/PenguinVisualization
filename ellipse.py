import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
import numpy as np

def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)


def scatter_with_ellipse(x, y, ax, x_ax="", y_ax="",p_label="",color="blue", n_std=[3.0], c_std=['firebrick'], set_label=False, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    x_ax : string
        The name of the x-axis
        
    y_ax : string
        The name of the y-axis
    p_label : string
        The label for the scatter plot points
    color : string
        The color to use for the scatter plot

    n_std : [float]
        The list of the number of standard deviations to determine the ellipse's radiuses.
    
    c_std : []
        The list of the colors to use for each standard deviation
    
    set_label : bool
        Boolean to determine whether the confidence ellipses should be labelled
    
    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------

    """
    if len(c_std) != len(n_std):
        raise IndexError("Length of c_std and n_std must match")
    if p_label != "":
        ax.scatter(x, y, color=color, label = p_label)
    else:
        ax.scatter(x, y, color=color)
    for i in range(len(n_std)):
        if set_label:
            confidence_ellipse(x, y, ax, n_std=n_std[i], label=fr'${n_std[i]}\sigma$', edgecolor=c_std[i])
        else:
            confidence_ellipse(x, y, ax, n_std=n_std[i], edgecolor=c_std[i])

    mu_x = x.mean()
    mu_y = y.mean()
    ax.scatter(mu_x,mu_y, marker="x")
    if x_ax != "" and y_ax != "":
        ax.set_xlabel(x_ax)
        ax.set_ylabel(y_ax)
    
    return
    


