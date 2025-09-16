#### Domain Layer

| Archivo / Carpeta                               | Propósito                                             | Tipo de recurso |
| ----------------------------------------------- | ----------------------------------------------------- | --------------- |
| `model/aggregates/Inventory.java`               | Agregado raíz, contiene y gestiona productos          | Aggregate       |
| `model/entities/Product.java`                   | Entidad dependiente del agregado                      | Entity          |
| `model/valueobjects/InventoryId.java`           | Identificador del inventario                          | Value Object    |
| `model/valueobjects/ProductId.java`             | Identificador del producto                            | Value Object    |
| `model/commands/AddProductCommand.java`         | Record con datos para añadir producto                 | Command         |
| `model/commands/RemoveProductCommand.java`      | Record con datos para remover producto                | Command         |
| `model/commands/ChangeProductPriceCommand.java` | Record con datos para cambiar precio                  | Command         |
| `model/queries/GetInventoryByShopQuery.java`    | Record con datos para consultar inventario por tienda | Query           |
| `repositories/InventoryRepository.java`         | Contrato de persistencia para Inventory               | Repository      |
| `services/InventoryCommandService.java`         | Expone operaciones de escritura del agregado          | Command Service |
| `services/InventoryQueryService.java`           | Expone operaciones de lectura del agregado            | Query Service   |
