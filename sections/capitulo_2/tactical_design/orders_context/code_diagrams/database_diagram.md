##### Bounded Context Database Design Diagram

La base de datos persiste los pedidos ligados a las ordenes, registrando snapshopts de el producto comprado (para mayor consistencia por si los precios cambian). Además, se persisten los datos de los clientes necesarios para registrar en el pedido.

<img src="../../../../../img/tactical-design/orders/db.png" alt="Orders db diagram">