import datetime

def show_diff(data):
    
    print(data)
    print(datetime.datetime.now()) 
    specified_timestamp = data.timestamp()
    current_timestamp = datetime.datetime.now().timestamp()
    time_difference = (current_timestamp - specified_timestamp)
    print(f' Разница в секундах - {time_difference}')
    
    time_difference_timedelta = datetime.timedelta(seconds=time_difference)
    days = time_difference_timedelta.days
    hours, remainder = divmod(time_difference_timedelta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print("Разница во времени (дни:часы:минуты):", days, "дн.", hours, "ч.", minutes, "мин.")

#datas = [datetime.datetime.now() + datetime.timedelta(minutes = i*3) for i in range(7)]
datas2 = [(datetime.datetime.now() + datetime.timedelta(minutes = i*3), datetime.datetime.now() + datetime.timedelta(minutes = i*3 + 5)) for i in range(7)]
print(f'Текущее время - {datetime.datetime.now()}\t{int(datetime.datetime.now().timestamp())}') 
for data in datas2:
    print(f'{int(data[0].timestamp())}\t{int(data[1].timestamp())}')
    #print(show_diff(data))