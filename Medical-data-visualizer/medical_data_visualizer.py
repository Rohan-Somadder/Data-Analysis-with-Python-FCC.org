import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(
    r'Data Analysis with Python-FCC.org\Medical-data-visualizer\medical_examination.csv')
# print(df)

# Add 'overweight' column
df['overweight'] = ((df['weight']/((df['height']/100)**2)) > 25)
# print(df)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, df['cholesterol'])
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, df["cholesterol"])
# print(df['cholesterol'].value_counts())

df['gluc'] = np.where(df['gluc'] == 1, 0, df['gluc'])
df['gluc'] = np.where(df['gluc'] > 1, 1, df["gluc"])
# print(df['gluc'].value_counts())
# print(df)
# Draw Categorical Plot


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=[
                     'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # print(df_cat)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(
        df_cat.groupby(['cardio', 'variable', 'value'])['value'].count()).rename(columns={'value': 'total'}).reset_index()
    # print(df_cat)

    # Draw the catplot with 'sns.catplot()'
    f = sns.catplot(x='variable', y='total', hue='value',
                    col='cardio', data=df_cat, kind='bar')
    fig = f.fig

    # Do not modify the next two lines
    fig.savefig(
        r'Data Analysis with Python-FCC.org\Medical-data-visualizer\catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df["ap_lo"] <= df["ap_hi"]) & (df["height"] >= df["height"].quantile(0.025)) & (df["height"] <= df["height"].quantile(
        0.975)) & (df["weight"] >= df["weight"].quantile(0.025)) & (df["weight"] <= df["weight"].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, vmax=.25, fmt=".1f", center=0, square=True,
                     linewidths=.5, cbar_kws={"shrink": .45, "format": "%.2f"}, vmin=-0.1, annot=True)
    
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
