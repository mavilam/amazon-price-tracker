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

### Crear un bot de telegram
Pues ver como crear un bot fácilmente [aquí](https://core.telegram.org/bots#3-how-do-i-create-a-bot).
### Obtener chat id de telegram
1. Busca en telegram el bot @RawDataBot
2. Pulsa /start
3. Escribe un mensaje
4. En la respuesta habrá un campo "from" y dentro un campo "id", ese es tu chat id

### Configurar el proceso en tu propia máquina
Puedes configurar una entrada en la tabla de cron de tu propio ordenador. Los precios no suelen fluctuar en cuestion de minutos, por lo que con ejecutarse una vez al día suele ser suficiente. 
Ejecutando el siguiente comando puedes editar la tabla de cron:
```bash
crontab -e
```
Si añades la siguiente linea se ejecutará el proceso todos los días a las 10 am:
```
0 10 * * * python {path al proyecto}/amazon-price-tracker/tracker/main.py
```

## Próximos pasos
- [x] Añadir una opción para insertar un producto por parámetros. 
- [ ] Mejorar sistema de log. 
- [ ] Hacer código más defensivo