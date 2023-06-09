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

- #### Listar empleados en formato JSON:
    - URL: `/api/clientes`
    - Método: GET
    - Descripción: Esta función devuelve una lista de clientes en formato JSON. Proporciona información sobre los clientes registrados, incluyendo el ID, nombre, apellido y si el cliente está activo.
![](/static/img/api-listado-clientes.png)

