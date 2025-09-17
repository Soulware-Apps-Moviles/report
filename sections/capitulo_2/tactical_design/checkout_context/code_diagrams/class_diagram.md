##### Bounded Context Domain Layer Class Diagrams

El diagrama de clases de este contexto se centra principalmente en Checkout, el único aggregate de este contexto. Representa el proceso de pago de una compra, permitiendo registrar pagos, créditos y deudas asociadas.

El contexto dispone de consultas que permiten verificar las deudas pendientes y los ingresos registrados, gestionadas por el CheckoutQueryService.

<img src="../../../../../img/tactical-design/checkout/class.png" alt="Checkout class diagram">