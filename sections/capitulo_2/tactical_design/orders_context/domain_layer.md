#### Domain Layer

| Archivo / Carpeta                                 | Propósito                                            | Tipo de recurso |
| ------------------------------------------------- | ---------------------------------------------------- | --------------- |
| `model/aggregates/Order.java`                     | Agregado raíz de orders                              | Aggregate       |
| `model/entities/Orderline.java`                   | Entidad snapshot de un producto al momento de compra | Entity          |
| `model/valueobjects/OrderStatus.java`             | Enum que registra los estados de una orden           | Value object    |
| `model/valueobjects/PaymentMethod.java`           | Enum que registra el método de pago para la orden    | Value object    |
| `model/valueobjects/DeliveryMethod.java`          | Enum que registra la forma de recojo de la orden     | Value object    |
| `model/aggregates/Shop.java`                     | Agregado secundario en Orders                              | Aggregate       |
| `model/valueobjects/OrderId.java`                 | Identificador de la orden                            | Value object    |
| `model/valueobjects/OrderlineId.java`             | Identificador de la linea de orden                   | Value object    |
| `model/commands/GetSuitableShopsQuery.java`       | Record para consultar las tiendas idóneas            | Query           |
| `model/queries/PlaceOrderCommand.java`            | Record para colocar una orden                        | Command         |
| `model/queries/AcceptOrderCommand.java`           | Record para aceptar una orden                        | Command         |
| `model/queries/RejectOrderCommand.java`           | Record para rechazar una orden                       | Command         |
| `model/queries/CancelOrderCommand.java`           | Record para cancelar una orden                       | Command         |
| `model/queries/MarkOrderAsReadyCommand.java`      | Record para señalar una orden como lista             | Command         |
| `model/queries/MarkOrderAsDispatchedCommand.java` | Record para señalar una orden como despachada        | Command         |
| `model/queries/MarkOrderAsDeliveredCommand.java`  | Record para señalar una orden como entregada         | Command         |
| `services/OrdersQueryService.java`               | Expone operaciones de lectura sobre productos          | Query Service   |
| `services/OrdersCommandService.java`             | Expone operaciones CUD sobre ordenes                 | Command Service |
| `services/ShopQueryService.java`             | Expone operaciones CUD sobre ordenes                 | Command Service |