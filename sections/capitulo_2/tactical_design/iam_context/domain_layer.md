<h4 id="iam-domain-layer">Domain Layer</h4>

| Archivo / Carpeta                             | Propósito                                   | Tipo            |
| --------------------------------------------- | ------------------------------------------- | --------------- |
| `model/aggregates/User.java`           | Credenciales y rol del usuario              | Aggregate       |
| `model/aggregates/Profile.java`               | Datos personales                            | Aggregate       |
| `model/valueobjects/Role.java`                | Rol del usuario (enum)                      | Value Object    |
| `model/commands/SignUpCommand.java`     | Crear nuevo usuario (email, password, role) | Command         |
| `model/commands/SignInCommand.java` | Login con email/password                    | Command         |
| `model/commands/ChangePasswordCommand.java`   | Cambiar contraseña                          | Command         |
| `model/queries/GetUserByIdQuery.java`         | Consultar usuario por id                    | Query           |
| `model/queries/GetProfileByIdQuery.java`      | Consultar perfil por id                     | Query           |
| `services/UserCommandService.java`     | Operaciones de escritura sobre usuarios     | Command Service |
| `services/UserQueryService.java`       | Operaciones de lectura sobre usuarios       | Query Service   |
| `services/ProfileCommandService.java`         | Operaciones de escritura sobre perfiles     | Command Service |
| `services/ProfileQueryService.java`           | Operaciones de lectura sobre perfiles       | Query Service   |