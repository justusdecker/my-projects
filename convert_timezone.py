from datetime import datetime, timedelta,timezone

def changeTimezone(_time,hours:int=4):
    return datetime.strptime(_time,'%H:%M').astimezone(timezone(timedelta(hours=hours + (hours + int(_time[:2]) > 24)))).strftime("%H:%M")
print(changeTimezone("14:34"))
print(changeTimezone("22:34"))
