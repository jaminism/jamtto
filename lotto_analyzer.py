from collections import Counter
import random
from itertools import combinations

def analyze_lotto_numbers(all_numbers):
    """
    숫자의 등장 빈도를 분석하여 상위 15개를 반환하는 함수.
    
    :param all_numbers: 모든 로또 번호 리스트
    :return: 가장 많이 등장한 상위 15개 숫자의 리스트
    """
    number_counts = Counter(all_numbers)
    most_common_numbers = number_counts.most_common(15)
    return most_common_numbers

def generate_lotto_recommendations(most_common_numbers):
    """
    상위 15개의 숫자를 기반으로 추천 번호를 생성하는 함수.
    
    :param most_common_numbers: 가장 많이 등장한 상위 15개 숫자 리스트
    :return: 추천 로또 번호 리스트
    """
    top_numbers = [number for number, count in most_common_numbers]
    
    # 가능한 모든 조합 중 하나를 무작위로 선택하여 추천 번호로 설정
    all_combinations = list(combinations(top_numbers, 6))
    recommended_combination = random.choice(all_combinations)
    
    return sorted(recommended_combination)