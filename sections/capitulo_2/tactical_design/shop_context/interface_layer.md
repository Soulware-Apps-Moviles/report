#### Interface Layer

| Carpeta / Archivo                                                     | Propósito                                                | Tipo de recurso              |
| --------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------- |
| `rest/controllers/ShopController.java`                                | Endpoints REST de Shop                                   | REST Controller              |
| `rest/controllers/TrustedClientController.java`                     | Endpoints REST de TrustedClient                        | REST Controller              |
| `rest/controllers/ShopkeeperController.java`                          | Endpoints REST de Shopkeeper                             | REST Controller              |
| `rest/controllers/PolicyController.java`                              | Endpoints REST de Policy                                 | REST Controller              |
| `rest/resources/AddTrustedClientResource.java`                      | Entrada para agregar cliente confiable                   | Resource (Input)             |
| `rest/resources/TrustedClientResource.java`                         | Salida para representar cliente confiable                | Resource (Output)            |
| `rest/resources/HireShopkeeperResource.java`                          | Entrada para contratar tendero                           | Resource (Input)             |
| `rest/resources/ShopkeeperResource.java`                              | Salida para representar tendero                          | Resource (Output)            |
| `rest/resources/UpdatePolicyResource.java`                            | Entrada para actualizar políticas de bodega              | Resource (Input)             |
| `rest/resources/PolicyResource.java`                                  | Salida para representar política de bodega               | Resource (Output)            |
| `rest/assemblers/AddTrustedClientCommandFromResourceAssembler.java` | Convierte resource a comando `AddTrustedClientCommand` | Resource → Command Assembler |
| `rest/assemblers/TrustedClientResourceFromEntityAssembler.java`     | Convierte entidad a resource `TrustedClientResource`   | Entity → Resource Assembler  |
| `rest/assemblers/HireShopkeeperCommandFromResourceAssembler.java`     | Convierte resource a comando `HireShopkeeperCommand`     | Resource → Command Assembler |
| `rest/assemblers/ShopkeeperResourceFromEntityAssembler.java`          | Convierte entidad a resource `ShopkeeperResource`        | Entity → Resource Assembler  |
| `rest/assemblers/UpdatePolicyCommandFromResourceAssembler.java`       | Convierte resource a comando `UpdatePolicyCommand`       | Resource → Command Assembler |
| `rest/assemblers/PolicyResourceFromEntityAssembler.java`              | Convierte entidad a resource `PolicyResource`            | Entity → Resource Assembler  |
