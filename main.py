from lotto_api import update_lotto_data
from lotto_analyzer import analyze_lotto_numbers, generate_lotto_recommendations

if __name__ == "__main__":
    # 데이터 파일 경로
    data_file = 'lotto_data.csv'
    
    # 데이터 파일 업데이트
    update_lotto_data(data_file)
    
    # 로또 번호 분석 및 추천
    all_numbers = analyze_lotto_numbers(data_file)
    
    print("가장 많이 당첨된 숫자:")
    for number, count in all_numbers:
        print(f"숫자 {number}: {count}번 당첨됨")
    
    # 추천 로또 번호 생성
    recommendations = generate_lotto_recommendations(all_numbers, num_recommendations=5)
    print("\n추천 로또 번호:")
    for i, recommendation in enumerate(recommendations, start=1):
        print(f"추천 {i}: {recommendation}")