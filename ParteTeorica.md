-   1. Estando en la carpeta del repositorio:
        - ``git init``
        - ``git add .`` (o en su defecto añadir archivos ya existentes uno por uno)
        - ``git commit -m "Comentario del commit"``
        - ``git remote add origin https://github.com/<usuario>/<nombre-repositorio>.git``

        - ``git push origin main``

-   2. Es necesario clonar el repositorio remoto a traves del comando
        - ``git clone https://github.com/<usuario>/<nombre-repositorio>.git``

-   3. Si se crea un objeto directamente a partir de una clase abstracta como tal, el objeto no podra ser creado, el programa lanzara un error indicando que se trata de una clase abstracta. La forma correcta de instanciar un objeto es a partir de crear una clase hija que herede de la clase abstracta, y crear el objeto a partir de la clase hija.
-   4. El decorador ``@abstractmethod`` antes de definir un metodo en una clase abstracta indica que dicho metodo tambien sera abstracto por lo que es necesario que las clases que hereden de esta clase abstracta definan la funcionalidad del metodo
-   5. Eventos relacionados con el mouse, se definen a partir de un metodo dentro de la clase principal de la interfaz, estos son
        - ``mouseDoubleClickEvent()`` se lanzara cuando dentro de la ventana se haga doble click con alguno de los botones del mouse especificados
        - ``mouseMoveEvent()`` se lanzara cuando dentro de la ventana el puntero del mouse se mueva
        - ``mouseReleaseEvent`` se lanzara cuando luego de que se haya presionado algun boton del mouse este mismo sea soltado,
        - Entre otros...
-   6. Un ciclo de eventos es como dice la palabra un ciclo que se ejecuta durante el tiempo de vida de un programa en ejecucion, se encarga de capturar los eventos causados por la interaccion del usuario con el programa, e interpretarlos de la manera que el programador haya definido dentro del codigo.
-   7. Dependiendo del modal de la ventana secundaria, si este fue definido previamente como ``True``, la ventana secundaria al mostrarse bloqueara cualquier evento en la ventana principal. Si el modal de la ventana no fue previamente definido y la ventana secundaria se lanza a partir del metodo ``exec()``, la ventana por defecto bloqueara cualquier evento en la ventana principal, por lo tanto la respuesta es no, en este caso no se podra seguir usando la ventana principal hasta que la ventana secundaria sea cerrada.
-   8.
        -   ``QLabel()``
        -   ``QPushButton()``
        -   ``QLineEdit()``
        -   ``QSpinBox()``
        -   ``QComboBox()``
-   9. Las alternativas son utilizar:
        -   ``QLineEdit()`` Sin embargo, por el comportamiento de este widget es necesario que el string entregado por el mismo sea convertido a un entero (int) o en decimal (float) segun corresponda para su uso como un numero dentro del programa
        -   ``QSpinBox()`` Este widget entrega unicamente valores enteros (int) por medio de su metodo ``value()``
        -   ``QDoubleSpinBox()`` Este widget entrega valores flotantes
        -   ``QSlider()`` Este widget entrega valores enteros dentro de un intervalo definido por el programador (minimo y maximo)
-   10. Es necesario una vez que se tiene el codigo fuente de la ventana creada en QtDesigner, importarlo en un nuevo archivo .py, y ejecutar el metodo que implementa QtDesigner para crear la ventana llamado ``setupUi()`` ademas de heredar de la ventana creada con QtDesigner.