"""리스트 생성"""
_list = []
_list = [1, 2, 3, 4, 5]
_list = ["사과", "포도", "딸기"]


"""리스트 인덱싱"""
_list = ["사과", "포도", "딸기"]
print(_list[0]) # 사과
print(_list[1]) # 포도
print(_list[2]) # 딸기


"""리스트 슬라이싱"""
_list = [1, 2, 3, 4, 5]
print(_list[0:2]) # [1, 2]
print(_list[1:4]) # [2, 3, 4]


"""리스트 더하기"""
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # [1, 2, 3, 4, 5, 6]

"""리스트 반복하기"""
a = [1, 2, 3]
print(a * 2) # [1, 2, 3, 1, 2, 3]

"""리스트 길이 구하기"""
a = [1, 2, 3]
print(len(a)) # 3


"""리스트 값 수정"""
_list = ["사과", "포도", "딸기"]
_list[0] = "청사과"
print(_list) # ["청사과", "포도", "딸기"]


"""리스트 값 삭제"""
_list = ["사과", "포도", "딸기"]
del _list[0] 
print(_list) # ["청사과", "포도"]


"""리스트 요소 추가"""
_list = ["사과", "포도", "딸기"]
_list.append("수박")
print(_list) # ["사과", "포도", "딸기", "수박"]


"""리스트 인덱스 반환"""
_list = ["사과", "포도", "딸기"]
print(_list.index("포도")) # 1


"""리스트 요소 삽입"""
_list = ["사과", "포도", "딸기"]
print(_list.insert(0, "수박")) # ["수박", "사과", "포도", "딸기"]


"""리스트 요소 끄집어내기"""
_list = ["사과", "포도", "딸기"]
print(_list.pop("사과")) # 사과
print(_list) # ["포도", "딸기"]


"""리스트 요소 세기"""
_list = [1, 2, 1, 1, 3]
print(_list.count(1)) # 3
