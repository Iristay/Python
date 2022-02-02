class Stats():
    # отслеживания статистика
    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
    def reset_stats(self):
        """статистика изменящаяся во время игры"""
        self.guns_left = 3

