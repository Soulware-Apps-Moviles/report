
#### Domain Layer

| Archivo / Carpeta                                         | Propósito                                                                | Tipo de recurso |
| --------------------------------------------------------- | ------------------------------------------------------------------------ | --------------- |
| `model/aggregate/Checkout.java`                           | Agregado raíz del contexto, maneja pagos, créditos y deudas               | Aggregate       |
| `model/entities/Payment.java`                             | Entidad que representa un pago registrado                                 | Entity          |
| `model/entities/Debt.java`                                | Entidad que representa una deuda generada por una orden                   | Entity          |
| `model/commands/RegisterPaymentCommand.java`              | Record con datos para registrar un pago                                   | Command         |
| `model/commands/RegisterCreditCommand.java`               | Record con datos para registrar un crédito                                | Command         |
| `model/commands/MarkCreditAsPaidCommand.java`             | Record con datos para marcar un crédito como pagado                       | Command         |
| `model/queries/GetPendingDebtsQuery.java`                 | Record con datos para consultar deudas pendientes                         | Query           |
| `model/queries/GetIncomesQuery.java`                      | Record con datos para consultar ingresos (pagos registrados)              | Query           |
| `services/CheckoutCommandService.java`                    | Expone operaciones de escritura del agregado (pagar, registrar deuda, etc.) | Command Service |
| `services/CheckoutQueryService.java`                      | Expone operaciones de lectura del agregado (consultar deudas/ingresos)    | Query Service   |