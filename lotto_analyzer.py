from collections import Counter
import random

def analyze_lotto_numbers(all_numbers):
    """
    숫자의 등장 빈도를 분석하여 상위 10개를 반환하는 함수.
    
    :param all_numbers: 모든 로또 번호 리스트
    :return: 가장 많이 등장한 상위 10개 숫자의 리스트
    """
    number_counts = Counter(all_numbers)
    most_common_numbers = number_counts.most_common(10)
    return most_common_numbers

def generate_lotto_recommendations(most_common_numbers):
    """
    상위 10개의 숫자를 기반으로 추천 번호를 생성하는 함수.
    
    :param most_common_numbers: 가장 많이 등장한 상위 10개 숫자 리스트
    :return: 추천 로또 번호 리스트
    """
    top_numbers = [number for number, count in most_common_numbers]
    recommended_numbers = random.sample(top_numbers, 6)
    recommended_numbers.sort()
    return recommended_numbers