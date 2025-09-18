<h4 id="shopping-application-layer">Application Layer</h4>

| Archivo / Carpeta                                             | Propósito                                                        | Tipo de recurso      |
| ------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------- |
| `internal/commandservices/ShoppingCommandServiceImpl.java`    | Implementación concreta de `ShoppingCommandService`              | Command Service Impl |
| `internal/queryservices/ShoppingQueryServiceImpl.java`        | Implementación concreta de `ShoppingQueryService`                | Query Service Impl   |
| `internal/outboundservices/acl/CatalogExternalService.java` | Adaptador para consultar productos del `Catalog`                 | ACL Service          |
