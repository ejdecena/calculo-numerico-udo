INSTRUCCIONES A SEGUIR PARA EL DESARROLLO DE LA ACTIVIDAD.

PASO 1: Desde su terminal, clone el repositorio de la actividad:
```bash
$ git clone https://github.com/ejdecena/calculo-numerico-udo.git
```

PASO 2: Vaya al repositorio clonado y cree una rama en su local:
```bash
$ cd calculo-numerico-udo
$ git checkout -b nombre_apellido_biseccion
```

PASO 3: Cree su archivo .py para la actividad:
```bash
$ cat ejercicio_biseccion.py > nombre_apellido_biseccion.py
```

PASO 4: En su archivo `nombre_apellido_biseccion.py`, implemente las funciones `error_relativo(vact, vant)` y `biseccion(fx, inter, er, n)`. Para probar sus funciones, puede correr su archivo .py así:
```bash
$ python3 nombre_apellido_biseccion.py
```

PASO 5: Luego que tenga las funciones implementadas y probadas, vaya al archivo `test_ejercicios.py` y agregue la importación de su archivo .py, tal y como se muestra en el código fuente del archivo `test_ejercicios.py`.

PASO 6: Cree un commit, actualice su repo y suba sus cambios al repositorio en GitHub:
```bash
$ git add .
$ git commit -m "Ejercicio de biseccion."
$ git checkout master
$ git pull master
$ git checkout nombre_apellido_biseccion
$ git rebase master
$ git push origin nombre_apellido_biseccion
```