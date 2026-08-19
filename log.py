class Log:
    def __init__(self, date, todo, description=""):
        self.date = date
        self.todo = todo
        self.description = description

    def __str__(self):
        return f"Date: {self.date} | Todo: {self.todo} | Description: {self.description}"