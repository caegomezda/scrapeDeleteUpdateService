import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm
import time
from urllib.parse import urljoin, urlparse

# Configuración inicial
url = input("Ingresa la URL del sitio web: ")
errors = []  # Lista para almacenar los errores
scraping_data = {"main_page": {}, "linked_pages": {}}  # Estructura para todo el scraping

# Configuración del navegador
def setup_driver():
    return webdriver.Chrome()  # Asegúrate de que ChromeDriver esté instalado y en el PATH

# Función para generar nombres de archivos basados en URLs
def generate_filename_from_url(base_url):
    parsed_url = urlparse(base_url)
    domain = parsed_url.netloc.replace(".", "_")
    return f"{domain}_scraping.json"

# Función para verificar si la página es válida
def is_valid_page(driver):
    try:
        body_text = driver.find_element(By.TAG_NAME, "body").text
        if "Page not found" in body_text or "404" in body_text:
            return False
        return True
    except Exception:
        return False

# Función para extraer elementos de una página
def extract_elements(driver):
    elements_data = []
    try:
        all_elements = driver.find_elements(By.XPATH, "//*")
        for element in all_elements:
            tag_name = element.tag_name
            text = element.text.strip()
            if text:
                elements_data.append({"tag": tag_name, "text": text})
    except Exception as e:
        errors.append(f"Error al extraer elementos: {str(e)}")
    return elements_data

# Función para manejar la navegación segura
def navigate_to_url(driver, target_url):
    try:
        driver.get(target_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        if not is_valid_page(driver):
            errors.append(f"Página no válida o 404: {target_url}")
            return False
        return True
    except Exception as e:
        errors.append(f"Error al navegar a {target_url}: {str(e)}")
        return False

# Función principal para procesar una página
def process_page(driver, page_url, is_main=False):
    if not navigate_to_url(driver, page_url):
        return None

    elements = extract_elements(driver)
    router_links = []

    for element in driver.find_elements(By.XPATH, "//*[@routerlink]"):
        try:
            tag_name = element.tag_name
            text = element.text.strip()
            router_link = element.get_attribute("routerlink")
            href = element.get_attribute("href")
            if router_link:
                router_links.append({"tag": tag_name, "text": text, "routerlink": router_link, "href": href})
        except Exception as e:
            errors.append(f"Error al procesar router link: {str(e)}")

    return {"url": page_url, "elements": elements, "router_links": router_links}

# Inicializar el driver
driver = setup_driver()

try:
    print("Procesando página principal...")
    main_page_data = process_page(driver, url, is_main=True)
    if main_page_data:
        scraping_data["main_page"] = main_page_data

    visited_links = set()
    print("Procesando páginas vinculadas...")

    for link in tqdm(scraping_data["main_page"].get("router_links", []), desc="Procesando router links"):
        router_url = urljoin(url, link.get("routerlink"))
        if router_url not in visited_links:
            visited_links.add(router_url)
            linked_page_data = process_page(driver, router_url)
            if linked_page_data:
                scraping_data["linked_pages"][link.get("routerlink")] = linked_page_data

finally:
    print("Cerrando el navegador...")
    driver.quit()

    # Guardar todos los datos de scraping en un archivo JSON único
    output_file = generate_filename_from_url(url)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(scraping_data, f, ensure_ascii=False, indent=4)
    print(f"Datos completos del scraping guardados en {output_file}")

    # Mostrar y guardar los errores de forma bonita
    if errors:
        print("Errores encontrados durante el scraping:")
        for error in errors:
            print(f"- {error}")
    else:
        print("No se encontraron errores durante el scraping.")
