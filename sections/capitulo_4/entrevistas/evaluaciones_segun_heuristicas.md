### Evaluaciones según heurísticas

**UX Heuristics & Principles Evaluation**

**Usability – Inclusive Design – Information Architecture**

**CARRERA:** Ingeniería de Software  
**CURSO:** CC238  
**SECCIÓN:** 1807 
**PROFESORES:** Jorge Luis Mayta Guillermo
**AUDITOR:** Carlos Guimaraes
**CLIENTE(S):** Juan Montes – Mateo Monge  

---

**SITE o APP A EVALUAR:**  
**T’Compro – Landing Page y Aplicación Móvil**

---

**TAREAS A EVALUAR**

El alcance de esta evaluación incluye la revisión de la usabilidad de las siguientes tareas:

- Visualización de la información en el landing page  
- Visualización del catálogo de productos  
- Gestión de inventario  
- Gestión de pedidos  
- Visualización de pedidos pendientes y completados  

No están incluidas en esta evaluación las siguientes tareas:

- Procesos de pago  
- Funcionalidades avanzadas de administración  
- Integración con sistemas externos (ERP, POS)  
- Comunicación por WhatsApp u otros canales externos  

---

**ESCALA DE SEVERIDAD**

| Nivel | Descripción |
|-------|-------------|
| **1** | Problema superficial, fácilmente superado y poco frecuente. |
| **2** | Problema menor, ocurre un poco más frecuentemente o genera leve fricción. |
| **3** | Problema mayor, ocurre frecuentemente o impide que algunos usuarios lo resuelvan. Requiere corrección prioritaria. |
| **4** | Problema muy grave, bloqueante. Debe resolverse antes del lanzamiento. |

---

**TABLA RESUMEN**

| # | Problema | Severidad | Heurística violada |
|---|-----------|-----------|---------------------|
| **1** | Falta de notificaciones en tiempo real para nuevos pedidos (Juan Montes) | **2** | Usability: Feedback inmediato |
| **2** | Vista de catálogo con sobrecarga visual, información densa (Mateo Monge) | **2** | Information Architecture: Is it usable? – Organización visual |

---

**DESCRIPCIÓN DE PROBLEMAS**

---

**PROBLEMA #1: Falta de notificaciones en tiempo real para nuevos pedidos**

**Usuario:** Juan Montes  
**Severidad:** 2  
**Heurística violada:** Usabilidad – *Feedback inmediato*

**Problema:**  
Durante el proceso de validación, Juan indicó que la aplicación cumple con sus tareas como tendero y que la interfaz es amigable. Sin embargo, detectó un problema importante para su trabajo diario: la aplicación no envía notificaciones cuando llega un pedido nuevo. Para visualizarlo, debe ingresar manualmente o refrescar la vista, lo cual no es práctico debido a que él debe atender presencialmente a los clientes y no puede estar revisando el teléfono constantemente.

Esto genera una falta de retroalimentación inmediata, obligando al usuario a monitorear activamente la aplicación en lugar de recibir un aviso automático.

**Recomendación:**  
Implementar un sistema de notificaciones push en tiempo real que informe al usuario cuando llegue un pedido nuevo, incluso si la aplicación está en segundo plano o cerrada. Esto reducirá fricción, permitirá una gestión más eficiente y evitará que se pierdan pedidos durante las horas de mayor flujo de clientes.

---

**PROBLEMA #2: Vista de catálogo visualmente sobrecargada**

**Usuario:** Mateo Monge  
**Severidad:** 2  
**Heurística violada:** Information Architecture – *Is it usable?*

**Problema:**  
Mateo considera que la aplicación es fácil de usar y que la separación en dos tabs por funcionalidad le parece correcta. No obstante, señaló que la vista del catálogo le parece visualmente “sobrecargada”, con demasiada información junta, lo que afecta la claridad de lectura y genera una sensación de saturación visual. Aunque no impide el uso, sí reduce la facilidad de navegación y la percepción de orden.

Este problema afecta la arquitectura de la información y puede generar confusión en usuarios menos familiarizados con apps.

**Recomendación:**  
Simplificar la vista del catálogo mediante:

- Mayor separación entre elementos  
- Jerarquías visuales más claras  
- Reducción del contenido mostrado por tarjeta (mostrar solo lo esencial)  
- Uso más consistente de colores y tamaños  
- Alternar listas compactas con vistas ampliadas  

Esto mejorará la legibilidad, reducirá carga cognitiva y hará la navegación más fluida.

