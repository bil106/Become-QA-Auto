from modules.ui.page_objects.post_office_page import PostOfficePage
import pytest


@pytest.mark.ui
def test_check_incorrect_num():
    # создаем обьект страницы
    check_pac = PostOfficePage()

    #открываем страницу почты
    check_pac.go_to()

    #пробуем ввести номер посылки
    check_pac.try_numb_pack('12345678')

    #Проверяем 
    assert AssertionError


    #закрываем браузер
    check_pac.close()
