<h4 id="catalog-domain-layer">Domain Layer</h4>

| Archivo / Carpeta                        | Propósito                                     | Tipo de recurso |
| ---------------------------------------- | --------------------------------------------- | --------------- |
| `model/aggregates/Product.java`          | Agregado raíz del catálogo (solo lectura)     | Aggregate       |
| `model/queries/GetAllProductsQuery.java` | Record para listar todos los productos        | Query           |
| `model/queries/GetProductByIdQuery.java` | Record para consultar un producto por id      | Query           |
| `services/ProductQueryService.java`      | Expone operaciones de lectura sobre productos | Query Service   |
