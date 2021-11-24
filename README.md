# PRUEBA INSTALACIÓN PROGRAMA/PAQUETE DEL PROYECTO WEB SCRAPPING
Esta es una pequeña prueba de como instalar el paquete del proyecto web scrapping y acceder a todas sus funcionalidades sin tener que clonar el proyecto original

### Detalle a tener en cuenta
Una vez instalado el entorno virtual venv e instalado el programa de web scrapping

```bash
pip install wheel

pip install Menus_Scrapping_Tool-0.0.1-py3-none-any.whl

pip freeze > requirements.txt

```

Ir a main.py y colocar la URL_ATLAS, DB y Collection de tu Cluster para insertar los JSON

```python 
    # #* MONGODB SECTION
    #* connection(<atlas_url>)
    #* Ejm: url-atlas: 
    '''
    "mongodb+srv://<user>:<password>@sandbox.dec55.mongodb.net/?retryWrites=true&w=majority"
    '''
    client = connection("<url_atlas>")              

    try:
        db_project = client['<db>']
        menus_collection = db_project['<collection>']
    
        #* insert menus on database
        menus_collection.insert_many(result_scrapping)

    ...

```




