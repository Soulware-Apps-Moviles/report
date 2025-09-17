#### Interface Layer

| Carpeta / Archivo                                                       | Propósito                                                                       | Tipo de recurso              |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------- |
| `rest/controllers/ShoppingController.java`                              | Controlador REST para exponer endpoints de bolsa, listas de compra y favoritos   | REST Controller              |
| `rest/resources/AddToBagResource.java`                                  | Resource de entrada para agregar un producto a la bolsa (equivalente a un command) | Resource (Input)         |
| `rest/resources/ShoppingBagResource.java`                               | Resource de salida que representa la bolsa de compras de un cliente             | Resource (Output)        |
| `rest/resources/CreateShoppingListResource.java`                        | Resource de entrada para crear una lista de compras                             | Resource (Input)         |
| `rest/resources/ShoppingListResource.java`                              | Resource de salida que representa una lista de compras                          | Resource (Output)        |
| `rest/resources/FavoriteProductResource.java`                           | Resource de salida que representa un producto favorito                          | Resource (Output)        |
| `rest/assemblers/AddToBagCommandFromResourceAssembler.java`             | Convierte un `AddToBagResource` en un `AddToBagCommand`                         | Resource → Command Assembler |
| `rest/assemblers/ShoppingBagResourceFromEntityAssembler.java`           | Convierte un `ShoppingBag` (aggregate) en `ShoppingBagResource`                 | Entity → Resource Assembler  |
| `rest/assemblers/CreateShoppingListCommandFromResourceAssembler.java`   | Convierte un `CreateShoppingListResource` en un `CreateShoppingListCommand`     | Resource → Command Assembler |
| `rest/assemblers/ShoppingListResourceFromEntityAssembler.java`          | Convierte un `ShoppingList` (aggregate) en `ShoppingListResource`               | Entity → Resource Assembler  |
| `rest/assemblers/FavoriteProductResourceFromEntityAssembler.java`       | Convierte un `FavoriteProduct` en `FavoriteProductResource`                     | Entity → Resource Assembler  |
| `acl/CatalogProductAcl.java`                                            | Interfaz para exponer datos de productos de catálogo al contexto Shopping       | ACL Facade                   |
