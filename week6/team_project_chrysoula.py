import pandas as pd
from pprint import pprint

# Get average speechiness and danceability per album
def find_mean_speechiness_danceability(df):
    album_info = {}
    album_start = 0
    # I start from 1 because I'm comparing the current album with the previous
    # in that way I won't go out of the bounds
    for i in range(1, len(df["album"])):
        # When the name of the album changes means I've reached the end of the album
        # So I can now find the mean speechiness and danceability of the album
        if df["album"][i] != df["album"][i - 1]:
            album_end = i - 1
            album_mean_speechiness = df.loc[album_start:album_end, "speechiness"].mean()
            album_mean_speechiness = round(album_mean_speechiness, 4) # rounding to 4 digits
            
            album_mean_danceability = df.loc[album_start:album_end, "danceability"].mean()
            album_mean_danceability = round(album_mean_danceability, 4) # rounding to 4 digits
            
            # I store the mean values in a dictionary
            album_means = dict([("speechiness", album_mean_speechiness), ("danceability", album_mean_danceability)])
            # I store everything in another dictionary with the name of the album as key
            # and the mean values dictionary as the value
            album_info[df["album"][album_start]] = album_means
            # I set the first position of the next album as the start for the next iteration
            album_start = i
    return album_info

def main():
    df = pd.read_csv("data/taylor_swift_spotify.csv")
    album_info = find_mean_speechiness_danceability(df)
    pprint(album_info) # pretty print
    
if __name__ == "__main__":
    main()