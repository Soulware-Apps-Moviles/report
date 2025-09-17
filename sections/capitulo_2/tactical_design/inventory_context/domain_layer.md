#### Domain Layer

| Archivo / Carpeta                               | Propósito                                             | Tipo de recurso |
| ----------------------------------------------- | ----------------------------------------------------- | --------------- |
| `model/aggregate/Product.java`                   | Agregado raíz del contexto                      | Aggregate          |
| `model/commands/AddProductCommand.java`         | Record con datos para añadir producto                 | Command         |
| `model/commands/RemoveProductCommand.java`      | Record con datos para remover producto                | Command         |
| `model/commands/ChangeProductPriceCommand.java` | Record con datos para cambiar precio                  | Command         |
| `model/queries/GetProductsByShopIdQuery.java`    | Record con datos para consultar inventario por tienda | Query           |
| `services/ProductCommandService.java`         | Expone operaciones de escritura del agregado          | Command Service |
| `services/ProductQueryService.java`           | Expone operaciones de lectura del agregado            | Query Service   |
