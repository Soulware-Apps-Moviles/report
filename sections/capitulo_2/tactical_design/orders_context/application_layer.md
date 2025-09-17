#### Application Layer

| Archivo / Carpeta                                           | Propósito                                            | Tipo de recurso      |
| ----------------------------------------------------------- | ---------------------------------------------------- | -------------------- |
| `internal/commandservices/OrdersCommandServiceImpl.java` | Implementación concreta de `OrdersCommandService`  | Command Service Impl |
| `internal/queryservices/OrdersQueryServiceImpl.java`     | Implementación concreta de `OrdersQueryService`    | Query Service Impl   |
| `acl/InventoryProductAclImpl.java`                       | Adaptador para consultar productos de `Inventory`  | ACL Service          |
| `acl/TrustedClientAclImpl.java`                          | Adaptador para para consultar clientes confiables y políticas de `Shop` | ACL Service |