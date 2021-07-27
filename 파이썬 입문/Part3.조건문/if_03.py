#아래 두 줄의 코드는 변수 hour에 현재 시간을 저장합니다.
from datetime import datetime 
hour = datetime.now().hour

if hour < 12 :
    print('오전입니다.')
