# from pyvirtualdisplay import Display
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup


def main(br_name):
    browser = webdriver.Firefox()
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

    # ожидание пока не появится title="Учеба..."
    WebDriverWait(browser, 1).until(
        ec.presence_of_element_located((webdriver.common.by.By.ID, "heading1")))
    # time.sleep(7)

    # открытие страницы с кнопкой
    WebDriverWait(browser, 20).until(
        ec.presence_of_element_located((By.ID, 'heading1'))
    ).click()  # title="Учеба..."
    WebDriverWait(browser, 20).until(
        ec.presence_of_element_located((By.ID, 'menu_li_6118'))
    ).click()  # title="Расписание"
    print('В Расписании')

    btn_time = time.localtime().tm_hour, \
               time.localtime().tm_min, \
               time.localtime().tm_sec

    try:
        start_btn = WebDriverWait(browser, 20).until(
            ec.presence_of_element_located((By.LINK_TEXT, 'Начать занятие'))
        )
        start_btn.click()
        print(f'Зашёл на лекцию в {btn_time[0]}:{btn_time[1]}:{btn_time[2]}')
        browser.quit()
        time.sleep(5000)
    except NoSuchElementException:
        print(f'Проверка в {btn_time[0]}:{btn_time[1]}:{btn_time[2]}, лекции нет')
        browser.quit()
        time.sleep(500)

    main(br_name)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('ss')
