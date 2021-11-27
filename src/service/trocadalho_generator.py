import requests


class TrocadalhoGeneratorService:
    def __init__(self, api_path: str):
        self.__api_path = api_path

    def get_answer(self, question: str):
        response = requests.get(self.__api_path, params={'question': question})
        if response.status_code == 200:
            return response.json()['answer']
        else:
            return None
