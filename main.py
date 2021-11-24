
#* MODULES
#* DATABASE MODULE
from database.db_conection import connection
from bson.json_util import dumps

#* REQUEST - CONTENT_PAGE MODULE
from content_page.content_html import get_html_content

#* CONVERT TO JSON MODULE
from convert_json.convert_json import convert_json

#* CRAWEL MODULE
from crawler.crawling import crawl_web

#* WEB SCRAPPING MODULE
from scrapping.scrapping import get_scrapping_content

"""MAIN.PY: Main File where we program execute
"""

#*************************************************************

#* Function to execute_program
def execute_program():
    """execute_program: This function execute the application

    Returns:
        list: Return a list with the result of the application
    """
    
    #* CRAWLER SECTION
    
    #* CRAWLER_WEB
    links_menus_web = crawl_web('https://mateogarciag.github.io/Project-dual-website')
    
    #* WEB SCRAPPING SECTION
    
    result_scrapping = []
    
    for link in links_menus_web:
        
        #* CONTENT_PAGE SECTION REQUEST
        html_string = get_html_content(link)
        
        dict_scrapping = get_scrapping_content(html_string)
        
        #* CONVERT TO JSON SECTION
        convert_to_json = convert_json(dict_scrapping, 'datos')
        
        result_scrapping.append(dict_scrapping)
        
        
    # #* MONGODB SECTION
    #* connection(<name>, <password>)
    client = connection()              

    try:
        db_project = client['project_menus']
        menus_collection = db_project['project_menus_prueba']
    
        #* insert menus on database
        menus_collection.insert_many(result_scrapping)
    
        # #* Get all documents of menus
        find_menus = menus_collection.find({}, {"_id":0})

        print('*'*50)
        #*Imprimir resultado con documentos
        print(dumps(find_menus, indent=4))
        print('*'*50)
        
    except Exception as err:
        print('ERROR: ', err.args)
    
    else:
        print('*'*50)
        print('\n Se ha insertado correctamente!!')
    
    return result_scrapping


#*******************************************************


if __name__ == "__main__":
    
    # print(execute_program.__doc__)
    
    #* Ejecuta el programa
    dicctionaries_menus = execute_program()
    
    print('*'*50)
    #*Imprimir resultado con documentos
    print(dumps(dicctionaries_menus, indent=4))
    print('*'*50)
