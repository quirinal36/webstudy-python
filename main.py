from db import Data

data = Data()
data.addData('코로나 예방접종', '이상반응 발생시 꼭 신고 해주세요.')

for board in data.getData():
    print(board)

data.addData('월드컵 최종예선 진출', '대한민국 국가대표 축구팀 화이팅')
data.addData('알고리즘을 배우자', '코딩만 알고 알고리즘을 모르면 안된다.')

print('___________________________')

for board in data.getData():
    print(board)