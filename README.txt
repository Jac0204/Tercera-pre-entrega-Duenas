EXPLICACIÓN DE LOS ARCHIVOS

-AppMain:

--views.py
Se encuentra la lógica de la inserción y lógica del formulario de los modelos

--urls.py
Se encuentra las rutas de la aplicación, relacionadas a los modelos correspondientes

--models.py
Se encuentra los modelos de las entidades con sus atributos. La clase Categoria hace referencia en la clase Producto, por lo que se usa un ForeingKey

--forms.py
Se encuentra las clases de los formularios de las entidades:
ClienteForm: Mismas columnas que su modelo
CategoriaForm: Mismas columnas que su modelo
ProductoForm: Mismas columnas que su modelo. Además, se agregó el tipo de dato ChoiceField que hace referencia al modelo Categoria para el input "select" del formulario

--admin.py
Se encuentra la conexión con el módulo de administración y las clases del proyecto
usuario: admin
contraseña: admin12345

--static/
Carpeta que almacena los archivos css, imágenes y js del proyecto

--templates/
Carpeta que almacena los archivos HTML, divididos en su carpeta correspondiente de cada clase; además, los layouts usados para esta aplicación.

EXPLICACIÓN DE LA APLICACIÓN

-Inicio:

Página que muestra el total de cada clase: Cliente, categoría y producto

-Cliente:

Página que permite mostrar, agregar y buscar clientes

-Categoría:

Página que permite mostrar, agregar y buscar categorías

-Producto:

Página que permite mostrar, agregar y buscar productos

Se hace uso de la librería Bootstrap para los estilos de la aplicación