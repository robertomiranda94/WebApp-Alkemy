# Proyecto Integrador Alkemy

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
