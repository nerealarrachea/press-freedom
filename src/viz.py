import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt

def map(df, color, hover, title):
    fig = px.choropleth(df, locations='ISO Code', color= color,  hover_name = df.index, hover_data=[hover], title=title)
    return fig.show()

def scatter(df,hdi,title):
    fig = px.scatter(df, x = hdi, y = 'Global Score', color='Region', trendline="ols", trendline_scope="overall", hover_name = df.index, height=500, width=700, title=title)
    return fig.show()

def heat(df):
    df_heatmap = df.drop(['Position 2022', 'Position 2021', 'Change in position', 'Media Workers Imprisoned', 'Media Workers Killed', 'Journalist Imprisoned','Journalist Killed'], axis = 1, inplace = False) 
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(df_heatmap.corr(), annot=True, fmt=".2f")
    plt.title('Correlation between press freedom and development')
    return plt.show()