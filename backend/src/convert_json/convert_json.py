import json
# se importa un diccionario

"""
JSON MODULE
"""

def convert_json(myRecord, filename):
    
    #* PRECONDICIONALES
    assert isinstance(myRecord, dict)
    assert isinstance(filename, str)
    
    mensaje = f"El diccionario ha sido convertido a json en este archivo: {filename}.json"
    try:
        # j = json.dumps(myRecord)
        # para que pueda funcionar with open, la ruta empieza desde la raíz hasta la carpeta donde esta el archivo donde queremos guardar los datos
        with open(f"backend/json/{filename}.json", "a", encoding="utf-8") as f: 
            x = json.dumps(myRecord, indent=4)
            f.write(x + ',' + '\n')
            # f.close()
    except json.JSONDecodeError as jsonerror:
        mensaje = "Decoding json ha fallado" 
    except FileNotFoundError as notfile:
        mensaje = "Archivo no encontrado"
    except Exception as exc:
        print("Ha ocurrido un error: ", exc.args)
        
    return mensaje


