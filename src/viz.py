import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def map(df, color, hover, title):
    fig = px.choropleth(df, locations='ISO Code', color= color,  hover_name = df.index, hover_data=[hover], title=title)
    return fig.show()

def scatter(df,hdi,title):
    fig = px.scatter(df, x = hdi, y = 'Global Score', color='Region', trendline="ols", trendline_scope="overall", hover_name = df.index, height=500, width=700, title=title)
    return fig.show()

def heat(df):
    df_heatmap = df.drop(['Position 2022', 'Position 2021', 'Change in position', 'Media Workers Imprisoned', 'Media Workers Killed', 'Journalist Imprisoned','Journalist Killed'], axis = 1, inplace = False)
    np.triu(np.ones_like(df_heatmap.corr()))
    fig, ax = plt.subplots(figsize=(8,6))
    mask = np.triu(np.ones_like(df_heatmap.corr(), dtype=bool))
    heatmap = sns.heatmap(df_heatmap.corr(), mask=mask, vmin=-1, vmax=1, annot=True, fmt=".2f")
    heatmap.set_title('Correlation between press freedom and development', fontdict={'fontsize':14}, pad=16)
    fig.savefig("/Users/narea/Desktop/ironhack/project-2/images/heatmap.png")
    return plt.show()