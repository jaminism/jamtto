import requests
from collections import Counter
import random

def fetch_lotto_results(draw_no):
    # 특정 회차의 로또 결과를 가져오는 함수
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["returnValue"] == "success":
            numbers = [data[f"drwtNo{i}"] for i in range(1, 7)]
            bonus_number = data["bnusNo"]
            return numbers, bonus_number
        else:
            return None
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

def fetch_all_lotto_results(max_draw_no):
    all_numbers = []
    
    for draw_no in range(1, max_draw_no + 1):
        result = fetch_lotto_results(draw_no)
        if result:
            numbers, _ = result
            all_numbers.extend(numbers)
        else:
            break  # 더 이상 결과가 없으면 종료
    
    return all_numbers

def analyze_lotto_numbers(all_numbers):
    # 숫자 빈도 계산
    number_counts = Counter(all_numbers)
    
    # 빈도수에 따라 상위 10개 숫자 추출
    most_common_numbers = number_counts.most_common(10)
    
    return most_common_numbers

def generate_lotto_recommendations(most_common_numbers):
    # 상위 10개의 번호를 사용하여 무작위로 6개를 선택
    top_numbers = [number for number, count in most_common_numbers]
    recommended_numbers = random.sample(top_numbers, 6)
    recommended_numbers.sort()  # 오름차순 정렬
    return recommended_numbers

if __name__ == "__main__":
    # 최대 회차 번호를 설정해야 합니다 (예: 1075)
    max_draw_no = 1075  # 최신 회차 번호로 설정
    
    # 모든 로또 결과 가져오기
    all_numbers = fetch_all_lotto_results(max_draw_no)
    
    # 가장 많이 당첨된 숫자 분석
    most_common_numbers = analyze_lotto_numbers(all_numbers)
    
    print("가장 많이 당첨된 숫자:")
    for number, count in most_common_numbers:
        print(f"숫자 {number}: {count}번 당첨됨")
    
    # 추천 로또 번호 생성
    recommendation = generate_lotto_recommendations(most_common_numbers)
    print("\n추천 로또 번호:")
    print(recommendation)