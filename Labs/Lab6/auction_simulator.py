"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def _notify_bidders(self, bidder):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        [x(self) for x in self.bidders if x != bidder]

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid > self._highest_bid:
            self._highest_bid = bid
            self._highest_bidder = bidder
            self._notify_bidders(bidder)

    def get_highest_bid(self):
        return self._highest_bid

    def get_highest_bidder(self):
        return self._highest_bidder

    def print_bidders(self):
        print("Highest bids per bidder")
        [print(x) for x in self.bidders]


class Bidder:

    def __init__(self, name, budget=100, bid_probability=0.35, bid_increase_perc=1.1):
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer):
        consider_bidding = random.random() < (self.bid_probability-0.01)
        new_bid = auctioneer.get_highest_bid() * self.bid_increase_perc
        if consider_bidding and self.budget >= new_bid:
            self.highest_bid = new_bid
            auctioneer.accept_bid(new_bid, self)

    def __str__(self):
        return "Bidder: " + self.name + "  Highest Bid: " + str(self.highest_bid)


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        auctioneer = Auctioneer()
        [auctioneer.register_bidder(x) for x in bidders]
        self._auctioneer = auctioneer

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        print("Auctioning " + item + " starting at " + str(start_price))
        self._auctioneer.accept_bid(start_price, None)
        winner = self._auctioneer.get_highest_bidder()
        final_price = self._auctioneer.get_highest_bid()
        print("The winner of the auction is: " + winner.name + " at " + str(final_price))
        self._auctioneer.print_bidders()


def main():
    bidders = [Bidder("Jojo", 3000, random.random(), 1.2), Bidder("Melissa", 7000, random.random(), 1.5),
               Bidder("Priya", 15000, random.random(), 1.1), Bidder("Kewei", 800, random.random(), 1.9),
               Bidder("Scott", 4000, random.random(), 2)]

    initial_input = None
    while initial_input != 3:
        print("Enter 1 to run the hardcoded test auction")
        print("Enter 2 for manual input")
        initial_input = int(input("Enter 3 to stop the program\nSelection: "))
        if initial_input == 1:
            print("\n\nStarting Auction!!")
            print("------------------")
            my_auction = Auction(bidders)
            my_auction.simulate_auction("Antique Vase", 100)
        elif initial_input == 2:
            print("Fill in the following fields.")
            item_name = input("Name of the item: ")
            start_price = int(input("Starting price: "))
            num_bidders = input("Number of bidders: ")
            num_created = 0
            manual_bidders = []
            while num_created < int(num_bidders):
                bidder_name = input("Bidder name: ")
                bidder_balance = int(input("Bidder balance: "))
                bidder_probability = float(input("Likelihood to rebid: "))
                bidder_increase_perc = float(input("Desired percent increment: "))
                manual_bidders.append(Bidder(bidder_name, bidder_balance, bidder_probability, bidder_increase_perc))
                num_created += 1
            my_auction = Auction(manual_bidders)
            my_auction.simulate_auction(item_name, start_price)


if __name__ == '__main__':
    main()

