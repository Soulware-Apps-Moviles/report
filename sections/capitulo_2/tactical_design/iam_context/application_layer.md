#### Application Layer

| Archivo / Carpeta                             | Propósito                                   | Tipo            |
| --------------------------------------------- | ------------------------------------------- | --------------- |
| `internal/commandservices/UserCommandServiceImpl.java`           |        Implementación de `UserCommandService`      |    Command Service Impl   |
| `internal/commandservices/ProfileCommandServiceImpl.java`           |      Implementación de `ProfileCommandService`        |    Command Service Impl   |
| `internal/queryservices/UserQueryServiceImpl.java`           |       Implementación de `UserQueryService`       |   Query Service Impl    |
| `internal/queryservices/ProfileQueryServiceImpl.java`           |       Implementación de `ProfileQueryService`       |   Query Service Impl    |
| `internal/outboundservices/hashing/HashingService.java`           |       Interface de Hashing Service       |   Security    |
| `internal/outboundservices/tokens/TokenService.java`           |       Interface de Token Service       |   Security    |
| `acl/IAMContextFacadeImpl.java`           |       Implementación de `IAMContextFacade`       |   Facade    |