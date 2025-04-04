from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import json
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from datas import obter_quintas
from datas import obter_sextas
import re



def salvar_agendamento(agendamento):
    data_str = agendamento["data_hora"].split(",")[0]  
    data_formatada = datetime.strptime(data_str, "%d %B %Y").strftime("%d-%m-%Y")  

    representante = agendamento["representante"].replace(" ", "_")  


    caminho_base = r"C:\\Users\\despachatur\\Documents\\PRONTO PARA RECOLHER"
    caminho_pasta = os.path.join(caminho_base, data_formatada, representante)

    os.makedirs(caminho_pasta, exist_ok=True)  


    nome_arquivo = f"{agendamento['cliente'].replace(' ', '_')}.json"  
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)


    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(agendamento, f, ensure_ascii=False, indent=4)
        print(f"✅ Agendamento salvo em: {caminho_arquivo}")
    except Exception as e:
        print(f"❌ Erro ao salvar o arquivo: {e}")








contas = []
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
email.send_keys("magdasoaresrute@despachatur.com.br")
senha.send_keys("DESPACHATUR12")
checkbox_wrapper = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div.icheckbox.icheck-item"))
)
checkbox_wrapper.click()

clientes = []
datas = []
locais = []
representantes = []

# Clique no botão "Entrar"
driver.find_element(By.NAME, "commit").click()

cliente = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//tr/td[1]'))
)
clientes = driver.find_elements(By.XPATH, '//tr/td[1]')

clientes_da_conta = [cliente.text.strip() for cliente in clientes],




# for nome in nomes:
#     print(nome)

map = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(((By.LINK_TEXT, "visualizar mapa")))
)
map.click()

representante = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//h5[contains(text(), "Endereço")]/following-sibling::p[1]'))
)

representante_da_conta = representante.text.upper()


local_do_agendamento = driver.find_element(By.XPATH, '//h5[contains(text(), "Nome da seção")]/following-sibling::p[1]')





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
    dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Realizar Agendamento"))
    )

    dropdown.click()

    button_appoint = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Realizar Agendamento')]"))
    )

    button_appoint.click()
    print('provável Recall')
    obs = 'provável recall'

try:
    ok = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK')]"))
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


agendar = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "appointments_submit"))
)

agendar.click()

ok = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "ui-button.ui-corner-all.ui-widget"))
)

ok.click()

imprimir = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='Imprimir']]"))
)
imprimir.click()

data_formatada = f"{data_agendada} {datetime(ano, mes, 1).strftime('%B')} {ano}"

agendamento = {
    "cliente": cliente,  # você pode adaptar isso se tiver uma lista
    "representante": representante_da_conta,
    "data_hora": data_formatada,
    "local": local_do_agendamento
}

salvar_agendamento(agendamento)

inicio = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Início"))
)
inicio.click()

data_local = WebDriverWait(driver, 10).until(
    EC._element_if_visible(By.CLASS_NAME, "consular-appt")
)
texto_completo = elemento.text

padrao_data = r"\d{1,2} \w+, \d{4}, \d{2}:\d{2}"
data_match = re.search(padrao_data, texto_completo)
padrao_local = r"(\w+ de \w+ - \w+)"
local_match = re.search(padrao_local, texto_completo)

data_do_agendamento = f"{data_agendada} {datetime(ano, mes, 1).strftime('%B')} {ano}"

local_do_agendamento = local_match.group() if local_match else "Local não encontrado"

print("Data:", data_do_agendamento)
print("Local:", local_do_agendamento)

def salvar_dados_em_json(dados, nome_arquivo="agendamentos.json"):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"Dados salvos em {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

agendamentos = {}

for conta in contas:  
    clientes = []  
    
    for cliente in clientes_da_conta: 
        clientes.append(cliente)  
    
    representante = representante_da_conta if representante_da_conta else "Nenhum"
    data_hora = data_do_agendamento
    local = local_do_agendamento
    

    agendamentos[conta] = {
        "clientes": clientes,
        "representante": representante,
        "data_hora": data_hora,
        "local": local,
        "Obs": obs
    }

salvar_dados_em_json(agendamentos)
salvar_agendamento




print(f"Agendamento feito para o dia {data_agendada}/{mes}/{ano}")



input("Pressione Enter para fechar o navegador manualmente...")

