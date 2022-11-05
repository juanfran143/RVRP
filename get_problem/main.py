
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def streats(origin, destiny, by = "walking", get = "minutes"):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options) #, chrome_options=options
    driver.get("https://www.google.com/maps/dir///@40.4030301,-3.6927541,15z/data=!4m2!4m1!3e3")

    cookies = driver.find_elements(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button')[0]
    cookies.click()

    origen = []
    while len(origen) == 0:
        origen = driver.find_elements(By.XPATH, '//*[@id="sb_ifc50"]/input')
    origen = origen[0]
    origen.send_keys(origin)

    destino = driver.find_elements(By.XPATH, '//*[@id="sb_ifc51"]/input')[0]
    destino.send_keys(destiny)
    destino.send_keys(Keys.ENTER)


    if by == "car":
        car = driver.find_elements(By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button')[0]
        car.click()

        minutes = []
        while len(minutes) == 0:
            minutes = \
                driver.find_elements(By.XPATH,
                                     '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]')

        minutes = minutes[0]
        minutes = minutes.text
        k = 0
        while minutes[k] != " ":
            k += 1

        minutes = int(minutes[:k])

        km = driver.find_elements(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[2]/div')[0]
        km = km.text
        k = 0
        while km[k] != " ":
            k += 1

        km = float(km[:k].replace(",", "."))

    elif by == "walking":
        walking = driver.find_elements(By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[4]/button')[0]
        walking.click()
        #//*[@id="section-directions-trip-0"]/div[1]/div[3]/div[1]/div[1]

        minutes = []
        while len(minutes) == 0:
            minutes = \
                driver.find_elements(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[3]/div[1]/div[1]')

        minutes = minutes[0]
        minutes = minutes.text
        k = 0
        while minutes[k] != " ":
            k += 1

        minutes = int(minutes[:k])

        km = driver.find_elements(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[3]/div[1]/div[2]')[0]
        km = km.text
        k = 0
        while km[k] != " ":
            k += 1

        km = float(km[:k].replace(",", "."))

    if get == "minutes":
        return minutes
    else:
        return km


def plot_sol(best_route, by = "walking"):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #, chrome_options=options
    driver.get("https://www.google.com/maps/dir///@40.4030301,-3.6927541,15z/data=!4m2!4m1!3e3")

    cookies = driver.find_elements(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button')[0]
    cookies.click()

    if by == "car":
        car = driver.find_elements(By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button')[0]
        car.click()

    elif by == "walking":
        walking = driver.find_elements(By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[4]/button')[0]
        walking.click()

    for route in best_route:
        origen = []
        while len(origen) == 0:
            origen = driver.find_elements(By.XPATH, '//*[@id="sb_ifc50"]/input')
        origen = origen[0]
        origen.send_keys(route.route[0].x.street)

        destino = driver.find_elements(By.XPATH, '//*[@id="sb_ifc51"]/input')[0]
        destino.send_keys(route.route[0].y.street)
        destino.send_keys(Keys.ENTER)

        #//*[@id="omnibox-directions"]/div/div[3]/button
        added = 2
        for e in route.route[1:]:
            time.sleep(2)
            add = driver.find_elements(By.XPATH, '//*[@id="omnibox-directions"]/div/div[3]/button')[0]
            add.click()

            #//*[@id="sb_ifc52"]
            destino = driver.find_elements(By.XPATH, '//*[@id="sb_ifc5'+str(added)+'"]/input')[0]
            destino.send_keys(e.y.street)
            destino.send_keys(Keys.ENTER)
            added += 1

    get_url = driver.current_url
    time.sleep(30)



def plot_sol2(best_route, by = "walking"):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #, chrome_options=options
    driver.get("https://www.google.com/maps/dir///@40.4030301,-3.6927541,15z/data=!4m2!4m1!3e3")

    cookies = driver.find_elements(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button')[0]
    cookies.click()

    if by == "car":
        car = driver.find_elements(By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button')[0]
        car.click()

    elif by == "walking":
        walking = driver.find_elements(By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[4]/button')[0]
        walking.click()

    for route in best_route:
        origen = []
        while len(origen) == 0:
            origen = driver.find_elements(By.XPATH, '//*[@id="sb_ifc50"]/input')
        origen = origen[0]
        origen.send_keys(route.route[0].x.street)

        destino = driver.find_elements(By.XPATH, '//*[@id="sb_ifc51"]/input')[0]
        destino.send_keys(route.route[0].y.street)
        destino.send_keys(Keys.ENTER)

        #//*[@id="omnibox-directions"]/div/div[3]/button
        added = 2
        for e in route.route[1:]:
            time.sleep(2)
            add = driver.find_elements(By.XPATH, '//*[@id="omnibox-directions"]/div/div[3]/button')[0]
            add.click()

            #//*[@id="sb_ifc52"]
            destino = driver.find_elements(By.XPATH, '//*[@id="sb_ifc5'+str(added)+'"]/input')[0]
            destino.send_keys(e.y.street)
            destino.send_keys(Keys.ENTER)
            added += 1

    time.sleep(30)







