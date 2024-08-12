import random

def generate_lotto_numbers():
    # 1부터 45 사이의 숫자 중 6개를 무작위로 선택합니다.
    numbers = random.sample(range(1, 46), 6)
    # 선택한 숫자를 오름차순으로 정렬합니다.
    numbers.sort()
    return numbers

if __name__ == "__main__":
    lotto_numbers = generate_lotto_numbers()
    print("추천 로또 번호: ", lotto_numbers)