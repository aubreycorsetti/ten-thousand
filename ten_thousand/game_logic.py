from random import randint
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        """

        :param num_dice:
        :return: tuple with random values between 1 and 6
        """
        return tuple(randint(1, 1) for _ in range(0, num_dice))

    @staticmethod
    def calculate_score(roll):
        """
              param: a tuple of integers that represent a dice roll.
              :return: an integer representing the roll’s score according to rules of game.
              """

        total = 0
        counted_dice = Counter(roll).most_common()
        print(counted_dice)

        if not counted_dice:
            return total

        if (counted_dice[0][1]) >= 3:
            if counted_dice[0][0] != 1:
                total += counted_dice[0][0] * 100 * (counted_dice[0][1] - 2)
                if counted_dice[0][1] == 6:
                    return total
                counted_dice = counted_dice[1:]
                print(counted_dice)
            else:
                total += 1000 * (counted_dice[0][1] - 2)
                if counted_dice[0][1] == 6:
                    return total
                counted_dice = counted_dice[1:]

            if len(counted_dice) == 1:
                if counted_dice[0][1] == 3:
                    if counted_dice[0][0] != 1:
                        total += counted_dice[0][0] * 100
                        return total
                    else:
                        total += 1000
                        return total

        if len(counted_dice) == 6:
            total += 1500
            return total

        if len(counted_dice) == 3:
            if counted_dice[2][1] == 2:
                total += 1500
                return total

        else:
            for dice in counted_dice:
                if dice[0] == 5:
                    total += dice[1] * 50
            for dice in counted_dice:
                if dice[0] == 1:
                    total += dice[1] * 100

        print("Total Score", total)
        return total



