from datetime import datetime, timedelta,timezone

def changeTimezone(_time,hours:int=4):
    return datetime.strptime(_time,'%H:%M').astimezone(timezone(timedelta(hours=hours))).strftime("%H:%M")
print(changeTimezone("14:34"))
print(changeTimezone("22:34"))