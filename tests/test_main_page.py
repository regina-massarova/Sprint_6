import allure
import pytest
from pages.main_page import MainPage
from data import ANSWERS



class TestMainPage:

    @allure.description('Проверяем, что при клике на вопрос ответ верный')
    @pytest.mark.parametrize(
        'num, result',
        [(i, ANSWERS[i]) for i in range(8)]  
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result  

