from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_open_change_modal(browser, login):
    change_wallpaper_menu = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'change-wallpaper'))
    )
    change_wallpaper_menu.click()

    change_wallpaper_item = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'change-wallpaper-menu__exact-change'))
    )
    change_wallpaper_item.click()

    change_modal = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'change-wallpaper-menu__exact-change'))
    )

    assert change_modal.is_displayed(), "Модальное окно для изменения обоев не отображается"

    close_button = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'close-upload-modal__btn'))
    )
    close_button.click()

    try:
        WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'change-wallpaper-menu__exact-change'))
        )
        flag = False
    except TimeoutException:
        flag = True

    assert flag is True, "Модальное окно для изменения обоев отображается после закрытия"

