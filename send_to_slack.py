import requests
import json

def send_lotto_numbers_to_slack(webhook_url, recommendations):
    """
    Slack Incoming Webhook을 사용하여 추천 로또 번호를 전송하는 함수.
    
    :param webhook_url: Slack Webhook URL
    :param recommendations: 추천 로또 번호의 리스트
    """
    # Slack 메시지 형식 정의
    message = {
        "text": "이번 주의 추천 로또 번호는 다음과 같습니다:",
        "attachments": [
            {
                "text": "\n".join([f"추천 {i+1}: {', '.join(map(str, recommendation))}" for i, recommendation in enumerate(recommendations)])
            }
        ]
    }

    # POST 요청을 통해 Slack으로 메시지 전송
    response = requests.post(
        webhook_url, 
        data=json.dumps(message), 
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code == 200:
        print("메시지가 성공적으로 전송되었습니다.")
    else:
        print(f"메시지 전송 실패: {response.status_code}, {response.text}")