"""
Simulation of a multi-player tournament of Rock, Paper, Scissors.
Uses basic Monte Carlo simulation techniques to derive statistical
analysis of this simple game scenario.

IS590PR
J. Weible


Adaptive strategies to consider implementing for players:

0. DONE. The original adaptive AI strategy already working: simply find the most-frequent selection by the opponent
against the AI player choose its killer.  Outcome: No advantage against uniform choosers nor against other AI players
with same technique, but devastating against the highly non-uniform choosers.

1. A player with same knowledge as current AI, but who uses balanced random choices instead of just looking at
their most-common choice. Hypothesis: Should reduce # of ties, but might not improve the winning advantage.

2. A player who knows if the opponent is using the current AI (strategy 0 above) and second-guesses them.
Hypothesis: Should be able to beat the current AI almost 100% of the time (except the cases where their stats
have two or three equally-high frequencies.

3. A player who can only remember the last X choices per opponent.  Hypothesis: Should be better than no AI but
not quite as successful against non-AI players adaptive technique 0.

4. Like #0, but the player somehow knows their opponent's _complete_ choice history against ALL opponents.
Hypothesis: No significant advantage over #0 against non-AI players.  Might actually do WORSE against certain types of
other AI though.

5. Simulate real people who cheat. A fast player who watches carefully and has X% chance of seeing the shape opponent
is forming, to change their own a few milliseconds later.  Hypothesis: Would be an advantage over any other strategy if
the success rate were high enough.  But perhaps the tournament judges can use camera replay and have Y% chance of
disqualifying them.  This style does not seem mathematically interesting to simulate...

"""


from random import choice, randint
from collections import Counter, defaultdict
import typing


def weapon_to_beat(weapon: str) -> str:
    """Which weapon will beat the given one?

    :param weapon: 'rock', 'paper', or 'scissors'
    :return: the correct weapon to beat the parameter weapon.

    >>> weapon_to_beat('rock')
    'paper'
    >>> weapon_to_beat('paper')
    'scissors'
    >>> weapon_to_beat('scissors')
    'rock'
    """
    better_weapon={'rock': 'paper',
                   'scissors': 'rock',
                   'paper': 'scissors'}

    if weapon not in better_weapon.keys():
        raise ValueError('unknown weapon.')
    return better_weapon[weapon]


class Player:
    """A competitor in a Rock, Paper, Scissors game.
    Most players have a fixed 'tendency' or 'preference' for choosing
    rock vs. paper vs. scissors, so this is defined proportionally
    for each player and influences the distribution of their
    pseudo-random choice in each match.

    However, a player can be configured to use adaptive playing techniques
    where they try to 'learn' the preferences of each opponent and will
    try to beat them instead of randomly choose."""

    player_count = 0  # Initialize count of all players.
    all_players = []  # automatically track all players
    win_verb = {'paper': 'covers', 'rock': 'smashes', 'scissors': 'cut'}

    def __init__(self, name=None, tendency=None, adaptive_ai=False):
        Player.player_count += 1
        Player.all_players.append(self)

        # assign player's name:
        if name is None:
            self.name = 'Player {:02}'.format(Player.player_count)
        else:
            self.name = name

        self.tendency = None
        self.randmax = None
        self.set_tendency(tendency)

        # track player stats:
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.opponents = Counter()
        self.choices = Counter()

        self.adaptive_ai = adaptive_ai
        if adaptive_ai:
            # This player will keep track of how many times each opponent
            # chooses each 'weapon', to make a theoretically better choice
            # against them next time:
            self.opponent_choices = defaultdict(Counter)

    def set_tendency(self, t: tuple):
        """player's preference or relative tendency to choose rock vs paper vs scissors.

        :param t: must be a tuple of 3 nums. tendency ratio of rocks:papers:scissors. """
        if t is None:
            self.tendency = (1, 1, 1)
        else:
            self.tendency = t

        # pre-calculate and store these values for randomization of turns:
        r, p, s = self.tendency
        self.randmax = r + p + s

    def __str__(self):
        """Define string representation of player object."""
        return self.name

    def __repr__(self):
        """Define object representation of player object."""
        return "Player('{}', {})".format(self.name, self.tendency.__repr__())

    def next_choice(self, opponent: 'Player') -> str:
        """In a single 'turn', what did this player randomly choose. This uses
        the 'tendency' tuple of the player to allow simulating players who don't
        choose with a uniform distribution.

        :param opponent: the opposing player. This is used only by the Adaptive_AI players.
        :return: 'rock', 'paper', or 'scissors'
        """

        if self.adaptive_ai:
            # this is an adaptive_ai player, so see if it has collected
            # enough stats about the current opponent yet:
            if sum(self.opponent_choices[opponent.name].values()) > 5:
                # has enough samples to start adapting to the opponent
                print(' {} is trying to guess the opponent\'s choice...'.format(self.name))

                # AI algorithm 1:
                # simply find the most-frequent selection by the opponent and
                # choose its killer.

                guess = self.opponent_choices[opponent.name].most_common(1)[0][0]
                ai_choice = weapon_to_beat(guess)
                print(' ', opponent.name, 'most often chose', guess, 'so he/she chose', ai_choice)
                return ai_choice

        # use the standard tendency distribution to choose a weapon:
        n = randint(1, self.randmax)
        if n <= self.tendency[0]:
            return 'rock'
        elif n <= self.tendency[0] + self.tendency[1]:
            return 'paper'
        else:
            return 'scissors'

    def play_against(self, p2, print_result=False):
        """Simulate a single 'match'. Continues until not a tie.

        :param p2: the opponent player
        :param print_result: enable or disable print output
        :return: the winning player
        """

        if self == p2:
            print('Invalid match. A player can not compete against themselves.')
            return None
        c1 = c2 = None

        while c1 == c2:
            # This loop takes care of ties.
            c1 = self.next_choice(opponent=p2)
            c2 = p2.next_choice(opponent=self)
            Player.record_play(self, c1, p2, c2, winner=None)

        if (c1 == 'rock' and c2 == 'paper') or \
            (c1 == 'paper' and c2 == 'scissors') or \
            (c1 == 'scissors' and c2 == 'rock'):
            winner = p2
            win_choice = c2
            loser = self
            loss_choice = c1
        else:
            winner = self
            win_choice = c1
            loser = p2
            loss_choice = c2

        # Update stats:
        Player.record_play(self, c1, p2, c2, winner)
        # winner.record_win(weapon=win_choice, opponent=loser)
        # loser.record_loss(weapon=loss_choice, opponent=winner)
        if print_result:
            print('{:20s}  {} {} {}'.format(winner.name + ' beat ' + loser.name + '.',
                                            win_choice,
                                            Player.win_verb[win_choice],
                                            loss_choice))
        return winner

    @staticmethod
    def record_play(p1: 'Player', weapon1: str, p2: 'Player', weapon2: str,
                    winner: typing.Union['Player', None]):
        if winner is None:
            # it was a tie
            p1.ties += 1
            p2.ties += 1
        else:
            if winner == p1:
                loser = p2
            else:
                loser = p1
            winner.wins += 1
            loser.losses += 1

        p1.choices[weapon1] += 1
        p2.choices[weapon2] += 1
        p1.opponents[p2] += 1
        p2.opponents[p1] += 1

        p1.record_ai_stats(p2, weapon2)
        p2.record_ai_stats(p1, weapon1)

    def record_ai_stats(self, opponent: 'Player', opponent_weapon: str):
        """Only for the adaptive_AI players, record what the opponent just chose

        :param opponent: a Player
        :param opponent_weapon: 'rock', 'paper', or 'scissors' just chosen by opponent.
        :return:
        """
        if self.adaptive_ai:
            self.opponent_choices[opponent.name][opponent_weapon] += 1

    def get_win_percentage(self) -> float:
        """Calculate the player's win/loss percentage."""
        if self.wins == 0:
            return 0.0
        else:
            return round((self.wins / (self.wins + self.losses)) * 100, 2)

    def tendency_as_percents(self) -> tuple:
        (r, p, s) = self.tendency
        total = r + p + s
        scale = 100.0 / total
        return r * scale, p * scale, s * scale

    def choices_as_percents(self) -> tuple:
        (r, p, s) = self.choices['rock'], self.choices['paper'], self.choices['scissors']
        total = r + p + s
        scale = 100.0 / total
        return r * scale, p * scale, s * scale

    def print_details(self):
        print('Name:', self.name)
        print(' Preference for rock/paper/scissors {:5.1f}% {:5.1f}% {:5.1f}%'.format(*self.tendency_as_percents()))
        print(' Actually chose rock/paper/scissors {:5.1f}% {:5.1f}% {:5.1f}%'.format(*self.choices_as_percents()))
        total_opponents = sum(self.opponents.values())
        print(' Opposed:')
        for p in sorted(self.opponents.keys(), key=lambda x: x.name):
            print('  {:8s} {} times ({:4.1f}% of matches)'.format(
                    p.name, self.opponents[p], (self.opponents[p] / total_opponents * 100)
            ))
        print()
        if self.adaptive_ai:
            print(' Adaptive AI data stored:', dict(self.opponent_choices))
            print()


if __name__ == '__main__':
    # Define several players:
    Player('Ted')                # uniform chooser
    Player('Jane')               # uniform chooser
    Player('Ed')                 # uniform chooser

    # Player('Joe', (100, 50, 0))  # loves rock, hates scissors
    # Player('Bob', (2, 2, 3))     # prefers scissors
    # Player('Kim', (2, 10, 7))    # favors paper, but also likes scissors

    # Player('Marvin', adaptive_ai=True)
    # Player('Hal', adaptive_ai=True)

    # Simulate many random matches:
    for match in range(100):
        player_1 = choice(Player.all_players)
        player_2 = choice(Player.all_players)
        if player_1 != player_2:  # Can't play against themselves!
            player_1.play_against(player_2, print_result=True)

    # Print Tournament stats:
    print('\n-----------------------------------------------------------------')
    print('\nTournament Player Statistics:\n')
    print('Name             Win%  Won Lost Tied')
    print('-------------- ------ ---- ---- ----')
    for p in sorted(Player.all_players, key=lambda x: x.get_win_percentage(), reverse=True):
        print('{:14} {:6.2f} {:4d} {:4d} {:4d}'.format(p.name, p.get_win_percentage(), p.wins, p.losses, p.ties))

    print('\n-----------------------------------------------------------------')
    print('\nPlayers\' Detailed Stats:\n')
    for p in Player.all_players:
        p.print_details()
