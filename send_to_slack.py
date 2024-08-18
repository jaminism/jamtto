import requests
import json

def send_lotto_numbers_to_slack(webhook_url, recommendations, context):
    """
    Slack Incoming Webhook을 사용하여 추천 로또 번호를 전송하는 함수.
    
    :param webhook_url: Slack Webhook URL
    :param recommendations: 추천 로또 번호의 리스트
    """
    message = {
        "text": context,
        "attachments": [
            {
                "text": "\n".join([f"추천 {i+1}: {', '.join(map(str, recommendation))}" for i, recommendation in enumerate(recommendations)])
            }
        ]
    }

    response = requests.post(
        webhook_url, 
        data=json.dumps(message), 
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code == 200:
        print("메시지가 성공적으로 전송되었습니다.")
    else:
        print(f"메시지 전송 실패: {response.status_code}, {response.text}")