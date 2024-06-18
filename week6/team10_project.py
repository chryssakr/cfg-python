# CFG Project

import pandas as pd
from scipy.stats import pearsonr # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore
import numpy as np
import os.path
# from kaggle.api.kaggle_api_extended import KaggleApi # type: ignore

def create_dict(df):
    return df.set_index(['year', 'album']).apply(dict, axis=1)

def get_unique_album(df):
    """Gets all the unique TS album"""
    df = df.sort_values(by="release_date") # ensures that album is sorted by release date
    return df["album"].unique()

# TODO it's not used
def album_data_popularity(df):

    # Per album get the avg popularity and put in dict
    for album in album_rows:
        album_rows = df.loc[
            df["album"] == album
        ] # same here as above
        
        album_popularity = {}        
        album_mean_popularity = album_rows.popularity.mean()
        album_mean_popularity = album_rows.speechiness.mean()
        album_mean_popularity = album_rows.dancebility.mean()
        album_mean_popularity = album_rows.temp.mean()
        album_popularity[album] = album_mean_popularity

    return album_popularity

def find_mean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the mean attributes per album.
    I first group by "album" name and then use the agg function to specify
    the "mean" aggregation function for the columns I need

    Args:
        df (pd.DataFrame): DataFrame containing the data.

    Returns:
        pd.DataFrame: DataFrame with columns representing the mean values per album.
    """
    mean_values = df.groupby(["album"]).agg({
        "popularity": "mean",
        "speechiness": "mean",
        "danceability": "mean",
        "energy": "mean",
        "tempo": "mean"
    }).reset_index(drop = True)

    return mean_values

def corr_matrix(dfcorr):
    """Computes a correlation matrix of all numerical variables in the dataset and
        displays a correlation matrix heatmap"""
    print("CORRELATION MATRIX")
    corr_all = dfcorr.corr(
        method = "pearson",
        numeric_only = True).round(4) # rounds all the values up to 4 decimal points

    print(corr_all)

    # Save correlation matrix to file
    with open("results.txt", "a") as file:
        file.write("\nCORRELATION MATRIX\n")
        file.write(corr_all.to_string())
        
    # Correlation Heatmap
    mask = np.triu(np.ones_like(corr_all, dtype=bool))
    sns.heatmap(corr_all,
                annot = True,
                vmax = 1,
                vmin = -1,
                center = 0,
                cmap = 'vlag',
                mask = mask)
    plt.show()

def calc_pearsonr(song_attribute: str, df2: pd.DataFrame) -> tuple[float, float]:
    """
    Calculate the Pearson correlation coefficient and p-value. Correlating x aspect of a song to its popularity.

    Args:
        x (str): A song attribute to correlate with popularity
        df2 (pd.DataFrame): DataFrame with columns "album", "year", "popularity", "speechiness", "danceability", "energy" and "tempo".

    Returns:
        tuple[float, float]: Pearson correlation coefficient and p-value.
    """
    correlation, p_value = pearsonr(df2[song_attribute], df2["popularity"])
    p_value = round(p_value, 4)

    return correlation, p_value

def interpret_correlation(correlation: float, p_value: float) -> dict:
    """
    Interpret the correlation and p-value results.

    Args:
        correlation (float): Pearson correlation coefficient.
        p_value (float): p-value associated with the correlation coefficient.

    Returns:
        dict: A dictionary containing the interpretation results including the relationship type and evidence type.
    """
    results = {}
    if correlation > 0:
        results["relationship"] = {"type": "positive", "message": "As the one variable increases, the other variable increases as well."}
    elif correlation < 0:
        results["relationship"] = {"type": "negative", "message": "As the one variable increases, the other variable decreases."}
    else:
        results["relationship"] = {"type": "no", "message": "The way the variables change is not correlated."}
    if p_value <= 0.05:
        results["evidence"] = {"type": "strong", "message": "A p_value equal to or less than 0.05 indicates that the observed correlation is unlikely to have occurred by chance alone, and there is likely a true correlation in the population."}
    else:
        results["evidence"] = {"type": "weak", "message": "A p_value more than than 0.05 indicates that there may not be a significant correlation present in the population, and the observed correlation could have plausibly occurred by chance."}
    return results

def plot_data(x_axis, y_axis: float, x, y):
  plt.scatter(x_axis,y_axis)
  plt.xlabel(x)
  plt.ylabel(y)
  plt.title(f"{y} and {x}")
  return plt.show()

def main():
    """ Main function """
    # Sets the display function of the print function
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.width', 600)

    # Download file
    file_path = "data/taylor_swift_spotify.csv"
    if not os.path.exists(file_path):
        print("Error: Data file not found.")
        return
    with open(file_path, "r") as f:
        df = pd.read_csv(file_path,
                      usecols=lambda x: x != "Unnamed: 0",
                      parse_dates=["release_date"]).sort_values(by="release_date").reset_index(drop = True)
    df["year"] = df.release_date.dt.year

    # Creates a dictionary of the dataset with year and album as the index (or point of reference)
    album_dict = create_dict(df)
    print(album_dict)

    df2 = df[["album", "year", "popularity", "speechiness", "danceability", "energy", "tempo"]]
    df2 = df2.set_index(["year", "album"])

    # Gets all the unique TS album in the dataset and lists them all.
    albums = get_unique_album(df)

    # save the results to a file
    with open("results.txt", "w") as file:
        file.write(f"This dataset has {len(albums)} albums. They are: \n")
        print(f"This dataset has {len(albums)} albums. They are: ")
        count = 1
        for album in albums:
            file.write(f"{count}. {album}\n")
            print(f"{count}. {album}")
            count = count + 1

    # Calls various functions for data analysis and viz
    mean_values = find_mean(df)
    print(f"The mean values per album\n{mean_values}")
    with open("results.txt", "a") as file:
        file.write(f"\nMean values:\n{mean_values}\n")

    # Creates correlation matrix and displays the correlation heatmap
    dfcorrmatrix = df.drop(["release_date", "track_number", "id", "uri", "duration_ms", "year"],
                           axis=1)
    corr_matrix(dfcorrmatrix)

    # Looks at individual correlations between song attributes and popularity
    print("\n-------Some examples on how to interpret our data:-------")
    with open("results.txt", "a") as file:
        file.write("\n-------Some examples on how to interpret our data:-------\n")
        for song_attribute in df2.drop(["popularity"], axis=1):
            correlation, p_value = calc_pearsonr(song_attribute, df2)
            results = interpret_correlation(correlation, p_value)
            file.write(
                f"\nCorrelating {song_attribute} & popularity.\n"
                f"There is a {results['relationship']['type']} relationship. {results['relationship']['message']}\n"
                f"The evidence of this correlation is {results['evidence']['type']} with a p_value of {p_value}.\n"
                f"{results['evidence']['message']}\n"
            )
            print(
                f"\nCorrelating {song_attribute} & popularity.\n"
                f"There is a {results["relationship"]["type"]} relationship. {results["relationship"]["message"]}\n"
                f"The evidence of this correlation is {results["evidence"]["type"]} with a p_value of {p_value}.\n"
                f"{results["evidence"]["message"]}\n"
                )

if __name__ == "__main__":
    main()