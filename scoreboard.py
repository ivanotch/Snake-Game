from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt") as file:
            self.write(f'Score: {self.score} High Score: {file.read()}', False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f'{self.score}')
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
