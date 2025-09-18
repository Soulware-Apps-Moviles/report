<h4 id="inventory-application-layer">Application Layer</h4>

| Archivo / Carpeta                                           | Propósito                                            | Tipo de recurso      |
| ----------------------------------------------------------- | ---------------------------------------------------- | -------------------- |
| `internal/commandservices/ProductCommandServiceImpl.java` | Implementación concreta de `ProductCommandService` | Command Service Impl |
| `internal/queryservices/ProductQueryServiceImpl.java`     | Implementación concreta de `ProductQueryService`   | Query Service Impl   |
| `internal/outboundservices/acl/ExternalCatalogServiceImpl.java`           | Adaptador para consultar productos del `Catalog`     | ACL Service          |
| `acl/InventoryContextFacadeImpl.java`           | Implementación concreta de `InventoryContextFacade`   | ACL Facade          |
