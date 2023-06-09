# Proyecto Integrador Alkemy

## Instalación del proyecto
Los pasos para poner en marcha el proyecto son los siguientes:
- Paso 1: Entrar en la consola e ingresar este comando pip install -r requeriments.txt
- Paso 2: Ejecutar el comando python manage.py migrate
- Paso 3: Ejecutar el comando python manage.py runserver para correr el servidor
- Paso 4: En cualquier navegador ingresar esta url: http://localhost:8000/ 

## Funcionalidades del módulo Clientes

El módulo **Clientes** proporciona las siguientes funcionalidades:

- ##### Registro de un nuevo cliente:
    - URL: `/clientes/nuevo`
    - Método: POST
    - Descripción: Esta función permite registrar un nuevo cliente en el sistema. Se espera que se envíen los datos del cliente (nombre y apellido) en una solicitud POST.
![](/static/img/registrar-cliente.png)

- ##### Listado de clientes:
    - URL: `/clientes/listado`
    - Método: GET
    - Descripción: Esta función muestra una lista de todos los clientes registrados en el sistema.
![](/static/img/lista-clientes.png)

- ##### Activar cliente:
    - URL: `/clientes/activar/id_cliente`
    - Método: GET
    - Descripción: Esta función activa un cliente específico en el sistema, identificado por su ID.

- ##### Desactivar cliente:
    - URL: `/clientes/desactivar/id_cliente`
    - Método: GET
    - Descripción: Esta función desactiva un cliente específico en el sistema, identificado por su ID.

- ##### Actualizar cliente:
    - URL: `/clientes/actualizar/id_cliente`
    - Método: GET, POST
    - Descripción: Esta función permite actualizar los datos de un cliente específico en el sistema, identificado por su ID. Se puede acceder a la página de actualización a través de una solicitud GET y se espera que se envíen los datos actualizados en una solicitud POST. Los datos actualizados incluyen el nombre y el apellido del cliente.
![](/static/img/actualizar-cliente.png)

## Funcionalidades del módulo Empleados

El módulo **Empleados** proporciona las siguientes funcionalidades:

- ##### Registro de un nuevo empleado:
    - URL: `/empleados/nuevo`
    - Método: POST
    - Descripción: Esta función permite registrar un nuevo empleado en el sistema. Se espera que se envíen los datos del empleado (nombre, apellido y número de legajo) en una solicitud POST.
![](/static/img/registrar-empleado.png)

- ##### Listado de empleados:
    - URL: `/empleados/listado`
    - Método: GET
    - Descripción: Esta función muestra una lista de todos los empleados registrados en el sistema.
![](/static/img/lista-empleados.png)

- ##### Activar empleado:
    - URL: `/empleado/activar/id_empleado`
    - Método: GET
    - Descripción: Esta función activa un empleado específico en el sistema, identificado por su ID.

- ##### Desactivar empleado:
    - URL: `/empleados/desactivar/id_empleado`
    - Método: GET
    - Descripción: Esta función desactiva un empleado específico en el sistema, identificado por su ID.

- ##### Actualizar empleado:
    - URL: `/empleados/actualizar/id_empleado`
    - Método: GET, POST
    - Descripción: Esta función permite actualizar los datos de un empleado específico en el sistema, identificado por su ID. Se puede acceder a la página de actualización a través de una solicitud GET y se espera que se envíen los datos actualizados en una solicitud POST. Los datos actualizados incluyen el nombre, el apellido y el número de legajo del empleado.
![](/static/img/actualizar-empleado.png)

## Funcionalidades del módulo Coordinadores

El módulo **Coordinadores** proporciona las siguientes funcionalidades:

- ##### Registro de un nuevo coordinador:
    - URL: `/coordinadores/nuevo`
    - Método: POST
    - Descripción: Esta función permite registrar un nuevo coordinador en el sistema. Se espera que se envíen los datos del coordinador (nombre, apellido, DNI y Fecha de alta) en una solicitud POST.
![](/static/img/registrar-coordinador.PNG)

- ##### Listado de coordinadores:
    - URL: `/coordinadores/listado`
    - Método: GET
    - Descripción: Esta función muestra una lista de todos los coordinadores registrados en el sistema.
![](/static/img/lista-coordinadores.PNG)

- ##### Activar coordinador:
    - URL: `/coordinadores/activar/id_coordinador`
    - Método: GET
    - Descripción: Esta función activa un coordinador específico en el sistema, identificado por su ID.

- ##### Desactivar coordinador:
    - URL: `/coordinadores/desactivar/id_coordinador`
    - Método: GET
    - Descripción: Esta función desactiva un coordinador específico en el sistema, identificado por su ID.

- ##### Actualizar coordinador:
    - URL: `/coordinadores/actualizar/id_empleado`
    - Método: GET, POST
    - Descripción: Esta función permite actualizar los datos de un coordinador específico en el sistema, identificado por su ID. Se puede acceder a la página de actualización a través de una solicitud GET y se espera que se envíen los datos actualizados en una solicitud POST. Los datos actualizados incluyen el nombre, el apellido, DNI y la fecha de alta del coordinador.
![](/static/img/actualizar-coordinador.PNG)

## Funcionalidades del módulo servicio


El módulo **Servicios** proporciona las siguientes funcionalidades:

- ##### Registro de un nuevo Servicio
    - URL: /servicios/nuevo
    - Método: POST
    - Descripción: Permite registrar un nuevo servicio en el sistema.
    ![](/static/img/registrar-servicio.png)
- ##### Listado de servicios:
    - URL: `/servicios/listado`
    - Método: GET
    - Descripción: Esta función muestra una lista de todos los servicios registrados en el sistema.
![](/static/img/lista-servicios.png)

- ##### Activar servicio:
    - URL: `/servicios/activar/id_servicio`
    - Método: GET
    - Descripción: Activa un servicio específico en el sistema, identificado por su ID.

- ##### Desactivar servicio:
    - URL: `/servicios/desactivar/id_servicio`
    - Método: GET
    - Descripción:Desactiva un servicio específico en el sistema, identificado por su ID.

- ##### Actualizar servicio:
    - URL: `/servicios/actualizar/id_servicio`
    - Método: GET, POST
    - Descripción: Permite actualizar los datos de un servicio específico en el sistema, identificado por su ID. Se puede acceder a la página de actualización a través de una solicitud GET y se espera que se envíen los datos actualizados en una solicitud POST. Los datos actualizados incluyen el nombre, la descripcion y el precio del servicio.
![](/static/img/actualizar-servicio.png)

## Funcionalidades del módulo Reserva de Servicios

El módulo **Reserva de Servicios** proporciona las siguientes funcionalidades:

- ##### Registro de una nueva reserva de servicio:
    - URL: `/reservas/nuevo`
    - Método: POST
    - Descripción: Esta función permite registrar una nueva reserva de servicio en el sistema. Se espera que se envíen los datos de la reserva (fecha, hora, cliente, empleado y servicio) en una solicitud POST.
![](/static/img/registrar-reserva.png)

- ##### Listado de reservas de servicios:
    - URL: `/reservas/listado`
    - Método: GET
    - Descripción: Esta función muestra una lista de todas las reservas de servicios registradas en el sistema.
![](/static/img/lista-reservas.png)

- ##### Activar reserva de servicio:
    - URL: `/reservas/activar/id_reserva`
    - Método: GET
    - Descripción: Esta función activa una reserva de servicio específica en el sistema, identificada por su ID.

- ##### Desactivar reserva de servicio:
    - URL: `/reservas/desactivar/id_reserva`
    - Método: GET
    - Descripción: Esta función desactiva una reserva de servicio específica en el sistema, identificada por su ID.

- ##### Actualizar reserva de servicio:
    - URL: `/reservas/modificar/id_reserva`
    - Método: GET, POST
    - Descripción: Esta función permite actualizar los datos de una reserva de servicio específica en el sistema, identificada por su ID. Se puede acceder a la página de actualización a través de una solicitud GET y se espera que se envíen los datos actualizados en una solicitud POST. Los datos actualizados incluyen la fecha, el cliente, el responsable, el empleado, el servicio de la reserva y el precio.
![](/static/img/actualizar-reserva.png)

***

## Funcionalidades de la API del sistema
- #### Listar servicios en formato JSON:
    - URL: `/api/servicios`
    - Método: GET
    - Descripción: Esta función devuelve una lista de servicios en formato JSON. Proporciona información sobre los servicios disponibles, incluyendo el ID, nombre y precio de cada servicio.
![](/static/img/api-listado-servicios.png)

- #### Mostrar información de un servicio en formato JSON:
    - URL: `/api/servicios/id_servicio`
    - Método: GET
    - Descripción: Esta función devuelve un objeto JSON que representa el servicio con el ID especificado. Proporciona información detallada sobre el servicio, incluyendo el ID, nombre, descripción y precio.
![](/static/img/api-filtro-id-servicios.png)

- #### Listar coordinadores en formato JSON:
    - URL: `/api/coordinadores`
    - Método: GET
    - Descripción: Esta función devuelve una lista de coordinadores en formato JSON. Proporciona información sobre los coordinadores registrados, incluyendo el ID, nombre, DNI, fecha de alta y la propiedad activo de cada coordinador.
![](/static/img/api-listado-coordinadores.png)

- #### Listar empleados en formato JSON:
    - URL: `/api/empleados`
    - Método: GET
    - Descripción: Esta función devuelve una lista de empleados en formato JSON. Proporciona información sobre los empleados registrados, incluyendo el ID, nombre, apellido, numero de legajo y la propiedad activo de cada empleado.
![](/static/img/api-listado-empleados.png)

## Django Admin

El panel de administración de Django es una interfaz incorporada que te permite administrar y manipular los datos de tu aplicación de manera fácil y eficiente. Proporciona una interfaz de usuario amigable y lista para usar para realizar tareas comunes de administración, como agregar, editar y eliminar registros de la base de datos.

#### Acceder a la página de administración:
- Ejecuta tu servidor de desarrollo local de Django utilizando el comando  `python manage.py runserver`.
- Abre tu navegador web y ve a la dirección [http://localhost:8000/admin/](http://localhost:8000/admin/) (reemplaza 'localhost' y '8000' con la configuración correspondiente si estás utilizando un host o puerto diferente).
- Verás la página de inicio de sesión del panel de administración de Django. Ingresa tus credenciales de superusuario para acceder al panel de administración.

![](/static/img/django_admin.png)



#### Uso básico del panel de administración

Una vez que hayas accedido al panel de administración, verás una interfaz intuitiva para administrar tus modelos registrados. Aquí tienes algunas acciones comunes que puedes realizar:
- Ver lista de registros: En la página principal del panel de administración, verás una lista de los modelos registrados. Haz clic en uno de los modelos para ver la lista de registros existentes.

![](/static/img/django_admin2.png)


- Agregar un nuevo registro: En la página de lista de registros de un modelo, haz clic en el botón "Agregar" para crear un nuevo registro en la base de datos. Luego, completa los campos del formulario y guarda el registro.

![](/static/img/django_admin6.png)

- Editar un registro existente: En la lista de registros de un modelo, puedes hacer clic en un registro para ver su detalle. Desde allí, puedes realizar modificaciones y guardar los cambios.

![](/static/img/django_admin3.png)


- Eliminar un registro: En la lista de registros de un modelo, cada registro tiene una opción para eliminarlo. Ten cuidado, ya que esto eliminará permanentemente el registro de la base de datos.

![](/static/img/django_admin4.png)


- Búsqueda y filtrado: El panel de administración de Django proporciona capacidades de búsqueda y filtrado para encontrar registros específicos. Utiliza la barra de búsqueda en la parte superior de la lista de registros o los filtros disponibles en el panel lateral para refinar los resultados.

![](/static/img/django_admin5.png)

- #### Listar empleados en formato JSON:
    - URL: `/api/clientes`
    - Método: GET
    - Descripción: Esta función devuelve una lista de clientes en formato JSON. Proporciona información sobre los clientes registrados, incluyendo el ID, nombre, apellido y si el cliente está activo.
![](/static/img/api-listado-clientes.png)
