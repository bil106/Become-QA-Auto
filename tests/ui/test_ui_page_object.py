from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # создаем обьект страницы
    sign_in_page = SignInPage()

    #открываем страницу гитхаб
    sign_in_page.go_to()

    #пробуем войти в систему гитхаб
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    #Проверяем что название страницы такое как ожидаем
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


    #закрываем браузер
    sign_in_page.close()

