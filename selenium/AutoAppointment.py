from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

# Configuração do WebDriver
driver = webdriver.Chrome()  # Substitua pelo caminho do chromedriver.exe, se necessário

# Acesse o sistema da PBH
driver.get("https://ais.usvisa-info.com/pt-br/niv/users/sign_in")



# Login
email = driver.find_element(By.ID, "user_email")  # Ajuste o ID de acordo com o site
senha = driver.find_element(By.ID, "user_password")
checkbox = driver.find_element(By.ID, "policy_confirmed")
email.send_keys("")
senha.send_keys("")
checkbox_wrapper = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.icheckbox.icheck-item"))
)
checkbox_wrapper.click()


# Clique no botão "Entrar"
driver.find_element(By.NAME, "commit").click()


continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.primary.small"))
)
continue_button.click()

dropdown = WebDriverWait(driver, 10).until(
   EC.element_to_be_clickable((By.LINK_TEXT, "Reagendar entrevista"))
)


dropdown.click()


appointment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.primary.small-only-expanded[href='/pt-br/niv/schedule/63853842/appointment']"))
)

appointment.click()




# # Fechar o navegador
input("Pressione Enter para fechar o navegador manualmente...")
