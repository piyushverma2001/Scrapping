from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run headless Chrome (without a GUI)
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome driver
# service = Service()  # Specify the path to the chromedriver if not in PATH
# driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.get('https://olympics.com/en/paris-2024/medals')
# driver.get('https://olympics.com/en/paris-2024/medals/india')

# def medal_elements(url):
#   driver = webdriver.Chrome()
#   driver.get(url)
#   wait = WebDriverWait(driver, 30)
#   elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.e1oix8v91.emotion-srm-9g0i61')))
#   country_selector = 'span.elhe7kv5.emotion-srm-uu3d5n'
#   medals_selector = 'span.e1oix8v91.emotion-srm-81g9w1'
#   total_medals_selector = 'span.e1oix8v91.emotion-srm-5nhv3o'
  
#   return olympics(driver, country_selector, medals_selector, total_medals_selector)


def olympics(url):
  # Set up Chrome options
  chrome_options = Options()
  # chrome_options.add_argument("--headless")  # Run headless Chrome (without a GUI)
  chrome_options.add_argument("--disable-gpu")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--window-size=1920,1080")  # Set the window size (optional)
  chrome_options.add_argument("--start-maximized")  # Ensure the window is maximized (optional)


  # Set up the Chrome driver
  service = Service()  # Specify the path to the chromedriver if not in PATH
  driver = webdriver.Chrome(service=service, options=chrome_options)

  driver = webdriver.Chrome()
  driver.get(url)
  wait = WebDriverWait(driver, 30)
  elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.e1oix8v91.emotion-srm-9g0i61')))
  country_selector = 'span.elhe7kv5.emotion-srm-uu3d5n'
  medals_selector = 'span.e1oix8v91.emotion-srm-81g9w1'
  total_medals_selector = 'span.e1oix8v91.emotion-srm-5nhv3o'
  
  rank_list = driver.find_elements(By.CSS_SELECTOR, country_selector)
  country_names = [element.text for element in rank_list]
  
  country_list = driver.find_elements(By.CSS_SELECTOR, country_selector)
  country_names = [element.text for element in country_list]
  
  medals_list = driver.find_elements(By.CSS_SELECTOR, medals_selector)
  medals_value = [element.text for element in medals_list]

  total_medals_list = driver.find_elements(By.CSS_SELECTOR, total_medals_selector)
  total_medals = [element.text for element in total_medals_list]

  driver.quit()
  return country_names, medals_value, total_medals


def medals():
  
  data_list = []
  
  # for all countries
  # country_names, medals_value, total_medals = olympics(driver, country_selector, medals_selector, total_medals_selector)
  country_names, medals_value, total_medals = olympics('https://olympics.com/en/paris-2024/medals')
  country_count = len(country_names)
  n = 3
  medals_chunk = [medals_value[i * n:(i + 1) * n] for i in range((len(medals_value) + n - 1) // n )]  
  
  india_in_first_list = False
  
  for i in range(5):
    if country_names[i].lower() == 'india':
      india_in_first_list = True
    data = {
        'Country': country_names[i],
        'Medals': {
            'Gold': medals_chunk[i][0],
            'Silver': medals_chunk[i][1],
            'Bronze': medals_chunk[i][2]
        },
        'Total Medals': total_medals[i]
    }
    data_list.append(data)
    
  print("All Countries \n")
  print(medals_chunk)
  print("\n")
  if india_in_first_list == False:
    del data_list[4]

    # for india
    country_names, medals_value, total_medals = olympics('https://olympics.com/en/paris-2024/medals/india')
    country_count = len(country_names)
    n = 3
    medals_chunk = [medals_value[i * n:(i + 1) * n] for i in range((len(medals_value) + n - 1) // n )]
    print("India Country \n")
    print(medals_chunk)
    print("\n")
    
    for i in range(1):
      data = {
          'Country': country_names[i],
          'Medals': {
              'Gold': medals_chunk[i][0],
              'Silver': medals_chunk[i][1],
              'Bronze': medals_chunk[i][2]
          },
          'Total Medals': total_medals[i]
      }
      data_list.append(data)
      
  # else:
    # 
    # data_list[4].Country
  
  return data_list


# print(medals())


