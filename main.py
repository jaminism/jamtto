import pandas as pd
from collections import Counter

def analyze_lotto_data(file_path):
    # CSV 파일 읽기
    df = pd.read_csv(file_path)
    
    # 모든 당첨 번호를 하나의 리스트로 합치기
    all_numbers = []
    for numbers in df['numbers']:
        all_numbers.extend(map(int, numbers.split(',')))
    
    # 숫자 빈도 계산
    number_counts = Counter(all_numbers)
    
    # 빈도수에 따라 정렬하여 상위 10개 숫자 추출
    most_common_numbers = number_counts.most_common(10)
    
    return most_common_numbers

if __name__ == "__main__":
    file_path = 'lotto_results.csv'  # 데이터 파일 경로
    top_numbers = analyze_lotto_data(file_path)
    print("가장 많이 당첨된 숫자 10개:")
    for number, count in top_numbers:
        print(f"숫자 {number}: {count}번 당첨됨")