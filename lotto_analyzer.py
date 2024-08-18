import random
import pandas as pd
from collections import Counter
from lotto_api import load_lotto_data, parse_winning_numbers

def analyze_lotto_numbers(filepath='lotto_data.csv'):
    """
    파일에서 데이터를 불러와 숫자의 등장 빈도를 분석하는 함수.
    
    :param filepath: 데이터 파일 경로
    :return: 가장 많이 등장한 상위 번호의 리스트
    """
    df = pd.read_csv(filepath)
    all_numbers = []
    
    for numbers in df['numbers']:
        all_numbers.extend(eval(numbers))  # 문자열을 리스트로 변환
    
    number_counts = Counter(all_numbers)
    most_common_numbers = [num for num, count in number_counts.most_common(15)]
    return most_common_numbers

def generate_varied_recommendations(most_common_numbers):
    """
    분석된 상위 당첨 번호를 기반으로 다양한 추천 번호 조합을 생성합니다.

    :param most_common_numbers: 분석된 상위 당첨 번호 리스트
    :return: 다양한 조합의 추천 로또 번호 리스트들
    """
    recommendations = []
    num_combinations = [(6, 0), (5, 1), (4, 2), (3, 3), (2, 4)]
    for combo in num_combinations:
        num_from_common, num_random = combo
        recommendations.append(generate_recommendations(most_common_numbers, num_from_common, num_random))
    return recommendations

def generate_recommendations(common_numbers, num_from_common, num_random):
    """
    주어진 상위 당첨 번호 중 일부와 랜덤 번호를 혼합하여 추천 번호를 생성합니다.

    :param common_numbers: 분석된 상위 당첨 번호 리스트
    :param num_from_common: 상위 번호 중 선택할 번호의 수
    :param num_random: 랜덤으로 생성할 번호의 수
    :return: 생성된 추천 로또 번호 리스트
    """
    selected_numbers = random.sample(common_numbers, num_from_common)
    additional_numbers = []
    while len(additional_numbers) < num_random:
        new_number = random.randint(1, 45)
        if new_number not in selected_numbers and new_number not in additional_numbers:
            additional_numbers.append(new_number)
    
    return sorted(selected_numbers + additional_numbers)

def check_winning(recommended, winning_numbers):
    """
    추천된 로또 번호가 당첨 번호와 얼마나 일치하는지 확인하는 함수.
    
    :param recommended: 추천된 로또 번호 리스트
    :param winning_numbers: 실제 당첨 번호 리스트
    :return: 일치하는 숫자의 개수
    """
    return len(set(recommended) & set(winning_numbers))

def determine_rank(matches):
    """
    일치하는 숫자의 개수에 따라 로또 등수를 결정하는 함수.
    
    :param matches: 일치하는 숫자의 개수
    :return: 로또 등수 (1등, 3등, 4등, 5등, 낙첨)
    """
    if matches == 6:
        return '1등'
    elif matches == 5:
        return '3등'
    elif matches == 4:
        return '4등'
    elif matches == 3:
        return '5등'
    return '낙첨'


def run_simulation(filepath='lotto_data.csv', num_simulations=100):
    """
    시뮬레이션을 실행하여 추천받은 번호들을 이전 당첨 번호와 비교하는 함수.
    
    :param filepath: 로또 데이터 파일 경로
    :param num_simulations: 시뮬레이션 횟수
    """
    lotto_data = load_lotto_data(filepath)
    most_common_numbers = analyze_lotto_numbers(filepath)

    for sim_num in range(1, num_simulations + 1):
        recommendations = generate_varied_recommendations(most_common_numbers)
        
        for i, recommended in enumerate(recommendations, start=1):
            max_matches = 0
            best_matching_draw_no = None
            best_matching_numbers = None

            for _, row in lotto_data.iterrows():
                previous_draw_no = row['draw_no']
                previous_winning_numbers = parse_winning_numbers(row['numbers'])
                matches = check_winning(recommended, previous_winning_numbers)
                
                if matches > max_matches:
                    max_matches = matches
                    best_matching_draw_no = previous_draw_no
                    best_matching_numbers = previous_winning_numbers

            rank = determine_rank(max_matches)
            if rank in ['1등', '3등']:
                print(f"시뮬레이션 {sim_num} | 추천 {i}: {recommended} | 최대 일치: {max_matches}개 | 결과: {rank}")
                print(f"당첨 회차: {best_matching_draw_no} | 당첨 번호: {best_matching_numbers} | 추천 번호: {recommended}")
