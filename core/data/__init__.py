#데이터를 불러오고 처리를 하기위한 모듈


# data클레스를 상속받고 차례대로 처리됨
# 1. load
# 2. preprocessing -> 필요 기능 정의
# 3. return
# 4. 그리고 return 된 데이터는 임시영역에서 다음 loader 부분으로 전달된다.(?음...데이터 헤드 보기 필요할듯)