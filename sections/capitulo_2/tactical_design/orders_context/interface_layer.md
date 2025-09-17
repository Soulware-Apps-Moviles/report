#### Interface Layer

| Carpeta / Archivo    | Propósito | Tipo de recurso |
| -------------------- | --------- | --------------- |
| `acl/OrdersContextFacade.java` | Interface para exponer capacidades de Orders a otros bounded contexts | ACL Facade |
| `rest/controllers/OrdersController` | Interface para exponer capacidades de Orders mediante endpoints REST | REST Controller | 
| `rest/assemblers/GetSuitableShopsQueryFromResourceAssembler.java`  | Convierte un `GetSuitableShopsResource` en un `GetSuitableShopsQuery`  | Resource → Query Assembler |
| `rest/assemblers/GetOrderQueryFromResourceAssembler.java`  | Convierte un `GetOrderResource` en un `GetOrderQuery`  | Resource → Query Assembler |
| `rest/assemblers/ShopResourceFromEntityAssembler.java`  | Convierte un `Shop` en un `ShopResource`  | Entity → Resource Assembler |
| `rest/controllers/OrdersController` | Interface para exponer capacidades de Orders mediante endpoints REST | REST Controller | 