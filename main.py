import time
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def main(curr_path):
    browser_path = curr_path + 'operadriver'
    # открытие браузера
    webdriver_service = webdriver.chrome.service.Service(browser_path)
    webdriver_service.start()
    browser = webdriver.Remote(webdriver_service.service_url,
                               webdriver.DesiredCapabilities.OPERA)
    print('Открываем браузер')

    # открытие сайта и вход
    browser.get('https://lk.sut.ru/cabinet/')
    email = WebDriverWait(browser, 20).until(
        ec.presence_of_element_located((By.NAME, 'users'))
    )
    parole = WebDriverWait(browser, 20).until(
        ec.presence_of_element_located((By.NAME, 'parole'))
    )
    login_btn = WebDriverWait(browser, 20).until(
        ec.presence_of_element_located((By.NAME, 'logButton'))
    )
    email.send_keys('vladislavvolkovn1@yandex.ru')
    parole.send_keys('8523526549')
    login_btn.click()
    print('Заходим на сайт')

    # открытие страницы с кнопкой
    WebDriverWait(browser, 20).until(
        ec.presence_of_element_located((webdriver.common.by.By.ID, "heading1"))
    ).click()  # title="Учеба..."
    WebDriverWait(browser, 20).until(
        ec.presence_of_element_located((By.ID, 'menu_li_6118'))
    ).click()  # title="Расписание"

    print('В Расписании')

    btn_time = time.localtime().tm_hour, \
               time.localtime().tm_min, \
               time.localtime().tm_sec

    try:
        start_btn = browser.find_element_by_link_text('Начать занятие')
        start_btn.click()
        print(f'Зашёл на лекцию в {btn_time[0]}:{btn_time[1]}:{btn_time[2]}')
        browser.quit()
        # print(f"Программа выполнилась за {time.time()-t1}")
        time.sleep(5000)
    except NoSuchElementException:
        print(f'Проверка в {btn_time[0]}:{btn_time[1]}:{btn_time[2]}, лекции нет')
        browser.quit()
        # print(f"Программа выполнилась за {time.time()-t1}")
        time.sleep(500)

    main(curr_path)


if __name__ == '__main__':
    main(sys.argv[0][:len(sys.argv[0]) - 7])
