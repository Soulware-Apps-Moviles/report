### Software Deployment Configuration

**LANDING PAGE DEPLOYMENT**

**KOTLIN MOBILE APP**

**API**
Para el despliegue del backend de T'Compro se utilizo una maquina virtual Azure, configurando 

1. Entrar a Azure e ir a Maquinas virtuales

<img src="../../../img/software-configuration/deploy/backend/step_1.png">

2. Seleccionamos la opción de crear una nueva maquina virtual

<img src="../../../img/software-configuration/deploy/backend/step_2.png">

3. Configurar la maquina virtual dentro del grupo de recursos de Soulware. El sistema operativo es Ubuntu 24.04, abriento los puertos 80, 443, 22 para las conexiones externas. Posterior a las configuraciones, creamos la maquina virtual.

<img src="../../../img/software-configuration/deploy/backend/step_3_1.png">
<img src="../../../img/software-configuration/deploy/backend/step_3_2.png">

4. Cuando el despliegue de la maquina virtual termine, nos dirigimos a sus configuraciones de red. Dentro cambiamos a una network interface que soporte IPv6.

<img src="../../../img/software-configuration/deploy/backend/step_4.png">

5. Posterior a ello, con la clave privada SSH que se genero al crear la maquina virtual, ingresamos a ella a través del CMD.

<img src="../../../img/software-configuration/deploy/backend/step_5_1.png">
<img src="../../../img/software-configuration/deploy/backend/step_5_2.png">

6. Dentro de la maquina virtual, ejecutamos comandos para instalar y actualizar paquetes del sistema operativo. Instalamos Java 17, Maven, Git y habilitamos el firewall para que permita la entrada en el puerto 8080.

<img src="../../../img/software-configuration/deploy/backend/step_6.png">

7. Clonamos el repositorio dentro de la maquina virtual y definimos las variables de entorno para la ejecución del backend.

<img src="../../../img/software-configuration/deploy/backend/step_7.png">

8. Corremos la aplicación en segundo plano y verificamos mediante logs que se encuentre operativo.

<img src="../../../img/software-configuration/deploy/backend/step_8.png">

9. Verificamos la disponibilidad del servicio a través de una computadora local.

<img src="../../../img/software-configuration/deploy/backend/step_9.png">