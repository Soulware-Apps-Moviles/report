#### Interface Layer

| Carpeta / Archivo                                                    | Propósito                                                                 | Tipo de recurso              |
| -------------------------------------------------------------------- | ----------------------------------------------------| ---------------------------- |
| `rest/controllers/CheckoutController.java`                          | Controlador REST para exponer endpoints relacionados al agregado `Checkout`| REST Controller              |
| `rest/resources/RegisterPaymentResource.java`                        | Resource de entrada para registrar un pago (equivalente a un command) | Resource (Input)             |
| `rest/resources/RegisterCreditResource.java`                         | Resource de entrada para registrar un crédito        | Resource (Input)             |
| `rest/resources/MarkCreditAsPaidResource.java`                       | Resource de entrada para marcar crédito como pagado  | Resource (Input)             |
| `rest/resources/PaymentResource.java`                                | Resource de salida que representa un `Payment`       | Resource (Output)            |
| `rest/resources/DebtResource.java`                                   | Resource de salida que representa un `Debt`                           | Resource (Output)            |
| `rest/assemblers/RegisterPaymentCommandFromResourceAssembler.java`   | Convierte un `RegisterPaymentResource` en un `RegisterPaymentCommand` | Resource → Command Assembler |
| `rest/assemblers/RegisterCreditCommandFromResourceAssembler.java`    | Convierte un `RegisterCreditResource` en un `RegisterCreditCommand`   | Resource → Command Assembler |
| `rest/assemblers/MarkCreditAsPaidCommandFromResourceAssembler.java`  | Convierte un `MarkCreditAsPaidResource` en un `MarkCreditAsPaidCommand`  | Resource → Command Assembler |
| `rest/assemblers/PaymentResourceFromEntityAssembler.java`            | Convierte un `Payment` (entity) en `PaymentResource`                     | Entity → Resource Assembler  |
| `rest/assemblers/DebtResourceFromEntityAssembler.java`               | Convierte un `Debt` (entity) en `DebtResource`                           | Entity → Resource Assembler  |
| `acl/OrdersContextAcl.java`                                          | Interface para exponer capacidades de Checkout hacia el contexto Orders  | ACL Facade                   |
| `acl/ShopContextAcl.java`                                            | Interface para exponer capacidades de Checkout hacia el contexto Shop    | ACL Facade                   |
