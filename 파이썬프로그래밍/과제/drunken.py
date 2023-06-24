import datetime
import calendar

def save_to_file(date, message):
    with open('log.txt', 'a') as f:
        f.write(date + ': ' + message + '\n')

while True:
    answer = input('아버지가 술을 드셨나요? (예/아니오) ')
    if answer == '예':
        today = datetime.date.today()
        print(calendar.month(today.year, today.month))
        save_to_file(str(today), '술을 드셨습니다.')
        break
    elif answer == '아니오':
        today = datetime.date.today()
        print(calendar.month(today.year, today.month))
        save_to_file(str(today), '술을 들이지 않았습니다.')
        break
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.')
