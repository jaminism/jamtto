import requests

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
            bonus_number = data["bnusNo"]
            return numbers, bonus_number
        else:
            return None
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

def fetch_all_lotto_results(max_draw_no):
    """
    최대 회차까지 모든 로또 결과를 가져오는 함수.
    
    :param max_draw_no: 최대 회차 번호
    :return: 모든 당첨 번호의 리스트
    """
    all_numbers = []
    
    for draw_no in range(1, max_draw_no + 1):
        result = fetch_lotto_results(draw_no)
        if result:
            numbers, _ = result
            all_numbers.extend(numbers)
        else:
            break  # 더 이상 결과가 없으면 종료
    
    return all_numbers