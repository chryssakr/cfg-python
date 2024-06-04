"""
before running the program install these libraries if you don't have them
run this on the terminal:
pip install pandas
pip install scipy
pip install kaggle
pip install matplotlib
pip install seaborn
"""
import os
import pandas as pd
# ignore type because some libraries do not have library stubs
from scipy.stats import pearsonr # type: ignore
import matplotlib.pyplot as plt # type: ignore
import scipy # type: ignore
import seaborn as sns # type: ignore
from kaggle.api.kaggle_api_extended import KaggleApi # type: ignore
import numpy as np

# Chrysoula
def find_mean_speechiness_danceability(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the mean speechiness and danceability per album.
    I'm using groupby() pandas function to calculate the mean speechiness
    and danceability per album
    I first group by "album" name and then use the agg function to specify
    the "mean" aggregation function for the "speechiness" and "danceability" columns
    
    Args:
        df (pd.DataFrame): DataFrame containing the data with columns "album", "speechiness", and "danceability".

    Returns:
        pd.DataFrame: DataFrame with columns "album", "mean_speechiness", and "mean_danceability" representing the mean values per album.
    """
    mean_values = df.groupby("album").agg({
        "speechiness": "mean",
        "danceability": "mean"
    }).reset_index() # this is creating an index column  
    return mean_values

# Chrysoula
def calc_pearsonr(mean_values: pd.DataFrame) -> tuple[float, float]:
    """
    Calculate the Pearson correlation coefficient and p-value between mean speechiness and danceability.

    Args:
        mean_values (pd.DataFrame): DataFrame with columns "album", "mean_speechiness", and "mean_danceability".

    Returns:
        tuple[float, float]: Pearson correlation coefficient and p-value.
    """
    correlation, p_value = pearsonr(mean_values["speechiness"], mean_values["danceability"])
    p_value = round(p_value, 4)
    return correlation, p_value

# Chrysoula
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

# Rose
def album_data_tempo_(df):
    # Get all albums in dataset
    albums = df.album.unique()
    # get together the unique data of the albums from the data set
    album_tempos = {} # make a dictionary for the mean tempos

    # Per album get the avg tempo and put in dict
    for album in albums:
        album_rows = df.loc[
            df["album"] == album # locate the album in the data, use only that albums data
        ]

        album_mean_tempo = album_rows.tempo.mean() # rows that have tempo
        album_tempos[album] = album_mean_tempo # get the mean tempo of the albums

    return album_tempos

# Rose
def album_data_popularity_(df):
    # Get all albums in dataset
    albums = df.album.unique()
    album_popularity = {}

    # Per album get the avg popularity and put in dict
    for album in albums:
        album_rows = df.loc[
            df["album"] == album
        ] # same here as above

        album_mean_popularity = album_rows.popularity.mean()
        album_popularity[album] = album_mean_popularity

    return album_popularity

# Camille

"""
note: df["<var>"] gives you a series while df[["<var>"]] returns a dataframe
"""
"""
Column names for reference:
Index(['name', 'album', 'release_date', 'track_number', 'id', 'uri',
       'acousticness', 'danceability', 'energy', 'instrumentalness',
       'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'popularity',
       'duration_ms', 'year'],
      dtype='object')
"""

# Camille
def check_file():
    """Checks if the file exists in the project root file"""
    data_file = "CFGProject/taylor_swift_spotify.csv"
    if os.path.exists(data_file):
        print("Found dataset archive, loading file...")
        load_file()
        return
    else:
        print("Dataset not found, using kaggle-api tool for download")
        download_file()

# Camille
def download_file():
    """Downloads file via Kaggle API"""
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file("jarredpriester/taylor-swift-spotify-dataset",
                              "taylor_swift_spotify.csv")

# Camille
def load_file():
    """Loads the file but initially checks whether the file exists in the project root directory
       through the check_file() function."""
    check_file()

    # reads the csv, drops the Unnamed: 0 column, converts release_date's data type, sets index but does not drop it from the dateframe
    df = (pd.read_csv("taylor_swift_spotify.csv",
                      usecols=lambda x: x != "Unnamed: 0",          # drops the "Unnamed: 0" column
                      parse_dates=["release_date"])                 # automatically converts release_date into a datetime data type
          .sort_values(by="release_date")                           # sorts the dataframe by release_date
          .set_index("album", drop=False))                    # sets album as index but keeps it in the dataframe

    # creates the year variable
    df["year"] = df.release_date.dt.year

    # concise data type and non-null count summary of the entire dataframe
    # print(df.info())

    # gets all the unique TS album in the dataset
    ts_albums = get_unique_album(df)

    return (df)

# Camille
def get_unique_album(df):
    """Gets all the unique TS album"""
    df = df.sort_values(by="release_date")                          # ensures that album is sorted by release date
    return df["album"].unique()

# Camille
def basic_stat(df):
    """Prints basic statistics
       note: Can be extended to include other variables"""
    print("BASIC STATS:")
    print(df.groupby(df.year)[["energy", "popularity"]].agg(["mean", "min", "max"]))
    print(df.groupby(df.index)[["energy", "popularity"]].agg(["mean", "min", "max"]))

# Camille
def corr_matrix(dfcorr):
    """Computes a correlation matrix of all numerical variables in the dataset and
        displays a correlation matrix heatmap"""
    print("CORRELATION MATRIX")
    corr_all = dfcorr.corr(
        method = "pearson",
        numeric_only = True).round(4)                               # rounds all the values up to 4 decimal points

    print(corr_all)

    #Option 1 for heatmap
    sns.heatmap(corr_all, annot = True, cmap = "coolwarm")
    plt.show()

    #Option 2 for heatmap
    mask = np.triu(np.ones_like(corr_all, dtype=bool))
    sns.heatmap(corr_all,
                annot = True,
                vmax = 1,
                vmin = -1,
                center = 0,
                cmap = 'vlag',
                mask = mask)

    plt.show()

# Camille
def energy_popularity(df):
    """Computes the correlation between energy and popularity

    Alternative method for getting correlation using pearson's / simpler version
    r, p = scipy.stats.pearsonr(df["energy"], df["popularity"])
    print(r)
    print(round(p, 4))

    """

    #x = energy, y = popularity
    slope, intercept, r, p, stderr = scipy.stats.linregress(df["energy"], df["popularity"])
    print(f"Slope: {slope} \n"
          f"Intercept {intercept} \n"
          f"r: {r}\n"
          f"p-value: {round(p,4)}\n"
          f"Standard Error: {stderr}")

    #plot_line_corr(df["energy"], df["popularity"], intercept, slope, "energy","population")
    corr_interpret(r,p,"energy","popularity")

    df["pop_avg_per_album"] = df.groupby(df.index)["popularity"].transform("mean")
    df["energy_avg_per_album"] = df.groupby(df.index)["energy"].transform("mean")
    df["pop_avg_per_year"] = df.groupby(["year"])["popularity"].transform("mean")
    df["energy_avg_per_year"] = df.groupby(["year"])["energy"].transform("mean")
    print(df[["popularity", "energy"]].agg(["mean", "min", "max"])) #returns a dataframe of stat

    print(f"")

    #print(min(df["pop_avg_per_album"]))

    return (df)

# Camille
def corr_interpret(r:float,p:float,x:str,y:str):
    """ Interprets the correlation
        note: Can be used for the interpretation of other variables"""
    if r > 0:
        print(f"There is a positive correlation between {x} and {y}")
    elif r == 0:
        print("There is no correlation between the two")
    elif r < 0:
        print(f"There is a negative correlation between {x} and {y}")

    if p <= 0.05:
        print(f"The p-value is p <= 0.05.")
    elif p == 0:
        print(f"The p-value = 0 hence no linear relationship exists between {x} and {y}.")
    elif p >= 0.05:
        print(f"The p-value is p >= 0.05.")

# Camille
def plot_line_corr(x_axis: float, y_axis: float, intercept: float, slope: float, x:str,y:str):
    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis, linewidth=0, marker='s', label='Data points')
    ax.plot(x_axis, intercept + slope * x_axis, label="line")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(facecolor='white')
    plt.show()

# Camille
def main_data_analysis():
    """ Main function """
    # sets the display function of the print function
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.width', 600)

    # download file
    df = load_file()

    # calls various functions for data analysis and viz
    basic_stat(df)
    dfcorrmatrix = df.drop(["release_date", "track_number", "id", "uri", "duration_ms", "year"],
                           axis=1)
    corr_matrix(dfcorrmatrix)
    energy_popularity(df)

def main():
    """
    Perform analysis on Taylor Swift's Spotify data.

    Reads the data, calculates mean speechiness and danceability per album, 
    calculates the Pearson correlation coefficient and p-value,
    and interprets the correlation results.
    """
    # check if the file exists
    file_path = "data/taylor_swift_spotify.csv"
    if not os.path.exists(file_path):
        print("Error: Data file not found.")
        return
    with open(file_path, "r") as f:
        df = pd.read_csv(f)
        
    # Chryssa's main
    mean_values = find_mean_speechiness_danceability(df)
    correlation, p_value = calc_pearsonr(mean_values)
    results = interpret_correlation(correlation, p_value)
    print(
        "\n----------Chrysoula's Analysis----------\n"
        "I correlated the mean speechiness and danceability per album of Taylor Swift.\n"
        f"The mean speechiness and danceability per album: \n{mean_values}\n"
        f"There is a {results["relationship"]["type"]} relationship. {results["relationship"]["message"]}\n"
        f"The evidence of this correlation is {results["evidence"]["type"]} with a p_value of {p_value}. {results["evidence"]["message"]}\n"
    )

    # Rose's main
    album_data = album_data_popularity_(df)
    album_data = album_data_tempo_(df)
    print("\n----------Rose's Analysis----------\n")
    print(album_data)
    
    Y = list(album_data_popularity_(df).values())
    X = list(album_data_tempo_(df).values())
    
    new_data = pd.DataFrame([X,Y])

    plt.scatter(X,Y)
    plt.show()
    
    # Camille's main
    "\n----------Camille's Analysis----------\n"
    main_data_analysis()
    
if __name__ == "__main__":
    main()
