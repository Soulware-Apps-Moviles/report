<h4 id="inventory-interface-layer">Interface Layer</h4>

| Carpeta / Archivo                                       | Propósito                                                                | Tipo de recurso              |
| ------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------- |
| `rest/controllers/ProductController.java`             | Controlador REST para exponer endpoints del agregado `Product`         | REST Controller              |
| `rest/resources/AddProductResource.java`             | Resource de entrada para crear un producto (equivalente a un command)         | Resource (Input)         |
| `rest/resources/ProductResource.java`                   | Resource de salida que representa un `Product`                                | Resource (Output)        |
| `rest/assemblers/AddProductCommandFromResourceAssembler.java` | Convierte un `AddProductResource` en un `AddProductCommand`        | Resource → Command Assembler |
| `rest/assemblers/ProductResourceFromEntityAssembler.java`        | Convierte un `Product` (entity/agregado) en `ProductResource`            | Entity → Resource Assembler  |
| `acl/InventoryContextFacade.java`                | Interface para exponer capacidades de Inventory a otros bounded contexts | ACL Facade                   |
