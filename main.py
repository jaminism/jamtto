import json
from lotto_api import update_lotto_data
from lotto_analyzer import analyze_lotto_numbers, generate_lotto_recommendations
from send_to_slack import send_lotto_numbers_to_slack

def load_config(config_file):
    """
    설정 파일을 로드하여 JSON 객체로 반환하는 함수.

    :param config_file: 설정 파일 경로
    :return: 설정 정보를 포함하는 딕셔너리
    """
    with open(config_file, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    # 설정 파일 경로
    config_file = 'config/slack_info.json'
    
    # 설정 파일 로드
    config = load_config(config_file)
    
    # 데이터 파일 경로
    data_file = 'lotto_data.csv'
    
    # 데이터 파일 업데이트
    update_lotto_data(data_file)
    
    # 로또 번호 분석 및 추천
    all_numbers = analyze_lotto_numbers(data_file)
    
    # print("가장 많이 당첨된 숫자:")
    # for number, count in all_numbers:
        # print(f"숫자 {number}: {count}번 당첨됨")
    
    # 추천 로또 번호 생성
    recommendations = generate_lotto_recommendations(all_numbers, num_recommendations=5)
    
    # Slack으로 추천 로또 번호 전송
    send_lotto_numbers_to_slack(config['slack_webhook_url'], recommendations)