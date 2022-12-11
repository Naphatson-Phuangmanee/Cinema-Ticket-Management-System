import pandas as pd
from show import Show
from seat import Seat


class Ticket:

    def __init__(self, ticketid=None, ownername=None):
        self.ticketid = ticketid
        self.ownerName = ownername
        self.showid = None
        self.seatid = None
        self.show = None
        self.seat = None

    def getdata(self):
        """Get ticket data by ticketid or ownername from the csv file"""
        
        df = pd.read_csv('./tickets.csv')
        df = df.astype(str)
        if self.ticketid is not None:
            data = df.loc[df['ticketID'] == self.ticketid]
        elif self.ownerName is not None:
            data = df.loc[df['ownerName'].str.startswith(self.ownerName)]
            if len(data.values) > 1:
                print(f"{len(data.values)} Occurences found please select one:")
                for ticketid, ownername, _, _ in data.values:
                    print(f"#{ticketid}: {ownername}")
                ticketid = input("Enter ticketid: ")
                data = data.loc[data['ticketID'] == ticketid]
        if not data.empty:
            self.ticketid, self.ownerName, self.showid, self.seatid = data.values[0]
        else:
            print(f"Ticket not found (#{self.ticketid})")
            exit()

    def getdetails(self):
        """Get ticket details by ticketid from the csv file"""

        self.getdata()
        self.show = Show(self.showid)
        self.show.getdata()
        self.seat = Seat(self.seatid, self.showid)
        self.seat.getdata()

        print(f"""
            Ticket #{self.ticketid}
            Owner: {self.ownerName}
            Show: {self.show.movieName} at {self.show.showTime} in Theatre {self.show.theatre}
            Seat: {self.seatid}
                Type: {self.seat.type}
            """)

    def create(self):
        """Create a new ticket generate new ticket id, add record to the csv file and update seat reserved status"""
        if self.ticketid is not None:
            exit()
        # generate new ticket id
        df = pd.read_csv('./tickets.csv')
        df = df.astype(str)
        self.ticketid = int(df['ticketID'].values[-1]) + 1

        self.show = Show(self.showid)
        self.show.getdata()
        self.seat = Seat(self.seatid, self.showid)
        self.seat.getdata()

        print(f"""
            Ticket #{self.ticketid}
            Owner: {self.ownerName}
            Show: {self.show.movieName} at {self.show.showTime} in Theatre {self.show.theatre}
            Seat: {self.seatid}
                Type: {self.seat.type}
            """)
        # write to csv file
        newticket_df = pd.DataFrame([[self.ticketid, self.ownerName, self.showid, self.seatid]],
                                    columns=['ticketID', 'ownerName', 'showID', 'seatID'])
        newticket_df.to_csv('./tickets.csv', mode='a', header=False, index=False)
        
        # update seat status
        self.seat.reserved = 'True'
        self.seat.update()
