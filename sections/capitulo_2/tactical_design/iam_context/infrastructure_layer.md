<h4 id="iam-infrastructure-layer">Domain Layer</h4>

| Archivo / Carpeta                             | Propósito                                   | Tipo            |
| --------------------------------------------- | ------------------------------------------- | --------------- |
| `authorization/sfs/configuration/WebSecurityConfiguration.java`           |       Configura filtros de seguridad y autenticación        |    Security    |
| `authorization/sfs/model/UserDetailsImpl.java`           |      Adapta a User para aplicar seguridad con Spring Security         |    Security    |
| `authorization/sfs/model/EmailPasswordAuthenticationTokenBuilder.java`           |      Constructor estatico para la creación de EmailPasswordAuthenticationToken         |   Security     |
| `authorization/sfs/pipeline/BearerAuthorizationRequestFilter.java`           |        Intercepta y procesa los requests HTTPS y valida si los deja pasar       |    Security    |
| `authorization/sfs/pipeline/UnauthorizedRequestHandlerEntryPoint.java `           |      Valida el comportamiento de los accesos no autorizados a endpoints        |    Security    |
| `authorization/sfs/services/UserDetailsServiceImpl.java`           |       Carga información del usuario para Spring Security        |    Security    |
| `authorization/bcrypt/services/HashingServiceImpl.java`           |       Se encarga del hasheo de las contraseñas y la verificación de una contraseña ingresada        |    Security    |
| `authorization/bcrypt/HashingService.java`           |       Interface de Hashin Service        |    Security    |
| `persistence/jpa/repositories/UserRepository.java`           |       Implementación JPA de `UserRepository` (agregado)        |    Repository Impl    |
| `persistence/jpa/repositories/ProfileRepository.java`           |       Implementación JPA de `ProfileRepository` (agregado)        |    Repository Impl    |
| `tokens/jwt/services/TokenServiceImpl.java`           |      Es el responsable de todas las operaciones relacionadas con JWT para los endpoints         |    Security    |
| `tokens/jwt/BearerTokenService.java`           |       Interface de TokenService        |    Security    |