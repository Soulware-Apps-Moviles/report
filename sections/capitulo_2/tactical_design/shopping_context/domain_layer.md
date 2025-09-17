#### Domain Layer

| Archivo / Carpeta                                    | Propósito                                                      | Tipo de recurso   |
| ---------------------------------------------------- | -------------------------------------------------------------- | ----------------- |
| `model/aggregates/ShoppingBag.java`                  | Agregado raíz que representa la bolsa de compras actual        | Aggregate         |
| `model/entities/ShoppingBagItem.java`                | Entidad snapshot de un producto de catálogo dentro de la bolsa | Entity            |
| `model/aggregates/ShoppingList.java`                 | Agregado raíz que representa una lista de compras recurrente   | Aggregate         |
| `model/entities/ShoppingListItem.java`               | Entidad snapshot de un producto de catálogo en la lista        | Entity            |
| `model/entities/FavoriteProduct.java`                | Entidad que registra un producto marcado como favorito         | Entity            |
| `model/valueobjects/ShoppingListId.java`             | Identificador de la lista de compras                           | Value object      |
| `model/valueobjects/ShoppingListItemId.java`         | Identificador del ítem dentro de la lista de compras           | Value object      |
| `model/valueobjects/CatalogItemId.java`              | Identificador del producto de catálogo                         | Value object      |
| `model/valueobjects/ClientId.java`                   | Identificador del cliente                                      | Value object      |
| `model/interfaces/CatalogProductReference.java`      | Interfaz común para snapshots de productos de catálogo         | Domain interface  |
| `model/commands/CreateShoppingListCommand.java`   | Record para crear una nueva lista de compras         | Command         |
| `model/commands/AddItemToShoppingListCommand.java`| Record para agregar un producto a una lista de compras | Command       |
| `model/commands/RemoveItemFromShoppingListCommand.java` | Record para eliminar un producto de una lista de compras | Command |
| `model/commands/MarkProductAsFavoriteCommand.java`| Record para marcar un producto como favorito         | Command         |
| `model/queries/GetShoppingListsQuery.java`        | Record para consultar todas las listas de compras de un cliente | Query |
| `model/queries/GetFavoritesQuery.java`            | Record para consultar los productos favoritos        | Query           |
| `services/ShoppingCommandService.java`            | Expone operaciones CUD sobre shopping (bolsa, listas, favoritos) | Command Service |
| `services/ShoppingQueryService.java`              | Expone operaciones de lectura sobre shopping (bolsa, listas, favoritos) | Query Service   |

