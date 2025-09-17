#### Application Layer

| Archivo / Carpeta                                              | Propósito                                                      | Tipo de recurso        |
| -------------------------------------------------------------- | ---------------------------------------------------------------| ---------------------- |
| `internal/commandservices/CheckoutCommandServiceImpl.java`     | Implementación concreta de `CheckoutCommandService`            | Command Service Impl   |
| `internal/queryservices/CheckoutQueryServiceImpl.java`         | Implementación concreta de `CheckoutQueryService`              | Query Service Impl     |
| `acl/OrdersContextAclImpl.java`                                | Adaptador para interactuar con el contexto de **Orders**       | ACL Service            |
| `acl/ShopContextAclImpl.java`                                  | Adaptador para interactuar con el contexto de **Shop**         | ACL Service            |
