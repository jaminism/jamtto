# jamtto

Lotto 번호를 추출하는 프로그램


## 실행 방법
`python main.py`


## test 시뮬레이션:
이전 당첨 회차의 번호들을 추천 번호와 비교하고, 실제로 각 회차의 결과와 비교하여 결과가 어떻게 되는지 확인.

추천 번호는 각 회차마다 100번의 추천 번호를 생성하며, 1등 또는 3등의 결과만 출력한다. 


#### 실행 방법
`python main.py --test`


## Config 파일
main.py 파일에서 config 경로를 수정하거나,
해당 파일을 만들어서 webhook url 정보를 기입해야 함

`config_file = 'config/slack_info.json'`

{

    "webhook_url": "https://hooks.slack.com/services/000000000/000000000000/000000000000000000000000"   
}

## 로또 당첨 결과 기록
lotto_data.csv 파일에 이전 당첨 번호를 기록하며, 최신 데이터가 없다면 업데이트를 함
