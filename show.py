import pandas as pd


class Show:

    def __init__(self, showid=0):
        self.showid = showid
        self.theatre = None
        self.movieName = None
        self.showTime = None
        self.duration = None

    def getdata(self):
        """Get show data by showid from the csv file"""
        df = pd.read_csv('shows.csv')
        df = df.astype(str)
        data = df.loc[df['showID'] == self.showid]
        if not data.empty:
            _, self.theatre, self.movieName, self.showTime, self.duration = data.values[0]
            # print(f"Show {self.movieName}({self.showid}) at {self.showTime} fetched successfully")
        else:
            print(f"Show not found ({self.showid})")
            exit()

    def getshowlist(self):
        """Get all shows avaliable from the csv file"""
        df = pd.read_csv('shows.csv')
        df = df.astype(str)
        print("Shows:")
        shows = df.values
        for show in shows:
            print(f"{show[0]}: {show[2]} at {show[3]} (Theater {show[1]})")
        