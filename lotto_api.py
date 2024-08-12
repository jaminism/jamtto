import requests
import pandas as pd
import os

def fetch_lotto_results(draw_no):
    """
    특정 회차의 로또 결과를 가져오는 함수.
    
    :param draw_no: 회차 번호
    :return: 당첨 번호 리스트와 보너스 번호
    """
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["returnValue"] == "success":
            numbers = [data[f"drwtNo{i}"] for i in range(1, 7)]
            return numbers
        else:
            return None
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

def update_lotto_data(file_path):
    """
    로컬 파일을 업데이트하여 새로운 로또 데이터를 추가하는 함수.
    
    :param file_path: 데이터 파일 경로
    """
    # 파일이 존재하지 않으면 새로운 파일 생성
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=['draw_no', 'numbers'])
        df.to_csv(file_path, index=False)
    
    # 기존 데이터 불러오기
    df = pd.read_csv(file_path)
    
    # 마지막 회차 확인
    last_draw_no = df['draw_no'].max() if not df.empty else 0
    
    # 새로운 회차 데이터를 가져와서 추가
    current_draw_no = last_draw_no + 1
    while True:
        result = fetch_lotto_results(current_draw_no)
        if result:
            df = df.append({'draw_no': current_draw_no, 'numbers': result}, ignore_index=True)
            current_draw_no += 1
        else:
            break
    
    # 데이터 파일 업데이트
    df.to_csv(file_path, index=False)