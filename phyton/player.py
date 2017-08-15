from .data import PlayerType, Race, Difficulty

class Player(object):
    def __init__(self, type, race, difficulty=None):
        assert isinstance(type, PlayerType)
        assert isinstance(race, Race)
        if type == PlayerType.Computer:
            assert isinstance(difficulty, Difficulty)
        else:
            assert difficulty is None

        self.type = type
        self.race = race
        if type == PlayerType.Computer:
            self.difficulty = difficulty

class Human(Player):
    def __init__(self, race):
        super().__init__(PlayerType.Participant, race)

class Bot(Player):
    def __init__(self, race, bot):
        super().__init__(PlayerType.Participant, race)

        # assert isinstance(bot, BotAI)
        self.bot = bot

class Computer(Player):
    def __init__(self, race, difficulty=Difficulty.Easy):
        super().__init__(PlayerType.Computer, race, difficulty)