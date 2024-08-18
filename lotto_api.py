import os
import pandas as pd
import requests

def load_lotto_data(filepath='lotto_data.csv'):
    """
    CSV 파일에서 로또 데이터를 로드.
    
    :param filepath: 로또 데이터 파일 경로
    :return: 로또 데이터를 담고 있는 pandas DataFrame
    """
    return pd.read_csv(filepath)

def parse_winning_numbers(numbers_str):
    """
    문자열 형식의 로또 번호를 리스트로 변환.
    
    :param numbers_str: 로또 번호가 문자열로 저장된 데이터 (예: "[10, 23, 29, 33, 37, 40]")
    :return: 로또 번호 리스트 (예: [10, 23, 29, 33, 37, 40])
    """
    return literal_eval(numbers_str)

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

def update_lotto_data(file_path='lotto_data.csv'):
    """
    로컬 파일을 업데이트하여 새로운 로또 데이터를 추가하는 함수.
    
    :param file_path: 데이터 파일 경로
    """
    # 파일이 존재하지 않으면 새로운 파일 생성
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=['draw_no', 'numbers'])
        df.to_csv(file_path, index=False)
    
    # 기존 데이터 불러오기
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        # 파일이 비어 있는 경우, 빈 데이터프레임 생성
        df = pd.DataFrame(columns=['draw_no', 'numbers'])
    
    # 마지막 회차 확인
    last_draw_no = df['draw_no'].max() if not df.empty else 0
    
    # 새로운 회차 데이터를 가져와서 추가
    current_draw_no = last_draw_no + 1
    new_rows = []
    while True:
        result = fetch_lotto_results(current_draw_no)
        if result:
            new_rows.append({'draw_no': current_draw_no, 'numbers': result})
            current_draw_no += 1
        else:
            break
    
    # 새로운 데이터를 데이터프레임으로 변환하고 기존 데이터와 결합
    if new_rows:
        new_df = pd.DataFrame(new_rows)
        df = pd.concat([df, new_df], ignore_index=True)
    
    # 데이터 파일 업데이트
    df.to_csv(file_path, index=False)