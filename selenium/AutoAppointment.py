from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from datas import obter_quintas
from datas import obter_sextas

mes = 4
ano = 2025
quintas = obter_quintas(mes, ano)
print(f"Quintas e Sextas de {mes}/{ano}: {quintas}")

sextas = obter_sextas(mes, ano)
print(f"Quintas e Sextas de {mes}/{ano}: {sextas}")

# Configuração do WebDriver
driver = webdriver.Chrome()  # Substitua pelo caminho do chromedriver.exe, se necessário


driver.get("https://ais.usvisa-info.com/pt-br/niv/users/sign_in")



# Login
email = driver.find_element(By.ID, "user_email")  # Ajuste o ID de acordo com o site
senha = driver.find_element(By.ID, "user_password")
checkbox = driver.find_element(By.ID, "policy_confirmed")
email.send_keys("fernandaalvesrute@despachatur.com.br")
senha.send_keys("")
checkbox_wrapper = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.icheckbox.icheck-item"))
)
checkbox_wrapper.click()


# Clique no botão "Entrar"
driver.find_element(By.NAME, "commit").click()

cliente = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//tr/td[1]'))
)
clientes = driver.find_elements(By.XPATH, '//tr/td[1]')

nomes = [cliente.text.strip() for cliente in clientes]

for nome in nomes:
    print(nome)

map = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(((By.LINK_TEXT, "visualizar mapa")))
)
map.click()

representante = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//h5[contains(text(), "Endereço")]/following-sibling::p[1]'))
)

representante_name = representante.text.upper()
print(representante_name)

return_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.small"))
)
return_button.click()


continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.primary.small"))
)
continue_button.click()


try:
    dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Agendar Entrevista para Retirar Documentos"))
    )

    dropdown.click()

    button_appoint = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/appointment/document_pickup')]"))
    )

    button_appoint.click()

except TimeoutException:
#     # dropdown = WebDriverWait(driver, 10).until(
#     # EC.element_to_be_clickable((By.LINK_TEXT, "Realizar Agendamento"))
#     # )

#     # dropdown.click()

#     # button_appoint = WebDriverWait(driver, 10).until(
#     # EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Realizar Agendamento')]"))
#     # )

#     # button_appoint.click()
    print('provável Recall')

try:
    ok = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
    )
    ok.click()

except:
    print("Botão 'OK' não encontrado, seguindo em frente...")


appointment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "appointments_asc_appointment_date"))
)

appointment.click()


appointment_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "appointments_asc_appointment_date"))
)

print("O botão tá ali, vou tentar clicar...")

appointment_button.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "td[data-handler='selectDay'] a.ui-state-default"))
)
# time.sleep(5)  # Espera manualmente 5 segundos para ver se o calendário aparece
# driver.save_screenshot("screenshot.png")  # Salva uma imagem da tela
# print("Screenshot tirado! Veja se o calendário aparece na imagem.")

data_agendada = None

while not data_agendada:
    for dia in sextas:
        try:
            seletor_dia = f'td[data-handler="selectDay"] a.ui-state-default'
            datas_disponiveis = driver.find_elements(By.CSS_SELECTOR, seletor_dia)

            for elemento in datas_disponiveis:
                if elemento.text.strip() == str(dia):
                    elemento.click()
                    data_agendada = dia
                    break
            if data_agendada:
                break
        except Exception:
            continue


dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "appointments_asc_appointment_time"))
)

select = Select(dropdown)

WebDriverWait(driver, 5).until(lambda d: len(select.options) > 1)

options = select.options

if len(options) > 1:
    select.select_by_index(len(options) -1)
else:
    print('sem horarios')


print(f"Agendamento feito para o dia {data_agendada}/{mes}/{ano}")


# # Fechar o navegador
input("Pressione Enter para fechar o navegador manualmente...")

