from lotto_api import fetch_all_lotto_results
from lotto_analyzer import analyze_lotto_numbers, generate_lotto_recommendations

if __name__ == "__main__":
    # 최대 회차 번호를 최신 회차 번호로 설정 (예: 1075)
    max_draw_no = 1075
    
    # 모든 로또 결과 가져오기
    all_numbers = fetch_all_lotto_results(max_draw_no)
    
    # 가장 많이 당첨된 숫자 분석
    most_common_numbers = analyze_lotto_numbers(all_numbers)
    
    print("가장 많이 당첨된 숫자:")
    for number, count in most_common_numbers:
        print(f"숫자 {number}: {count}번 당첨됨")
    
    # 추천 로또 번호 생성
    recommendations = generate_lotto_recommendations(most_common_numbers, num_recommendations=5)
    print("\n추천 로또 번호:")
    for i, recommendation in enumerate(recommendations, start=1):
        print(f"추천 {i}: {recommendation}")