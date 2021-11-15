*Este proyecto es un fork para adaptar el proyecto original para amazon España y poder usarlo como cli.*
*Todavía en construcción* 

# Amazon Price Tracker
Tracker de productos de amazon que te enviará un mensaje a telegram cuando el precio baje del indicado
## Features
* Capacidad de trackear más de un producto
* Configura el precio de límite de cada producto
* Las alertas te llegarán al chat configurado de telegram
## Cómo usarlo
### Dependencias
Puedes instalar las dependencias con `pip install -r requirements.txt`
### Cómo funciona
1. Clona el repositorio
2. Cambia tu token de telegram y tu id de chat en `settings.py` 
3. Añade linea a linea en tracker/data/data.csv cada producto con el formato [url del producto],[precio objetivo]
4. Ejecuta el script
```bash
python tracker/main.py
```
### Obtener chat id de telegram
1. Busca en telegram el bot @RawDataBot
2. Pulsa /start
3. Escribe un mensaje
4. En la respuesta habrá un campo "from" y dentro un campo "id", ese es tu chat id
## Próximos pasos
- [ ] Añadir una opción para insertar un producto por parámetros. 
- [ ] Mejorar sistema de log. 