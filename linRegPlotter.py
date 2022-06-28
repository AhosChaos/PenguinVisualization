import pandas as pd
import seaborn as sns
import numpy as np

def lin_reg_plotter(x,y,x_label,y_label,ax):
    """
    This is not a wrapper function.  This function passes two 1D arrays to
    sns.regplot with their labels.  This is not a wrapper function.
    x : 1D numpy array 
    y : 1D numpy array 
    x_label : string name for x axis
    y_label : string name for y axis
    ax : matplotlib Axes to draw the plot on

    return:
    matplotlib Axes
    """
    data = np.concatenate((x, y), axis=1)
    df = pd.DataFrame(data=data, columns=[x_label, y_label])
    return sns.regplot(x=x_label,y=y_label,data=df, ax=ax)

def resid_plotter(x,y,x_label,y_label,ax):
    """
    This is not a wrapper function.  This function passes two 1D arrays to
    sns.residplot with their labels.  This is not a wrapper function.
    x : 1D numpy array 
    y : 1D numpy array 
    x_label : string name for x axis
    y_label : string name for y axis
    ax : matplotlib Axes to draw the plot on

    return:
    matplotlib Axes
    """
    data = np.concatenate((x, y), axis=1)
    df = pd.DataFrame(data=data, columns=[x_label, y_label])
    return sns.residplot(x=x_label,y=y_label,data=df, ax=ax)


if __name__ == "__main__":
    pass