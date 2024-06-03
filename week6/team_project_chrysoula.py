"""
before running the program install these libraries if you don't have them
run this on the terminal:
pip install pandas
pip install scipy
"""
import os
import pandas as pd
# ignore type because scipy.stats library does not have library stubs
from scipy.stats import pearsonr # type: ignore

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

# Calculate the Pearson correlation coefficient (PCC)
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
        
    mean_values = find_mean_speechiness_danceability(df)
    correlation, p_value = calc_pearsonr(mean_values)
    results = interpret_correlation(correlation, p_value)
    print("I correlated the mean speechiness and danceability per album of Taylor Swift.\n")
    print(f"The mean speechiness and danceability per album: \n{mean_values}\n")
    print(f"There is a {results["relationship"]["type"]} relationship. {results["relationship"]["message"]}\n")
    print(f"The evidence of this correlation is {results["evidence"]["type"]} with a p_value of {p_value}. {results["evidence"]["message"]}")

if __name__ == "__main__":
    main()