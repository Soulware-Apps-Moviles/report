<h4 id="shop-domain-layer">Domain Layer</h4>

| Archivo / Carpeta                                  | Propósito                                                      | Tipo de recurso |
| -------------------------------------------------- | -------------------------------------------------------------- | --------------- |
| `model/aggregates/Shop.java`                       | Agregado raíz, representa una bodega                           | Aggregate       |
| `model/aggregates/TrustedClient.java`            | Agregado raíz de cliente confiable                             | Aggregate       |
| `model/aggregates/Shopkeeper.java`                 | Agregado raíz de tendero                                       | Aggregate       |
| `model/aggregates/Policy.java`                     | Agregado raíz de política de la tienda (1:1 con Shop)          | Aggregate       |
| `model/valueobjects/ShopId.java`                   | Identificador de Shop                                          | Value Object    |
| `model/valueobjects/TrustedClientId.java`        | Identificador de TrustedClient                               | Value Object    |
| `model/valueobjects/ShopkeeperId.java`             | Identificador de Shopkeeper                                    | Value Object    |
| `model/valueobjects/PolicyId.java`                 | Identificador de Policy                                        | Value Object    |
| `model/commands/AddTrustedClientCommand.java`    | Datos para agregar cliente confiable a una tienda              | Command         |
| `model/commands/RemoveTrustedClientCommand.java` | Datos para remover cliente confiable                           | Command         |
| `model/commands/HireShopkeeperCommand.java`        | Datos para contratar tendero                                   | Command         |
| `model/commands/FireShopkeeperCommand.java`        | Datos para despedir tendero                                    | Command         |
| `model/commands/UpdatePolicyCommand.java`          | Datos para actualizar políticas (pago, recojo, crédito máximo) | Command         |
| `model/queries/GetShopByIdQuery.java`              | Consulta de Shop por id                                        | Query           |
| `model/queries/GetAllTrustedClientsQuery.java`   | Consulta lista de clientes confiables de una tienda            | Query           |
| `model/queries/GetAllShopkeepersQuery.java`        | Consulta lista de tenderos de una tienda                       | Query           |
| `model/queries/GetPolicyByShopIdQuery.java`        | Consulta políticas de una tienda                               | Query           |
| `services/ShopCommandService.java`                 | Interfaz de operaciones de escritura de Shop                   | Command Service |
| `services/ShopQueryService.java`                   | Interfaz de operaciones de lectura de Shop                     | Query Service   |
| `services/TrustedClientCommandService.java`      | Interfaz de operaciones de escritura de TrustedClient        | Command Service |
| `services/TrustedClientQueryService.java`        | Interfaz de operaciones de lectura de TrustedClient          | Query Service   |
| `services/ShopkeeperCommandService.java`           | Interfaz de operaciones de escritura de Shopkeeper             | Command Service |
| `services/ShopkeeperQueryService.java`             | Interfaz de operaciones de lectura de Shopkeeper               | Query Service   |
| `services/PolicyCommandService.java`               | Interfaz de operaciones de escritura de Policy                 | Command Service |
| `services/PolicyQueryService.java`                 | Interfaz de operaciones de lectura de Policy                   | Query Service   |
