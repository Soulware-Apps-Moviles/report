#### Domain Message Flows Modeling

Para detallar el funcionamiento y conexión de los bounded context se ha determinado 3 escenarios que permitan comprender los procesos del negocio. 

**Escenario 1: Pedir orden**
Objetivo: Un cliente quiere registrar una orden en una tienda cercana.
<img src="../../../../img/strategic-design/dmfm/Scenario1.jpg" alt="Scenario 1: Take order">
Se observa como el cliente interactua con la bolsita de compras de la aplicación llevandolo de productos, finalmente esa bolsita de compras nutre a la creación de la orden. Finalmente la bodega seleccionada es notificada y un tendero se encarga de la orden.

**Escenario 2: Entregar orden**
Objetivo: Un tendero quiere atender rapidamente la orden que le corresponde.
<img src="../../../../img/strategic-design/dmfm/Scenario2.jpg" alt="Scenario 2: Deliver order">
Un tendero recibe una orden a través de la aplicación móvil, la prepara con todos los productos especificados. Cuando el cliente llega a la tienda el tendero le hace entrega de su orden y posterior a ello el tendero marca el pedido como entregado en la aplicación móvil, lo cual desencadena un registro de ingreso.

**Escenario 3: Manejo de inventario**
Objetivo: Un dueño quiere actualizar el stock de su tienda a través del conteo de productos.
<img src="../../../../img/strategic-design/dmfm/Scenario3.jpg" alt="Scenario 3: Stock management">
El dueño de la bodega contabiliza manualmente los productos que tiene en tienda y marca con un check los productos con existencias en la bodega.