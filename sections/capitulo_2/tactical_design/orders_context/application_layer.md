#### Application Layer

| Archivo / Carpeta                                           | Propósito                                            | Tipo de recurso      |
| ----------------------------------------------------------- | ---------------------------------------------------- | -------------------- |
| `internal/commandservices/OrdersCommandServiceImpl.java` | Implementación concreta de `OrdersCommandService`  | Command Service Impl |
| `internal/queryservices/OrdersQueryServiceImpl.java`     | Implementación concreta de `OrdersQueryService`    | Query Service Impl   |
| `internal/acl/OrdersContextFacadeImpl.java`   | Implementación concreta de la interface expuesta a otros contextos para acceder a la lógica de este  | ACL Facade  |
| `internal/outboundservices/acl/ExternalInventoryService.java`                       | Adaptador para consultar productos de `Inventory`  | ACL Service          |
| `internal/outboundservices/acl/ExternalShopService.java`                          | Adaptador para para consultar clientes confiables y políticas de `Shop` | ACL Service |