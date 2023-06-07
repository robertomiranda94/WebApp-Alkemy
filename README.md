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