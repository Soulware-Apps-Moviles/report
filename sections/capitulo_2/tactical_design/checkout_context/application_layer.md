<h4 id="checkout-application-layer">Application Layer</h4>

| Archivo / Carpeta                                              | Propósito                                                      | Tipo de recurso        |
| -------------------------------------------------------------- | ---------------------------------------------------------------| ---------------------- |
| `internal/commandservices/PaymentCommandServiceImpl.java`     | Implementación concreta de `PaymentCommandService`            | Command Service Impl   |
| `internal/queryservices/PaymentQueryServiceImpl.java`         | Implementación concreta de `PaymentQueryService`              | Query Service Impl     |
| `internal/commandservices/DebtCommandServiceImpl.java`     | Implementación concreta de `DebtCommandService`            | Command Service Impl   |
| `internal/queryservices/DebtQueryServiceImpl.java`         | Implementación concreta de `DebtQueryService`              | Query Service Impl     |
| `internal/eventhandlers/DebtPaidEventHandler.java`   | Clase que escucha el evento DebtPaidEvent para desencadenar el registro de un pago / ingreso a la tienda  | Event Handler |
| `internal/acl/CheckoutContextFacadeImpl.java`   | Implementación concreta de la interface expuesta a otros contextos para acceder a la lógica de este  | ACL Facade  |
| `internal/outboundservices/acl/ExternalOrdersService.java`         | Adaptador para interactuar con el contexto de **Orders** |  External Service     |
| `internal/outboundservices/acl/ExternalShopService.java`         | Adaptador para interactuar con el contexto de **Shop** | External Service      | |
