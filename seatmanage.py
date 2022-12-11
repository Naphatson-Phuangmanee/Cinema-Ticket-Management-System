import pandas as pd
from seat import Seat
from termcolor import colored
import glob


class SeatManage:

    def __init__(self, showid=0):
        self.showid = showid
        self.seatlist = []

    def getavaliableseats(self):
        """Get avaliable seats from the showid.csv file"""
        try:
            df = pd.read_csv(f'./seats/{self.showid}.csv')
        except FileNotFoundError:
            print(f"Show not found ({self.showid})")
            exit()
        df = df.astype(str)
        avaliable_seats = df.loc[df['reserved'] == 'False']['seatid'].values
        for seat in avaliable_seats:
            self.seatlist.append(Seat(seat, self.showid))
        for seat in self.seatlist:
            seat.getdata()
            if seat.type == 'common':
                print(colored(seat.seatid, 'green'))
            elif seat.type == 'VIP':
                print(colored(seat.seatid, 'yellow'))

    def getallseats(self):
        """Get all seats from the all of the showid.csv file"""
        if self.showid != 0:
            exit()
        for f in glob.glob('./seats/*.csv'):
            df = pd.read_csv(f)
            df = df.astype(str)
            showid = f.split('/')[2].split('.')[0]
            avaliable_seats = df['seatid'].values
            for seat in avaliable_seats:
                self.seatlist.append(Seat(seat, showid))
        return self.seatlist
