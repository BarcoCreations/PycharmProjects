from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class Message(Turtle):


    def __init__(self):
        super().__init__()
        self.message = "Ahoj"
        self.level = 0
        self.color("white")
        self.penup()
        self.goto(0, -290)
        self.hideturtle()
        self.update_message()

    def update_message(self):
        self.write(f"Message = {self.message}", align=ALIGNMENT, font=FONT)

    def increase_message(self):
        self.level += 1
        self.clear()
        if self.level == 1:
            self.message = "Ahoj, Team Zeus"
        elif self.level == 2:
            self.message = "Ahoj, Team Zeus rád"
        elif self.level == 3:
            self.message = "Ahoj, Team Zeus rád by som"
        elif self.level == 4:
            self.message = "Ahoj, Team Zeus rád by som pracoval"
        elif self.level == 5:
            self.message = "Ahoj, Team Zeus rád by som pracoval pre Vas"
        elif self.level == 6:
            self.message = "Ahoj, Team Zeus rád by som pracoval pre Vas \n a učil sa Python,"
        elif self.level == 7:
            self.message = "Ahoj, Team Zeus rád by som pracoval pre Vas \n a učil sa Python, Django a"
        else:
            self.message = "Ahoj, Team Zeus rád by som pracoval pre Vas \n a učil sa Python, Django, a dalsie zaujimave veci :-)"
        self.write(f"Message = {self.message}", align=ALIGNMENT, font=FONT)