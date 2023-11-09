#import getting_cars_url
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mariadb
from datetime import date, timedelta
from datetime import datetime
connection = mariadb.connect(
    user = "root",
    password = "123",
    host = "127.0.0.1",
    port = 3306,
    database = "mysql"

)
# Get Cursor
mycursor = connection.cursor()

chrome_options = Options()
chrome_options.add_argument('--headless')

chrome_options.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/Profile99")

# create a new Chrome browser instance with headless mode
browser = webdriver.Chrome(options=chrome_options)


# Open the file for reading
with open("cars_url.txt", "r", encoding='utf-8') as f:
    # Read the lines of the file and store them in a list
    car_urls = f.readlines()

# Strip newline characters from each line
car_urls = [line.strip() for line in car_urls]

with open("tel_dataset.txt", "r", encoding='utf-8') as f:
    # Read the lines of the file and store them in a list
    tel_nums = f.readlines()

# Strip newline characters from each line
tel_nums = [line.strip() for line in tel_nums]

with open("whatsapp_dataset.txt", "r", encoding='utf-8') as f:
    # Read the lines of the file and store them in a list
    whatsapp_nums = f.readlines()

# Strip newline characters from each line
whatsapp_nums = [line.strip() for line in whatsapp_nums]

for url_no in range(149, len(car_urls)):
    browser.get(car_urls[url_no])

    items = {}
    items_len = len(browser.execute_script("return document.getElementsByClassName('andes-table__row ui-vpp-striped-specs__row')"))
    for i in range(items_len):
        key = browser.execute_script(f"return document.getElementsByClassName('andes-table__row ui-vpp-striped-specs__row')[{i}].children[0].innerText")
        value = browser.execute_script(f"return document.getElementsByClassName('andes-table__row ui-vpp-striped-specs__row')[{i}].children[1].innerText")
        items[key] = value

    color = items.get("Color", "null")
    combustible = items.get("Tipo de combustible", "null")  #fuel
    motor = items.get("Motor", "null")     #engine
    puertas = items.get("Puertas", "null") #doors
    estaciona = items.get("Sensor de estacionamiento", "null") #park
    transmision = items.get("Transmisión", "null")
    encat = items.get("Encat", 0)
    id_ads = url_no + 2
    id_catg = items.get("Id_catg", 0)
    marca = items.get("Marca", "null")  #mark
    modelo = items.get("Modelo", "null") #model
    try:
        # Your existing code here
        titulo = browser.execute_script("return document.getElementsByClassName('ui-pdp-header__title-container')[0].innerText") #title
    except:
        titulo = "null" #title
    
    try:
        # Your existing code here
        descri = browser.execute_script("return document.getElementsByClassName('ui-pdp-description__content')[0].innerText") #description
    except:
        descri = "null" #description
    
    images = ""
    try:
        # Your existing code here
        images_len = len(browser.execute_script("return document.getElementsByClassName('ui-pdp-image ui-pdp-gallery__figure__image')"))

        for i in range(images_len):
            image = browser.execute_script(f"return document.getElementsByClassName('ui-pdp-image ui-pdp-gallery__figure__image')[{i}].getAttribute('src')")
            images = images + image + ","
        imagen = browser.execute_script("return document.getElementsByClassName('ui-pdp-image ui-pdp-gallery__figure__image')[0].getAttribute('src')") 
        iextra = images  #image
    except:
        iextra = 'null'  #image
    

    moneda = items.get("Moneda", "null") #currency
    try:
        # Your existing code here
        precio = int(browser.execute_script("return document.getElementsByClassName('andes-money-amount__fraction')[0].textContent").replace(",", ""))  #price
    except:
        precio = "null"  #price
    
    #precio = 0 #price
    usuario = items.get("Usuario", "null")  #user
    email = items.get("Email", "null")
    website = items.get("Website", "null")
    video = items.get("Video", "null")

    telefono = tel_nums[url_no]#####################
    whatsapp = whatsapp_nums[url_no]###################

    prof_part = items.get("Prof_part", "null")
    periodo = items.get("Periodo", "null") #period
    ano = items.get("Año", "null") #year
    
    km = items.get("Kilómetros", "null")


    interiores = items.get("Interiores", "null") #interiors
 

    
    asientos = items.get("Asientos", "null") #seats
    cilindros = items.get("Cilindros", "null") #cylinders
    consumo = items.get("Consumo", "null") # consumption
    co2 = items.get("Co2", "null")
    recamaras = items.get("Recamaras", "null") #bedrooms
    m2c = items.get("M2c", "null")
    m2t = items.get("M2t", "null")
    banos = items.get("Banos", "null") #bathrooms
    estaciona = items.get("Estaciona", "null") #park
    plantas = items.get("Plantas", "null") #plants
    x = items.get("X", "null")
    y = items.get("Y", "null")

    direccion = ""
    try:
        # Your existing code here
        address_len = len(browser.execute_script("return document.getElementsByClassName('ui-seller-info__status-info')"))
        for i in range(address_len):
            address_title = browser.execute_script(f"return document.getElementsByClassName('ui-seller-info__status-info')[{i}].textContent")
            if "Vehicle location" in address_title:
                address_title = address_title.replace("Vehicle location", "")
                direccion = address_title   #address
    except:
        direccion = "null"   #address

    cp = items.get("Cp", "null")
    estado = items.get("Estado", "null") #status
    ciudad = items.get("Ciudad", "null") #city
    colonia = items.get("Colonia", "null") #colony

    try:
        # Your existing code here
        subtitle = browser.execute_script('return document.getElementsByClassName("ui-pdp-subtitle")[0].textContent').split(" ")
        current_date = date.today()
        new_date = current_date - timedelta(days=int(subtitle[7]))
        publicado =  new_date.strftime("%Y-%m-%d") #published
        edad = datetime.now().year - int(subtitle[0]) #age
    except:
        publicado =  "0000-00-00" #published
        edad = "null" #age
   

    active = items.get("Active", 1) 
    destacado = items.get("Destacado", 0)  #featured
    notificado = items.get("Notificado",0)  #reported
    id_bot = items.get("Id_bot", 0) 
    id_url = items.get("Id_url", 0) 
    indexeado = items.get("Indexeado", 0) 
    from_post_user = items.get("From post user",0) 
    #print('loaing successful!################################################')

    query = f"INSERT INTO `p_ads_tmp` (`encat`, `id_ads`, `id_catg`, `marca`, `modelo`, `titulo`, `descri`,`imagen`,`iextra`,`moneda`, `precio`, `usuario`, `email`, `website`, `video`, `telefono`, `whatsapp`, `prof_part`, `periodo`, `ano`, `transmision`, `km`, `color`, `interiores`, `motor`, `combustible`, `puertas`, `asientos`, `cilindros`, `consumo`, `co2`, `recamaras`, `m2c`, `m2t`, `banos`, `estaciona`, `plantas`, `edad`, `x`, `y`, `direccion`, `cp`, `estado`, `ciudad`, `colonia`, `publicado`, `active`, `destacado`, `notificado`, `id_bot`, `id_url`, `indexeado`, `from_post_user`) VALUES({encat},{id_ads},{id_catg},'{marca}', '{modelo}', '{titulo}', '{descri}', '{imagen}', '{iextra}', '{moneda}', {precio}, {usuario}, '{email}', '{website}', '{video}', '{telefono}', '{whatsapp}', {prof_part}, '{periodo}', {ano}, '{transmision}', '{km}', '{color}', '{interiores}', '{motor}', '{combustible}', {puertas}, {asientos}, {cilindros}, {consumo}, {co2}, {recamaras}, {m2c}, {m2t}, '{banos}', '{estaciona}', '{plantas}', '{edad}', '{x}', '{y}', '{direccion}', '{cp}', {estado}, {ciudad}, {colonia}, '{publicado}', {active}, {destacado}, {notificado}, {id_bot}, {id_url}, {indexeado}, {from_post_user})"
    mycursor.execute(query)
    connection.commit()
    print(f'{url_no}-step')

# Close the cursor and database connection
connection.close()
browser.quit()