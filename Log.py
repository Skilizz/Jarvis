class Log(object):
    """Class for logging"""

    from datetime import datetime

    now = datetime.now()

    day = str(now.day)
    month = str(now.month)
    year = str(now.year)
    hour = str(now.hour)
    minute = str(now.minute)

    if len(day) == 1:
        day = "0" + day

    if len(month) == 1:
        month = "0" + month

    if len(hour) == 1:
        hour = "0" + hour

    if len(minute) == 1:
        minute = "0" + minute

    def __init__(self, message_user = "None", message_bot = "None"):
        self.message_user = message_user
        self.message_bot = message_bot

        Logging = f"Date: {self.day}.{self.month}.{self.year} \nTime: {self.hour}:{self.minute} \nMessage User: {message_user} \nMessage Bot: {message_bot}\n{'-' * 20}\n"
        
        with open("Log.txt", "a") as log_file:
            log_file.write(Logging)
            log_file.close()