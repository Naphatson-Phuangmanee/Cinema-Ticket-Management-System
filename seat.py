import pandas as pd


class Seat:
    def __init__(self, seatid, showid):
        self.seatid = seatid
        self.showid = showid

        self.type = None
        self.reserved = None

    def getdata(self):
        """Get seat data by seatid & showid from the csv file"""

        try:
            df = pd.read_csv(f'seats/{self.showid}.csv')
        except FileNotFoundError:
            print(f"Show not found ({self.showid})")
            exit()
        df = df.astype(str)
        data = df.loc[df['seatid'] == self.seatid]
        if not data.empty:
            self.seatid, self.type, self.reserved, = data.values[0]
        else:
            print(f"Seat not found ({self.seatid})")
            exit()

    def update(self):
        """Update seat data into the csv file"""

        df = pd.read_csv(f'seats/{self.showid}.csv')
        df = df.astype(str)
        df.loc[df['seatid'] == self.seatid, 'reserved'] = self.reserved
        df.to_csv(f'seats/{self.showid}.csv', index=False, header=True)

    def __eq__(self, other):
        """Replace == operator
        Check if two seats are the same seat"""

        return self.seatid == other.seatid and self.showid == other.showid
