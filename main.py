import argparse
import json
from datetime import datetime
from lotto_api import load_lotto_data, update_lotto_data
from lotto_analyzer import analyze_lotto_numbers, generate_varied_recommendations, run_simulation
from send_to_slack import send_lotto_numbers_to_slack

def load_slack_info(filepath='config/slack_info.json'):
    """
    Slack Webhook URL을 JSON 파일에서 로드하는 함수.

    :param filepath: JSON 파일 경로
    :return: Slack Webhook URL을 포함한 딕셔너리
    """
    with open(filepath, 'r') as file:
        return json.load(file)

def get_current_week():
    """
    현재 날짜를 기준으로 올해 몇째 주인지 계산하는 함수.

    :return: 현재 날짜 기준 몇째 주인지
    """
    current_date = datetime.now()
    week_number = current_date.isocalendar()[1]  # isocalendar()[1]은 몇째 주인지 반환
    return week_number

def get_next_draw_number(filepath='lotto_data.csv'):
    """
    다음 회차 번호를 계산하는 함수. 마지막 회차 번호에 1을 더함.

    :param filepath: 로또 데이터 파일 경로
    :return: 다음 회차 번호
    """
    df = load_lotto_data(filepath)
    last_draw_no = df['draw_no'].max()
    return last_draw_no + 1

def main():
    """
    메인 실행 함수. 이번 주에 추천할 5가지 로또 번호를 생성하거나, 시뮬레이션을 실행.
    """
    parser = argparse.ArgumentParser(description="로또 번호 생성기 및 시뮬레이션 도구")
    parser.add_argument('--test', action='store_true', help="시뮬레이션을 실행하려면 이 옵션을 사용하세요")
    args = parser.parse_args()

    # 최신 로또 데이터 업데이트
    update_lotto_data()

    if args.test:
        # 시뮬레이션 모드
        run_simulation()
    else:
        # 이전 당첨 데이터 분석하여 상위 번호 추출
        most_common_numbers = analyze_lotto_numbers()
        
        # 다양한 추천 로또 번호 생성
        recommendations = generate_varied_recommendations(most_common_numbers)
        
        # 현재 몇째 주인지 계산
        current_week = get_current_week()
        
        # 다음 회차 번호 계산
        next_draw_number = get_next_draw_number()
        
        context=f"이번 주({current_week}주차, {next_draw_number}회차) 추천 로또 번호:"
        print(context)
        for i, recommended in enumerate(recommendations, start=1):
            print(f"추천 {i}: {recommended}")
        
        # Slack Webhook URL 로드 및 전송
        slack_info = load_slack_info()
        send_lotto_numbers_to_slack(slack_info['webhook_url'], recommendations, context)

if __name__ == "__main__":
    main()
=======
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