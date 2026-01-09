import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import pandas as pd

def set_color_map(color_list):
    """
    Display and register a custom color palette for use in plots.

    This helper function creates a ListedColormap object from a given list
    of color hex codes, displays the palette visually using seaborn, and 
    returns the corresponding Matplotlib colormap object for reuse in 
    other plotting functions.

    Args:
        color_list (list[str]):
            A list of color hex strings (e.g. ["#A5D7E8", "#576CBC", "#19376D"]).

    Returns:
        matplotlib.colors.ListedColormap:
            A Matplotlib ListedColormap object constructed from the input colors.
war
    Example:
        >>> bluishColorList = ["#A5D7E8", "#576CBC", "#19376D", "#0b2447"]
        >>> cmap_custom = set_color_map(bluishColorList)
        >>> # Use cmap_custom in your plot
        >>> plt.scatter(x, y, c=z, cmap=cmap_custom)
    
    Notes:
        - The function prints and displays the color palette for quick visual reference.
        - Designed for use in notebooks and visualization utilities.
    """
    cmap_custom = ListedColormap(color_list)
    print("Notebook Color Schema:")
    sns.palplot(sns.color_palette(color_list))
    plt.show()
    return cmap_custom


# ✅ reusable color themes
bluishColorList = ["#A5D7E8", "#576CBC", "#19376D", "#0b2447"]
warmColorList   = ["#F6C90E", "#F45B69", "#C92C6D", "#7B1E7A"]
warmBlueColorList = ["#F45B69","#A5D7E8"]


def analyze_bins(data, bins=None, binwidth=None):
    """
    Analyze histogram bins and binwidth given numeric data.

    Parameters
    ----------
    data : list or array-like
        Numeric data for which you want to analyze the histogram.

    bins : int, optional
        The number of bins (intervals) to divide the range into.
        If given, 'binwidth' is computed automatically.

    binwidth : float, optional
        The desired width of each bin.
        If given, 'bins' is computed automatically.

    Notes
    -----
    - 'bins' choice is often trial and error.
    - You can approach it two ways:
        1. Divide the range by small integers (3, 5, 7...) → coarser summary.
        2. Multiply the range by small integers (1, 2, 3...) → finer detail.
    """

    data_min, data_max = min(data), max(data)
    data_range = data_max - data_min

    if (bins is None) and (binwidth is None):
        raise ValueError("Please provide either 'bins' or 'binwidth'.")
    if (bins is not None) and (binwidth is not None):
        raise ValueError("Please provide only one: 'bins' OR 'binwidth', not both.")

    if bins is not None:
        binwidth = data_range / bins
    else:
        bins = int(data_range / binwidth)

    print("📊 Histogram Bin Analysis")
    print("-------------------------")
    print(f"Min value     : {data_min}")
    print(f"Max value     : {data_max}")
    print(f"Range         : {data_range}")
    print(f"Number of bins: {bins}")
    print(f"Bin width     : {round(binwidth, 3)}")

  
    # 🔹 Suggested trial bins (multiplying approach)
    print("\n🧩 Suggested bins (Multiply the range):")
    for multiplier in [1, 2, 3]:
        suggested_bins = int(data_range * multiplier)
        print(f"  - range×{multiplier:<2} → {suggested_bins} bins (width ≈ {round(data_range/suggested_bins, 2)})")

    return bins, binwidth


def plot_pivot_bar(
    pivot_df: pd.DataFrame,
    title: str = "title here",
    legendTitle: str = "",
    legendLabels: list = [],
    figsize: tuple = (7, 4),
    width: float = 0.5,
    colorList=bluishColorList
):
    """
    Plot a grouped bar chart from a pivoted DataFrame using Matplotlib.

    Also refer to sns_countplot_pairs

    Parameters
    ----------
    pivot_df : pd.DataFrame
        A pivoted DataFrame where columns represent categories and the 
        index represents groups to be plotted. Each column will be drawn 
        as a separate series of bars.

    title : str, optional
        Title of the plot.

    legend_title : str, optional
        Title displayed above the legend.

    legend_labels : list, optional
        Labels to display in the legend. Must match the number of 
        columns in `pivot_df`.

    figsize : tuple, optional
        Figure size passed to `plt.subplots()`, formatted as (width, height).

    width : float, optional
        Width of the bars in the grouped bar chart.

    Returns
    -------
    plt : module
        The matplotlib.pyplot module, returned for convenience.

    fig : matplotlib.figure.Figure
        The Figure object created by plt.subplots().

    ax : matplotlib.axes.Axes
        The Axes object where all plotting elements are drawn. Useful
        for further customization outside this function.

    Notes
    -----
    Returning (plt, fig, ax) allows the caller to modify the figure 
    further after creation, such as adding additional annotations,
    saving the figure, or adjusting layout settings.
    """


    fig,ax = plt.subplots(1,1,figsize=figsize)
    #print("edited")
    pivot_df.plot(
                    kind='bar',
                    ax=ax,
                    width=width,
                    #color=bluishColorList[:len(pivot_df.columns)],
                    color= colorList[:len(pivot_df.columns)]
    )
    ax.set_title(f"{title}")

    # ✅ Set legend title
    #ax.legend(title=f"{legend_title}",labels=legend_labels)
    ax.legend(title=legendTitle,labels=legendLabels)
    # 👇 rotate x-axis tick labels
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0,ha="center")
    ax.grid(color="black", linestyle="--", linewidth=0.5, alpha=0.6, axis="y", which="major")

    fig.tight_layout()
    #plt.show()
    return (plt,fig,ax)

def plot_hist_hue(data_df,
                    feature,
                    hue="set",
                    bins=25,
                    title="title here",
                    legendTitle="",
                    legendLabels=[],
                    figsize=(7,4),
                    debug=False):
    """
    Also refer to sns_histplot_pairs
    """
    fig, ax = plt.subplots(1,1, figsize=figsize)

    for i, h in enumerate(data_df[hue].unique()):
        
        if pd.isna(h):
            continue

        if debug:
            print(f"--> h: {h}")

        # alpha decreases by 0.1 each iteration, minimum 0.1
        alpha = max(1.0 - 0.1 * i, 0.1)

        ax.hist(
            data_df.loc[data_df[hue] == h, feature],
            bins=bins,
            edgecolor='black',
            color=bluishColorList[i],
            alpha=alpha
        )

    ax.set_title(title)
    ax.legend(title=legendTitle,labels=legendLabels)
    ax.set_xlabel(feature)
    ax.set_ylabel("Frequency")
    ax.grid(color="black",alpha=0.7 ,linestyle="-.", linewidth=0.5, axis="y", which="major")
    fig.tight_layout()
    #plt.show()
    return (plt,fig,ax)

def sns_pivot_heatmap(
        df_pivot:pd.DataFrame,
        title:str="title here",
        xLabel:str="xlabel here",
        yLabel:str="ylabel here",
        figsize:tuple=(6,5),
        width:float=0.5,
        fmt="d",
        cmap="Blues"
):
    # ---- HEATMAP ----
    fig, ax = plt.subplots(figsize=figsize)

    sns.heatmap(
        df_pivot,
        ax=ax,
        annot=True,
        fmt=fmt,
        cmap=cmap,
        linewidths=width,
        linecolor="gray"
    )

    ax.set_title(title, fontsize=14)
    ax.set_ylabel(yLabel)
    ax.set_xlabel(xLabel)

    # ---- FULL BORDER AROUND HEATMAP ----
    for _, spine in ax.spines.items():
        spine.set_visible(True)
        spine.set_linewidth(1.0)
        spine.set_edgecolor("gray")

    fig.tight_layout()
    #plt.show()
    return (plt,fig,ax)

def sns_countplot_pairs(
    data_df,
    feature,
    hue="set",
    title="title here 2",
    figsize=(7, 4),
    width=0.5
):
    """
    Also refer to plot_pivot_pairs

    Plot grouped categorical counts using Seaborn's countplot.

    This function creates a side-by-side bar chart (pairs of bars)
    to compare category frequencies across groups (e.g., 'train' vs 'test',
    'male' vs 'female'). It is called *pairs* because each category on the x-axis
    is represented by paired bars — one for each hue level.

    This visualization is particularly useful in **machine learning workflows**
    to compare feature distributions between training and testing datasets,
    ensuring that both subsets are representative and not biased.
    It can also be applied to other comparative analyses such as A/B tests,
    demographic splits, or experimental group comparisons.

    Parameters
    ----------
    data_df : pandas.DataFrame
        The input DataFrame containing the categorical data to visualize.
    feature : str
        The column name to display on the x-axis.
    title : str
        The title of the plot.
    hue : str, default "set"
        The column used to create grouped bars (color-coded by hue levels).

        In Seaborn, the `hue` parameter splits data by a categorical variable
        and assigns different colors to each subgroup. It effectively adds a 
        third dimension to the plot — allowing comparisons across both the 
        main category (`x`) and subgroup (`hue`). For example, if `x="Sex"` 
        and `hue="set"`, each gender will display two bars side by side, 
        representing 'train' and 'test' groups.
    figsize : tuple, default (7, 4)
        Figure size in inches, passed to Matplotlib’s `plt.subplots`.
    width : float, default 0.5
        Width of the bars in the Seaborn countplot.

    Notes
    -----
    - This function is generic and can be used for any dataset with a categorical
      feature and a grouping variable.
    - In machine learning, use it to visually validate train/test splits or
      compare categorical feature distributions between datasets.
    - In analytics, it works well for visualizing counts across demographic
      groups or experimental conditions.

    Example
    -------
    >>> sns_countplot_pairs(df, feature="Sex", title="Passenger Distribution", hue="set")
    """

    f, ax = plt.subplots(1, 1, figsize=figsize)
    sns.countplot(
        data=data_df,
        x=feature,
        hue=hue,
        ax=ax,
        palette=bluishColorList[:2],
        width=width
    )
    plt.grid(color="black", linestyle="-.", linewidth=0.5, axis="y", which="major")
    ax.set_title(title)
    plt.show()



    


def sns_histplot_pairs(data_df,feature,hue="set",bins=25,title="title here",figsize=(7,4)):
    """
    Also refer to plot_hist_pairs
    """
    fig,ax = plt.subplots(1,1,figsize=figsize)

    for i,h in enumerate(data_df[hue].unique()):
        sns.histplot(data=data_df[data_df[hue] == h],  # 👈 filter inside the data arg
                         x=feature,                        # 👈 tell Seaborn which column to use
                         ax=ax,
                         bins=bins,
                         color=bluishColorList[i],
                         label=h
                        )
        # sns.histplot(data_df.loc[data_df[hue]==h,feature],
        #                     ax=ax,
        #                     bins=bins,
        #                     color=bluishColorList[i]
        #                )
    ax.set_title(title)
    ax.legend(title=hue)
    plt.show()


def plot_hist_pairs(data_df,feature,hue="set",bins=25,title="title here",title_legend="title legend here",figsize=(7,4)):
    """
    Also refer to sns_histplot_pairs
    """
    fig,ax = plt.subplots(1,1,figsize=figsize)

    for i,h in enumerate(data_df[hue].unique()):
        ax.hist(data_df.loc[data_df[hue]==h,feature],
                bins=bins,
                edgecolor='black',
                color=bluishColorList[i],
                label=h
            )

    ax.set_title(f"{title}")
    #ax.legend(title="Set")
    ax.legend(title=title_legend)
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    fig.tight_layout()
    plt.show()