from collections import Counter
import random
import pandas as pd
from itertools import combinations

def analyze_lotto_numbers(file_path):
    """
    파일에서 데이터를 불러와 숫자의 등장 빈도를 분석하는 함수.
    
    :param file_path: 데이터 파일 경로
    :return: 가장 많이 등장한 상위 15개 숫자의 리스트
    """
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return []  # 파일이 비어 있으면 빈 리스트 반환

    all_numbers = []
    
    for numbers in df['numbers']:
        all_numbers.extend(eval(numbers))  # 문자열을 리스트로 변환
    
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
    if not most_common_numbers:
        print("No data available for recommendations.")
        return []

    top_numbers = [number for number, count in most_common_numbers]
    
    # 모든 가능한 6개 조합 생성
    all_combinations = list(combinations(top_numbers, 6))
    
    # 무작위로 num_recommendations개의 고유 조합을 선택
    recommendations = random.sample(all_combinations, num_recommendations)
    
    # 각 조합을 정렬하여 반환
    return [sorted(recommendation) for recommendation in recommendations]