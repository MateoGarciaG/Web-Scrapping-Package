# PRUEBA INSTALACIÓN PROGRAMA/PAQUETE DEL PROYECTO WEB SCRAPPING
Esta es una pequeña prueba de como instalar el paquete del proyecto web scrapping y acceder a todas sus funcionalidades sin tener que clonar el proyecto original

### Detalle a tener en cuenta
Una vez instalado el entorno virtual venv e instalado el programa de web scrapping

```bash
pip install wheel

pip install Menus_Scrapping_Tool-0.0.1-py3-none-any.whl

pip freeze > requirements.txt

```

Hay que ir a la carpeta del entorno virtual y eliminar de la ruta del modulo "crawler" el "src" en el import`
En la siguiente ruta:

```python 

# <nombreEntornoVirtual>/Lib/site-packages/crawler/crawling.py

# Antes

import requests
from src.content_page.content_html import get_html_content
...

# Después

import requests
from content_page.content_html import get_html_content

...

```




