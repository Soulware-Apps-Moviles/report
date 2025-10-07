### Source Code Style Guide & Conventions

Para el desarrollo de la solución, se utlizarán los siguientes lenguajes de programación:
- TypeScript  
- Java
- Kotlin

**CONVENCIONES GENERALES**
Para todos los lenguajes de programación y marcado mencionados:
- Se aplicará el uso de nomenclaturas en inglés.
- Se nombraran variables, constantes, elementos y clases de forma explícita.
- Se usará saltos de linea vacíos para separar unidades lógicas diferentes del código.
- Se promoverá la reutilización de código.

**CONVECIONES ESPECÍFICAS**

A continuación, se describen las convenciones principales a aplicar por lenguaje:

**TypeScript:** Se adoptarán las recomendaciones del Google JavaScript Style Guide y el Google TypeScript Style Guide.
- Usar `camelCase` para variables y funciones.
- Usar `PascalCase` para clases y componentes.
- Definir constantes en `UPPER_SNAKE_CASE`.
- Evitar el uso de `var`, preferir `let` y `const`.
- Usar funciones flecha (`=>`) siempre que sea posible.
- Documentar funciones y clases con comentarios JSDoc.
- Diseñar y codificar orientados al desacoplamiento.
- Aplicar tipado estricto (para typescript).

**Java:** Seguir el Google Java Style Guide.
- Usar `camelCase` para métodos y variables.
- Usar `PascalCase` para clases e interfaces.
- Agrupar paquetes de forma coherente y ordenada (`com.empresa.proyecto.modulo`).
- Usar anotaciones correctamente (`@Override`, `@Autowired`, etc.).
- Seguir prácticas de desarrollo recomendadas por **Spring Boot** como la inyección de dependencias, uso de DTOs, controladores REST, etc.

**Kotlin:**
- Se seguirán las recomendaciones del Kotlin Coding Conventions de JetBrains y las guías - oficiales de Jetpack Compose de Google.
- Usar `camelCase` para variables y funciones, y `PascalCase` para clases y composables.
- Definir constantes en `UPPER_SNAKE_CASE` dentro de objetos o companion object.
- Preferir val sobre var para fomentar la inmutabilidad.
- Mantener las funciones `@Composable puras`, sin lógica de negocio ni efectos secundarios.
- La lógica de estado debe vivir en el `ViewModel`, no dentro de los composables.
- Usar State Hoisting: el estado se eleva al nivel más alto que lo necesite.
- Colocar modifier: Modifier = Modifier siempre al final de los parámetros de un composable.
- Evitar anidaciones profundas; extraer subcomponentes reutilizables.
- Documentar composables y clases con comentarios KDoc (/** ... */).

