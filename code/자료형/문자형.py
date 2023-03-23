"""문자열 자료형"""
# 큰따옴표("")
_str1 = "온 세상이 너를 닮은 꽃빛으로 반짝일 때"

# 작은따옴표('')
_str2 = '넌 머지않아 예쁜 꽃이 될 테니까'

# 큰따옴표 3개(연속)
_str3 = """Python is fun"""

# 숫자형 -> 문자형
int2str = int("5555")


"""이스케이프 코드"""
line = "\n" # 줄 변경
tab = "\t" # 탭 간격
slash = "\\" # \ 출력


"""문자열 연산하기"""
# 문자열 더하기(연결)
head = "life "
tail = "is Python"
print(head + tail) # list is Python


# 문자열 곱하기
text = "python"
print(text * 2) # pythonpython

# 문자열 길이 구하기
text = "무한으로 즐겨요!"
print(len(text)) # 9
