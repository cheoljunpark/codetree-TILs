from decimal import Decimal, getcontext

# 입력값을 받습니다.
a, b = map(int, input().split())

# 소수점 22자리까지 정확도를 설정합니다.
# 21번째 자리에서 내림하기 위해 22자리까지 계산한 후 21자리에서 자릅니다.
getcontext().prec = 22

# 실수 a/b를 계산합니다.
result = Decimal(a) / Decimal(b)

# 소수점 21번째 자리에서 내림하여 결과를 문자열로 변환합니다.
# 문자열로 변환한 후, 소수점 21번째 자리까지 슬라이스합니다.
result_str = str(result)[:23]  # 소수점 포함 총 23자리 (0.xxxxxxxxxxxxxxxxxxxx)

print(result_str)