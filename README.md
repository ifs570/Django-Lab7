<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5"> Relaciones de uno a muchos, muchos a muchos y impresion de pdf y emails</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>07</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO::</td><td>04-Julio-2022</td><td>FECHA FIN:</td><td>14-Julio-2022</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">RECURSOS:
    <ul>
        <li><a href="https://www.youtube.com/watch?v=OTmQOjsl0eg">https://www.youtube.com/watch?v=OTmQOjsl0eg</a></li>        
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Anibal Sardon </li>
</ul>
</td>
</<tr>
</tdbody>
</table>

# Django

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

#

## OBJETIVOS Y TEMAS

### OBJETIVOS

- Establecer una conexión entre dos modelos y permitir el acceso, manipulación y consulta eficientes de los datos relacionados.
- Obtener y filtrar los objetos secundarios relacionados, ordenarlos según un atributo específico, realizar consultas agregadas y estadísticas en los datos relacionados, realizar consultas inversas y aprovechar las consultas relacionadas y anidadas para acceder a los datos de manera eficiente. 
- 

### TEMAS
- Relación de uno a muchos
- Relación muchos a muchos
- Impresión de pdfs
- Envio de emails

### MARCO TEORICO
- Una relación de uno a muchos se establece utilizando el campo ForeignKey. Esta relación permite que un modelo tenga una clave foránea que apunte a otro modelo, lo que indica que un objeto en el primer modelo puede estar asociado con múltiples objetos en el segundo modelo.
- Una relación de muchos a muchos se establece utilizando el campo ManyToManyField. Esta relación permite que múltiples objetos de un modelo estén relacionados con múltiples objetos de otro modelo. Django utiliza una tabla de unión para almacenar las relaciones entre los objetos de ambos modelos.
- La impresión de PDF en Django se puede lograr utilizando bibliotecas como ReportLab o WeasyPrint. Estas bibliotecas permiten generar documentos PDF dinámicamente a partir de los datos del modelo de Django.
-  Django proporciona un conjunto de utilidades y clases para enviar correos electrónicos de forma sencilla.

### ACTIVIDADES
   Reproducir las actividades de los videos donde trabajamos:
1.  Relación de uno a muchos
2.  Relación muchos a muchos
3. Impresión de pdfs 
4. Envio de emails
5. Crear su video Flipgrid

#

## INFORME DE LABORATORIO

## Relación de uno a muchos

- Primero instalamos DB Browser for SQLite. para poder ver una interfaz grafica para poder ver la base de datos de SQLite.

    - ![python](img\img1.PNG)

- Veamos si tenemos algunas migraciones. No tenemos cambios detectados
    
    - ![python](img\img2.PNG)

- Cada vez que ejecutamos el proyecto tenemos este mensaje.

    - ![python](img\img3.PNG)

- Ejecutamos las migraciones

    - ![python](img\img4.PNG)

- Al ejecutar se crean las tablas dentro de la base de datos

    - ![python](.\img\img5.PNG)

- En un inicio mi base datos.

    - ![python](.\img\img6.PNG)

- Despues de haber ejecutado las migraciones y actualizado la base datos.(Base de datos por defecto en Django)

    - ![python](.\img\img7.PNG)
  
- Veamos una de nuestras tablas(auth_user)

    - ![python](.\img\img8.PNG)
    - ![python](.\img\img9.PNG)
    - ![python](.\img\img10.PNG)

- Ahora dentro de models.py vamos a crear un modelo especifico.

    - ![python](.\img\img11.PNG)

- Tenemos que conectar la Base de Datos. Dentro de settings.py conectamos nuestra aplicación con el proyecto.

    - ![python](.\img\img12.PNG)

- Realizemos las nuevas migraciones

    - ![python](.\img\img13.PNG)
    - ![python](.\img\img14.PNG)

- Vemos que se crea una nueva carpeta 0001_initial.py, un modelo del proyecto.

    - ![python](.\img\img15.PNG)
    - ![python](.\img\img16.PNG)

- Realizamos la migración, y vemos que se realizo correctamente.

    - ![python](.\img\img17.PNG)

- Si actualizamos nuestra Base de Datos vemos que aumento una tabla.

    - ![python](.\img\img18.PNG)

- La nueva tabla que creamos solo contiene por ahora un id(por defecto) y un name(el que se creo).

    - ![python](.\img\img19.PNG)

- Creamos otra tabla llamada Task. Y vamos a relacionarla con la tabla Project. Para esto usamos el ForeignKey. 

    -  ![python](.\img\img20.PNG)

- Ejecutamos

    -  ![python](.\img\img21.PNG)
    -  ![python](.\img\img22.PNG)
    -  ![python](.\img\img23.PNG)
  
- Al ver el archivo que se creo vemos que tiene una dependencia del archivo anterior.

    - ![python](.\img\img24.PNG)

    - ![python](.\img\img25.PNG)

- Volvemos a aplicar las migraciones

     - ![python](.\img\img26.PNG)


     - ![python](.\img\img27.PNG)

- Actualizamos la base de datos y vemos que aumenta una tabla. 

    -  ![python](.\img\img28.PNG)
    -  ![python](.\img\img29.PNG)

  - Ahora trabajaremos con el shell

    -  ![python](.\img\img30.PNG)
  
- Importamos las dos clases

    - ![python](.\img\img31.PNG)

- Creamos un objeto basado en la clase. En este caso se llama aplicación movil

    - ![python](.\img\img32.PNG)
    - ![python](.\img\img33.PNG)
    - ![python](.\img\img34.PNG)

## Relación de muchos a muchos

- Ahora creo otro proyecto

    - ![python](.\img\img35.PNG)
    - ![python](.\img\img36.PNG)

- Ahora vamos a agregar tareas dentro de Task, vemos que en un inicio no tenemos niguna tarea. Por eso nos muestra un QuerySet[] vacio.

    - ![python](.\img\img37.PNG)
    - ![python](.\img\img38.PNG)

- Vamos a agregar una tarea dentro del proyecto Task. Podemos ver que dentro de Task tenemos tablas como titulo, descripcion y proyecto.

    - ![python](.\img\img39.PNG)
    - ![python](.\img\img40.PNG)
    - ![python](.\img\img41.PNG)
    - ![python](.\img\img42.PNG)
    - ![python](.\img\img43.PNG)
#

## Enviar E-mail en Django

- Primero incluimos las Urls de envio
    - ![python](.\img\img44.PNG)
    - ![python](.\img\img45.PNG)
    - ![python](.\img\img46.PNG)

- Luego realizamos algunas configuraciones de correo.

    - ![python](.\img\img47.PNG)

- Importamos redirect, EmailMessage.
    - ![python](.\img\img48.PNG)

- En views.py creamos la función index y correo
    - ![python](.\img\img49.PNG)
    - ![python](.\img\img50.PNG)

- Dentro de los templates tendremos correo.html y home.html
  
    - ![python](.\img\img51.PNG)
    - ![python](.\img\img52.PNG)

- Ejecutamos

    - ![python](.\img\img54.PNG)
    - ![python](.\img\img55.PNG)
    - ![python](.\img\img56.PNG)

- Enviaremosun mensaje de prueba a mi correo institucional.

    - ![python](.\img\img57.PNG)

- Dentro de la url nos dice que el mensaje es valido. 

    - ![python](.\img\img58.PNG)

- Ahora nos dirigimos a nuestro correo para ver el mensaje.

    - ![python](.\img\img59.PNG)
    - ![python](.\img\img60.PNG)

#

## Generar pdf en Django

- Primero añadimos la aplicación

    - ![python](.\img\img61.PNG)

    - urls.py project
  
    - ![python](.\img\img62.PNG)

    -urls.py app

    - ![python](.\img\img63.PNG)

- En views.py creamos dos funciones(home y pdf) dentro de las cuales tenemos los templates(home.html y pdf.html) e importamos html2pdf.

    - ![python](.\img\img64.PNG)

    - pdf.html
  
    - ![python](.\img\img65.PNG)

    - home.html

    - ![python](.\img\img66.PNG)

- Ejecutamos el programa

    - ![python](.\img\img67.PNG)
    - ![python](.\img\img68.PNG)

- Creamos un archivo pdf.py, aqui importamos bit IO, get_template y pisa.

    - ![python](.\img\img69.PNG)
    - ![python](.\img\img70.PNG)

- Ejecutamos el programa y damos generar pdf y nos imprimira el pdf.

    - ![python](.\img\img71.PNG)
    - ![python](.\img\img72.PNG)


#

## REFERENCIAS
- Django tutorial. https://www.youtube.com/watch?v=X7DWErkNVJs&t=400s
- Django tutorial. https://www.youtube.com/watch?v=B7EIK9yVtGY&t=318s
- https://www.codingforentrepreneurs.com/blog/html-template-to-pdf-in-django/
- [Bootstrap]: https://getbootstrap.com/docs/5.2/examples/pricing/

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
