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
    browser = None
    if br_name == 'opera':
        browser_path = '/home/exi_ku/PycharmProjects/lk_autostart_lecture/operadriver'
        # открытие браузера
        webdriver_service = webdriver.chrome.service.Service(browser_path)
        webdriver_service.start()
        browser = webdriver.Remote(webdriver_service.service_url,
                                   webdriver.DesiredCapabilities.OPERA)
    elif br_name == 'chrome':
        chromedriver = '/usr/bin/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # для открытия headless-браузера
        browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    else:
        driver = webdriver.Firefox()
    print('Открываем браузер')

    # открытие сайта и вход
    browser.get('https://lk.sut.ru/cabinet/')
    email = browser.find_element_by_name('users')
    parole = browser.find_element_by_name('parole')
    login_btn = browser.find_element_by_name('logButton')
    email.send_keys('vladislavvolkovn1@yandex.ru')
    parole.send_keys('8523526549')
    login_btn.click()
    print('Заходим на сайт')

    # ожидание пока не появится title="Учеба..."
    WebDriverWait(browser, 1).until(
        ec.presence_of_element_located((webdriver.common.by.By.ID, "heading1")))
    # time.sleep(7)

    # открытие страницы с кнопкой
    browser.find_element_by_id('heading1').click()  # title="Учеба..."
    time.sleep(0.1)
    browser.find_element_by_id('menu_li_6118').click()  # title="Расписание"
    time.sleep(1)
    print('В Расписании')

    btn_time = time.localtime().tm_hour, \
               time.localtime().tm_min, \
               time.localtime().tm_sec

    try:
        start_btn = browser.find_element_by_link_text('Начать занятие')
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
