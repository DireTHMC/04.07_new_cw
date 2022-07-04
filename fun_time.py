from datetime import datetime

def get_time_now():
    cur_time = datetime.now().time()
    cur_date = datetime.now().date()
    x = f'время: {cur_time} / дата: {cur_date}'
    return x
print(get_time_now())