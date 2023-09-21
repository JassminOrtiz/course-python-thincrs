# Funcionamiento de las operaciones en una API REST

Las API REST son una forma común de diseñar y desarrollar servicios web que permiten la comunicación entre sistemas. Estas API se basan en el uso de los métodos HTTP para realizar diversas operaciones en recursos. Los cuatro métodos HTTP principales utilizados en una API REST son:

## GET
El método GET se utiliza para recuperar información de un recurso en la API. Cuando se realiza una solicitud GET a un recurso, se espera que el servidor responda con los datos del recurso en el cuerpo de la respuesta. Esta operación es idempotente, lo que significa que no debe tener efectos secundarios en el servidor.

Ejemplo:

GET /api/productos/1


## POST

El método POST se utiliza para crear un nuevo recurso en la API. Cuando se realiza una solicitud POST, se envían datos al servidor en el cuerpo de la solicitud, y el servidor crea un nuevo recurso basado en esos datos. Esta operación no es idempotente, ya que cada solicitud crea un nuevo recurso.

Ejemplo:

POST /api/productos
{
"nombre": "Pechuga de pollo",
"precio": 19.99,
"Description": "Rica pechuga de pollo"
}


## PATCH

El método PATCH se utiliza para actualizar parcialmente un recurso en la API. A diferencia de PUT, que reemplaza completamente el recurso, PATCH permite realizar modificaciones parciales. Se envían los cambios específicos que se desean aplicar al recurso.

Ejemplo:

PATCH /api/productos/1
{
"description": "No tan rica pechuga de pollo"
}


## DELETE

El método DELETE se utiliza para eliminar un recurso en la API. Cuando se realiza una solicitud DELETE a un recurso, el servidor elimina ese recurso si existe. Al igual que GET, esta operación es idempotente.

Ejemplo:

DELETE /api/productos/1

{
}
