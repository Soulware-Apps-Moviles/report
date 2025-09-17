#### Bounded Context Software Architecture Component Level Diagrams

El componente Orders expone un endpoint para obtener las tiendas idóneas previa la a solicitud de atención de pedido, por lo que IAM protege su acceso. Para dicho fin, es necesario que se comunique con Shop e Inventory. Además, Shopping debe proveer datos para el armado del pedido y Checkout debe ser llamado para el registro de los pagos y deudas generados a consecuencia de la atención del pedido.

<img src="../../../../img/tactical-design/orders/component.png" alt="Catalog Component in C3 Level">