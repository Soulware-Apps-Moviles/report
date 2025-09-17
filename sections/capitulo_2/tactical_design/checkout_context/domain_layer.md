#### Domain Layer

| Archivo / Carpeta                                         | Propósito                                                                | Tipo de recurso |
| --------------------------------------------------------- | ------------------------------------------------------------------------ | --------------- |
| `model/aggregate/Payment.java`                             | Agregado raíz que representa un pago registrado                                 | Aggregate          |
| `model/valuebjects/PaymentSource.java`                                | Value object de enumeración que indica el tipo de pago                   | Value Object          |
| `model/aggregate/Debt.java`                                | Agregado raíz que representa una deuda generada por una orden                   | Aggregate          |
| `model/valuebjects/DebtStatus.java`                                | Value object de enumeración que indica el estado de la deuda                   | Value Object          |
| `model/commands/RegisterPaymentCommand.java`              | Record con datos para registrar un pago                                   | Command         |
| `model/commands/RegisterCreditCommand.java`               | Record con datos para registrar un deuda de fiado                                | Command         |
| `model/commands/MarkCreditAsPaidCommand.java`             | Record con datos para marcar un deuda de fiado como pagado                       | Command         |
| `model/queries/GetPendingDebtsQuery.java`                 | Record con datos para consultar deudas pendientes                         | Query           |
| `model/queries/GetIncomesQuery.java`                      | Record con datos para consultar ingresos (pagos registrados)              | Query           |
| `model/events/DebtPaidEvent.java`                      | Evento que registra los datos de una deuda pagada              | Event  |
| `services/DebtCommandService.java`                    | Expone operaciones de escritura del agregado | Command Service |
| `services/DebtQueryService.java`                      | Expone operaciones de lectura del agregado | Query Service   |
| `services/PaymentCommandService.java`                    | Expone operaciones de escritura del agregado | Command Service |
| `services/PaymentQueryService.java`                      | Expone operaciones de lectura del agregado | Query Service   |