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

def generate_lotto_recommendations(most_common_numbers, num_recommendations=5):
    """
    상위 15개의 숫자를 기반으로 추천 번호를 생성하는 함수.
    
    :param most_common_numbers: 가장 많이 등장한 상위 15개 숫자 리스트
    :param num_recommendations: 생성할 추천 번호의 수
    :return: 추천 로또 번호의 리스트
    """
    top_numbers = [number for number, count in most_common_numbers]
    
    # 모든 가능한 6개 조합 생성
    all_combinations = list(combinations(top_numbers, 6))
    
    # 무작위로 num_recommendations개의 고유 조합을 선택
    recommendations = random.sample(all_combinations, num_recommendations)
    
    # 각 조합을 정렬하여 반환
    return [sorted(recommendation) for recommendation in recommendations]