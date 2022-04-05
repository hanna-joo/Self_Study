# %%
"""
# Lottery Simulation Program
#### 로또는 주 1회씩 열립니다. 하지만 한 사람이 한 회차에 여러 번 참여할 수도 있습니다.  
#### 번호는 1부터 45까지 있는데요. 주최측에서는 매주 6개의 '일반 당첨 번호'와 1개의 '보너스 번호'를 뽑습니다. 그리고 참가자는 1번 참여할 때마다 서로 다른 번호 6개를 선택합니다.
#### 당첨 액수는 아래 규칙에 따라 결정됩니다.
1. 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
2. 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
3. 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
4. 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
5. 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)
"""

# %%
"""
## 1. 번호 생성 (Generate numbers)
- 파라미터로 정수 n을 받는다.
- 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑는다.
- 그 번호들이 담긴 리스트를 리턴한다.
"""

# %%
from random import randint

def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers

# %%
# 함수 테스트
print(generate_numbers(6))
print(generate_numbers(3))

# %%
"""
## 2. 당첨 번호 뽑기 (Draw winning numbers)
- 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 생성한다.
- 일반 당첨 번호 6개는 정렬되어 있고, 보너스 번호는 마지막에 추가한다.
- 그 번호들이 담긴 리스트를 리턴한다.
"""

# %%
def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

# %%
# 함수 테스트
print(draw_winning_numbers())

# %%
"""
## 3. 겹치는 번호 개수 세기 (Count matching numbers)
- 리스트 2개를 파라미터로 받는다. (각 리스트 길이 상관 없음)
- 두 리스트 사이에 겹치는 번호 개수를 센다.
- 번호 개수를 리턴한다.
"""

# %%
def count_matching_numbers(numbers, winning_numbers):
    # 지난 과제의 코드를 붙여 넣으세요.
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count

# %%
# 함수 테스트
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))

# %%
"""
## 4. 당첨금 조회하기 (Check winnings)
- 파라미터로 참가자가 뽑은 번호 리스트(numbers)와 주최측에서 뽑은 번호 리스트(winning_numbers)를 받는다.
- 당첨 액수 규칙은 아래와 같으며 참가자의 당첨 금액을 리턴한다.
    + 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
    + 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
    + 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
    + 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
    + 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)
"""

# %%
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

# %%
print(check([2, 4, 11, 14, 25, 40], [2, 4, 11, 14, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))