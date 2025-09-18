<h4 id="iam-interface-layer">Domain Layer</h4>

| Archivo / Carpeta                             | Propósito                                   | Tipo            |
| --------------------------------------------- | ------------------------------------------- | --------------- |
| `rest/controllers/AuthenticationController.java`           |        Endpoints REST de Auth      |   REST Controller    |
| `rest/resources/SignInResource.java`           |      Entrada para logearse        |   Resource (Input)    |
| `rest/resources/SignUpResource.java`           |      Entrada para añadir usuario        |    Resource (Input)   |
| `rest/resources/UserResource.java`           |      Salida para representar usuario        |    Resource (Output)   |
| `rest/resources/AuthenticatedUserResource.java`           |       Salida para representar usuario autenticado       |   Resource (Output)    |
| `rest/assemblers/AuthenticatedUserResourceFromEntityAssembler.java`           |       Convierte entidad a resource `AuthenticatedUserResource`       |    Entity → Resource Assembler   |
| `rest/assemblers/SignInCommandFromResourceAssembler.java`           |       Convierte resource a comando `SignInCommand`       |   Resource → Command Assembler    |
| `rest/assemblers/SignUpCommandFromResourceAssembler.java`           |      Convierte resource a comando `SignUpCommand`          |    Resource → Command Assembler   |
| `rest/assemblers/UserResourceFromEntityAssembler.java`           |        Convierte entidad a resource `UserResource`      |   Entity → Resource Assembler    |
| `acl/IAMContextFacade.java`           |       Interfaz de `IAMContextFacadeImpl`       |   Facade    |