
Advertencia: Esta app se ha ideado con la idea probar el manejo remoto de las BD en local. Si se introducen los datos solicitados por el programa, un DROP en la interfaz implica un DROP en la BD o tabla lo que puede implicar pérdida de la información.

La "SQL Query App" es una aplicación gráfica desarrollada en Python utilizando la biblioteca Tkinter. Esta herramienta está diseñada para facilitar la ejecución de consultas SQL en una base de datos MySQL. Además, verifica la conectividad de la IP y el puerto especificados, proporcionando una solución completa para la interacción con bases de datos MySQL. 

Características de la Interfaz
La interfaz de usuario de la aplicación es intuitiva y amigable. Al abrir la aplicación, los usuarios ven un título destacado "SQL Query App" en negrita, lo que proporciona una presentación clara de la funcionalidad principal del programa. Debajo del título, se encuentra una imagen cargada desde "imagen.png", redimensionada a 50x50 píxeles y centrada en la interfaz, añadiendo un toque visual atractivo.

Entradas de Usuario
La aplicación permite a los usuarios ingresar información necesaria para conectarse a una base de datos MySQL:

Dirección IP: Campo de entrada para la dirección IP del servidor MySQL, con un valor predeterminado de '127.0.0.1'.
Puerto: Campo de entrada para el puerto del servidor MySQL, con el puerto por defecto '3306'.
Usuario: Campo de entrada para el nombre de usuario de MySQL, predeterminado a 'root'.
Contraseña: Campo de entrada para la contraseña del usuario de MySQL, oculto con asteriscos.
Nombre de la BD: Campo de entrada para el nombre de la base de datos a la que se desea conectar, predeterminado a 'test'.
Sentencia SQL: Campo de entrada para la consulta SQL que se desea ejecutar. Por defecto, se muestra una sentencia SQL para crear una tabla llamada ITSELISA.
Funcionalidad Principal
Al pulsar el botón "Ejecutar Consulta", la aplicación intenta conectarse a la base de datos MySQL utilizando las credenciales y parámetros proporcionados. Una vez establecida la conexión, la aplicación ejecuta la consulta SQL ingresada por el usuario. Los resultados de la consulta se muestran en un área de texto en la parte inferior de la interfaz. Este área de texto incluye una barra de desplazamiento para facilitar la visualización de grandes volúmenes de datos.

Además de ejecutar la consulta SQL, la aplicación verifica la conectividad a la dirección IP y puerto especificados. Utilizando la biblioteca socket, intenta establecer una conexión TCP con el servidor MySQL. El resultado de esta verificación se muestra también en el área de resultados, informando al usuario si la conexión fue exitosa o si hubo algún error.

Módulos y Librerías
La aplicación utiliza varias bibliotecas de Python para su funcionamiento:

Tkinter: Para crear la interfaz gráfica de usuario.
mysql.connector: Para conectarse y ejecutar consultas en la base de datos MySQL.
socket: Para verificar la conectividad IP y puerto.
PIL (Pillow): Para cargar y mostrar la imagen en la interfaz.
datetime: (Aunque no se usa en este ejemplo específico, está importada, presumiblemente para futuras funcionalidades relacionadas con la fecha y hora).
Diseño y Usabilidad
La interfaz está diseñada para ser sencilla y directa, facilitando a los usuarios la introducción de los datos necesarios y la ejecución de consultas SQL. Los campos de entrada están organizados lógicamente y etiquetados claramente. La inclusión de valores predeterminados en los campos de IP, puerto, usuario y base de datos reduce la cantidad de datos que el usuario debe ingresar manualmente, haciendo que la aplicación sea más fácil de usar.

El área de resultados proporciona un feedback inmediato sobre la ejecución de la consulta y la conectividad del servidor, lo que es crucial para tareas de diagnóstico y validación en entornos de desarrollo y producción.

Conclusión
En resumen, la "SQL Query App" es una herramienta útil y eficiente para cualquier persona que necesite interactuar con bases de datos MySQL. Su interfaz gráfica facilita la ejecución de consultas y la verificación de la conectividad, convirtiéndola en una solución práctica tanto para desarrolladores como para administradores de bases de datos.
