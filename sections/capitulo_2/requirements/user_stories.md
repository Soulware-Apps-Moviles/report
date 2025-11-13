<div style="page-break-before: always;">

### User Stories

Dado que en el statement no fue especificado qué técnica emplear para la priorización de las historias, se optó por usar MoSCoW.

<table>
    <tbody>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US01</td>
            <td>Cliente</td>
            <td>Must have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Ver productos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero visualizar los productos que puedo comprar para organizar mi pedido lo más completo posible
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Visualizar productos de catálogo</strong><br>
                Dado que el cliente se encuentra en la sección principal<br>
                Cuando hace scroll<br>
                Entonces se muestra una lista de productos a comprar<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US02</td>
            <td>Cliente</td>
            <td>Should have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Añadir producto a favoritos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero añadir productos a favoritos para acceder a ellos rápidamente en mis próximos pedidos.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Añadir producto a favoritos desde pantalla principal</strong><br>
                Dado que el cliente se encuentra en la pantalla principal<br>
                Cuando hace tap dos veces en el producto<br>
                Entonces se añade el producto a la lista de sus favoritos<br>
                <br>
                <strong>Escenario: Añadir producto a favoritos desde carrito de compras</strong><br>
                Dado que el cliente se encuentra en el carrito de compras<br>
                Cuando selecciona favorito<br>
                Entonces se añade el producto a la lista de sus favoritos<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US03</td>
            <td>Cliente</td>
            <td>Should have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Quitar producto de favoritos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero quitar productos de favoritos para evitar comprar productos que ya no consumo
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Quitar producto de favoritos desde pantalla principal</strong><br>
                Dado que el cliente se encuentra en la pantalla principal<br>
                Cuando hace tap dos veces en el producto<br>
                Entonces se quita el producto de su lista de sus favoritos<br>
                <br>
                <strong>Escenario: Quitar producto de favoritos desde carrito de compras</strong><br>
                Dado que el cliente se encuentra en el carrito de compras<br>
                Cuando selecciona favorito<br>
                Entonces se quita el producto de la lista de sus favoritos<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US04</td>
            <td>Cliente</td>
            <td>Should have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Visualizar productos favoritos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero visualizar mis productos favoritos para añadirlos rápidamente a mi orden
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Visualizar productos favoritos</strong><br>
                Dado que el cliente se encuentra en la sección principal<br>
                Cuando hace scroll<br>
                Entonces se muestra la lista de sus productos favoritos<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US05</td>
            <td>Cliente</td>
            <td>Should have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Compras recurrentes</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero una lista de mis compras recurrentes para añadirlas rápidamente a mi orden
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Visualizar compras recurrentes</strong><br>
                Dado que el cliente se encuentra en la sección principal<br>
                Cuando hace scroll<br>
                Entonces se muestra la lista de sus compras recurrentes<br>
                <br>
                <strong>Escenario: Añadir compra recurrente al carrito de compras</strong><br>
                Dado que el cliente se encuentra en la sección principal<br>
                Cuando selecciona la compra<br>
                Entonces se añade los productos relacionados a la compra al carrito de compras<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US06</td>
            <td>Cliente</td>
            <td>Must have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Añadir producto</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero añadir productos a mi carrito de compras para solventar mis necesidades del hogar
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Añadir producto a carrito de compras</strong><br>
                Dado que el cliente se encuentra en la pantalla principal<br>
                Cuando selecciona añadir en un producto<br>
                Entonces se añade el producto al carrito de compras<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US07</td>
            <td>Cliente</td>
            <td>Must have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Quitar producto</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero quitar productos de mi carrito de compras para eliminar un producto que sin querer escogí
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Quitar producto del carrito de compras</strong><br>
                Dado que el cliente se encuentra en el carrito de compras<br>
                Cuando selecciona quitar en un producto<br>
                Entonces el producto se elimina del carrito de compras<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US08</td>
            <td>Cliente</td>
            <td>Must have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Realizar pedido</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero realizar el pedido de mi carrito de compras para que la bodega empiece a armarla
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Visualizar bodegas</strong><br>
                Dado que el cliente se encuentra en el carrito de compras<br>
                Cuando selecciona realizar pedido<br>
                Entonces se muestra las bodegas cercanas disponibles para realizar el pedido<br>
                <br>
                <strong>Escenario: Realizar pedido a bodega</strong><br>
                Dado que el cliente se encuentra en la confirmación del pedido con una bodega<br>
                Cuando selecciona pedir<br>
                Entonces el pedido se realiza<br>
                Y la bodega recibe un pedido a atender<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US09</td>
            <td>Cliente</td>
            <td>Must have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Seleccionar método de pago</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero seleccionar un método de pago para manejar correctamente el control de mis finanzas
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Visualizar métodos de pago</strong><br>
                Dado que el cliente se encuentra en la confirmación del pedido con una bodega<br>
                Cuando hace scroll<br>
                Entonces se muestra los métodos de pago disponibles<br>
                <br>
                <strong>Escenario: Visualizar métodos de pago</strong><br>
                Dado que el cliente se encuentra en la confirmación del pedido con una bodega<br>
                Y es cliente confiable de la bodega<br>
                Cuando hace scroll<br>
                Entonces se muestra los métodos de pago disponibles<br>
                Y la opción de fiado<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US10</td>
            <td>Cliente</td>
            <td>Must have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Seleccionar delivery / recojo en bodega</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero seleccionar una modalidad de recojo para tener mi pedido lo más antes posible
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Visualizar modalidad de recojo</strong><br>
                Dado que el cliente se encuentra en la confirmación del pedido con una bodega<br>
                Cuando hace scroll<br>
                Entonces se muestra las modalidades de recojo<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US11</td>
            <td>Cliente</td>
            <td>Must have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Cancelar pedido como cliente</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero cancelar mi pedido en la bodega para pedir en otra porque se demoraron mucho en atenderme
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Cancelar pedido</strong><br>
                Dado que el cliente se encuentra en la pantalla de pedido<br>
                Cuando selecciona cancelar<br>
                Entonces el pedido se cancela<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US12</td>
            <td>Tendero</td>
            <td>Must have</td>
            <td>EP02</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Visualizar pedido</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero visualizar los pedidos que llegan a la bodega para organizar correctamente mi tiempo
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Visualizar pedido</strong><br>
                Dado que el tendero se encuentra en la pantalla principal<br>
                Cuando selecciona un pedido<br>
                Entonces se muestra los detalles del pedido<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US13</td>
            <td>Tendero</td>
            <td>Must have</td>
            <td>EP02</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Aceptar pedido</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero aceptar un pedido de la bodega para realizar la venta
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Aceptar pedido</strong><br>
                Dado que el tendero se encuentra en los detalles de un pedido<br>
                Cuando selecciona aceptar<br>
                Entonces el pedido se acepta<br>
                Y cambia a estado EN PREPARACIÓN<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US14</td>
            <td>Tendero</td>
            <td>Must have</td>
            <td>EP02</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Rechazar pedido</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero rechazar un pedido de la bodega para indicar que no puedo atenderlo
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Rechazar pedido</strong><br>
                Dado que el tendero se encuentra en los detalles de un pedido<br>
                Cuando selecciona rechazar<br>
                Entonces el pedido se rechaza<br>
                <br>
                <strong>Escenario: Justificar rechazo de pedido</strong><br>
                Dado que el tendero rechazó un pedido<br>
                Y escribió un mensaje para el cliente<br>
                Cuando selecciona enviar<br>
                Entonces se envía la justificación de rechazo de pedido al cliente<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US15</td>
            <td>Tendero</td>
            <td>Must have</td>
            <td>EP02</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Marcar pedido como listo</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero marcar un pedido como listo para que mi cliente sepa que puede pasar por él o que está en camino
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Marcar pedido como listo</strong><br>
                Dado que el tendero se encuentra en los detalles de un pedido con estado EN PREPARACIÓN<br>
                Cuando selecciona pedido listo<br>
                Entonces el pedido cambia de estado a LISTO PARA RECOGER<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US16</td>
            <td>Tendero</td>
            <td>Must have</td>
            <td>EP02</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Marcar pedido como entregado</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero marcar un pedido como entregado para confirmar que entregué el producto y su cobro mediante el medio respectivo se ha efectuado
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Marcar pedido como entregado</strong><br>
                Dado que el tendero se encuentra en los detalles de un pedido con estado LISTO PARA RECOGER<br>
                Cuando selecciona entregado<br>
                Entonces el pedido cambia a estado ENTREGADO<br>
                Y suma el monto del pedido a las finanzas de la bodega<br>
                <br>
                <strong>Escenario: Marcar pedido como entregado en pedidos con método de pago fiado</strong><br>
                Dado que el tendero se encuentra en los detalles de un pedido con estado LISTO PARA RECOGER o EN CAMINO<br>
                Cuando selecciona confirmar la entrega<br>
                Entonces el pedido cambia a estado ENTREGADO<br>
                Y suma añade la venta a la lista de cobros pendientes<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US17</td>
            <td>Tendero</td>
            <td>Must have</td>
            <td>EP02</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Cancelar pedido como tendero</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero cancelar la atención de un pedido para dar a conocer que no me será posible atenderlo si ocurrió un problema en el proceso de atención
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Cancelar pedido</strong><br>
                Dado que el tendero se encuentra en la pantalla de pedido<br>
                Cuando selecciona cancelar<br>
                Entonces el pedido se cancela<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US18</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Añadir cliente a lista de clientes conFIABLES</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero añadir a un cliente a la lista de conFIABLES para permitirle fiarse mediante compras en la aplicación que me facilita su seguimiento
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Añadir con éxito un cliente a la lista de confiables mediante código único de cliente</strong><br>
                Dado que el dueño ha seleccionado añadir un cliente a la lista de conFIABLES mediante código único de cliente<br>
                Y ha ingresado un código válido<br>
                Cuando confirme su adición<br>
                Entonces se debe añadir dicho cliente a la lista de conFIABLES de la bodega<br>
                Y mostrar un mensaje de confirmación<br>
                <br>
                <strong>Escenario: Añadir fallidamente un cliente a la lista de confiables mediante código único de cliente</strong><br>
                Dado que el dueño ha seleccionado añadir un cliente a la lista de conFIABLES mediante código único de cliente<br>
                Y ha ingresado un código inválido<br>
                Cuando confirme su adición<br>
                Entonces se debe mostrar un mensaje de error<br>
                <br>
                <strong>Escenario: Añadir a cliente a la lista de confiables mediante QR</strong><br>
                Dado que el dueño se encuentra en la lista de conFIABLES mediante código QR<br>
                Y haya escaneado exitosamente el código QR<br>
                Cuando confirme su adición<br>
                Entonces se debe añadir dicho cliente a la lista de conFIABLES de la bodega<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US19</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Quitar cliente a lista de clientes conFIABLES</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero quitar a un cliente de la lista de conFIABLES para evitar que los que no son responsables se sigan fiando
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Quitar cliente de la lista de confiables</strong><br>
                Dado que el dueño se encuentra en la lista de conFIABLES<br>
                Y ha seleccionado a un cliente de la lista<br>
                Cuando elija retirarlo de la lista<br>
                Entonces dicho cliente debe ser retirado de la lista de conFIABLES<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US20</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Ajustar crédito máximo</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero determinar un monto máximo que mis clientes me pueden estar debiendo para evitar que se fíen demasiado dinero
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Límite de crédito por defecto</strong><br>
                Dado que el dueño se encuentra en la sección de reglas de fiado<br>
                Y ha ajustado el crédito máximo de fiado<br>
                Cuando confirme los cambios<br>
                Entonces se debe actualizar el monto máximo de crédito para todos los fiados<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US21</td>
            <td>Cliente</td>
            <td>Must have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Mostrar código de cliente</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero conocer cuál es mi código único de cliente para que los bodegueros puedan añadirme a su lista de conFIABLES
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Mostrar código único de cliente CuC</strong><br>
                Dado que el cliente ingresa a opciones de cuenta<br>
                Cuando seleccione código de cliente<br>
                Entonces se debe mostrar su código único de cliente<br>
                <br>
                <strong>Escenario: Mostrar código QR</strong><br>
                Dado que el cliente se encuentra en código de cliente<br>
                Cuando seleccione mostrar en formato QR<br>
                Entonces se debe mostrar el equivalente de su código único de cliente en formato QR para ser fácilmente escaneado<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US22</td>
            <td>Tendero</td>
            <td>Should have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Visualizar lista de clientes conFIABLES de bodega como tendero</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero consultar la lista de confiables de la bodega para saber a quienes se les puede fiar y cuánto crédito llevan consumiendo
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Consultar lista de conFIABLES</strong><br>
                Dado que el tendero es parte de una bodega que cuenta con conFIABLES<br>
                Cuando ingrese a la sección de conFIABLES<br>
                Entonces se debe mostrar la lista de todos los clientes que pertenezcan a la lista<br>
                <br>
                <strong>Escenario: Consultar saldo restante</strong><br>
                Dado que el tendero se encuentra en la lista de conFIABLES<br>
                Cuando seleccione a un cliente de la lista<br>
                Entonces se debe mostrar el saldo máximo que se puede seguir fiando<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US23</td>
            <td>Dueño</td>
            <td>Should have</td>
            <td>EP04</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Dashboard de ingresos según periodo de tiempo</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero visualizar información clara de los ingresos mediante la aplicación según periodo de tiempo (día, semana, mes) para poder sacar mis cuentas fácilmente
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Ganancias diarias</strong><br>
                Dado que el dueño se encuentra en el dashboard<br>
                Cuando seleccione ver ganancias del día<br>
                Entonces se deben mostrar todos los ingresos que se hayan producido a lo largo del día<br>
                <br>
                <strong>Escenario: Ganancias de la semana</strong><br>
                Dado que el dueño se encuentra en el dashboard<br>
                Cuando seleccione ver ganancias de la semana<br>
                Entonces se deben mostrar todos los ingresos que se hayan producido desde el inicio de la semana hasta la fecha actual<br>
                <br>
                <strong>Escenario: Ganancias del mes</strong><br>
                Dado que el dueño se encuentra en el dashboard<br>
                Cuando seleccione ver ganancias del mes<br>
                Entonces se deben mostrar todos los ingresos que se hayan producido desde el inicio del mes hasta la fecha actual<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US24</td>
            <td>Dueño</td>
            <td>Should have</td>
            <td>EP04</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Dashboard de ingresos según método de pago</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero filtrar los ingresos del dashboard por método de pago (efectivo, virtual o fiado) para analizar cómo se están distribuyendo mis ventas según la forma de pago
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Ingresos en efectivo</strong><br>
                Dado que el dueño se encuentra en el dashboard<br>
                Cuando seleccione el filtro por método de pago “efectivo”<br>
                Entonces se deben mostrar únicamente los ingresos provenientes de ventas pagadas en efectivo<br>
                <br>
                <strong>Escenario: Ingresos virtuales</strong><br>
                Dado que el dueño se encuentra en el dashboard<br>
                Cuando seleccione el filtro por método de pago “virtual”<br>
                Entonces se deben mostrar únicamente los ingresos provenientes de ventas pagadas con medios digitales<br>
                <br>
                <strong>Escenario: Ingresos fiados</strong><br>
                Dado que el dueño se encuentra en el dashboard<br>
                Cuando seleccione el filtro por método de pago “fiado”<br>
                Entonces se deben mostrar únicamente los pedidos registrados como fiados, diferenciando que aún no generan ingreso efectivo<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US25</td>
            <td>Dueño</td>
            <td>Should have</td>
            <td>EP04</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Dashboard de ingresos según método de despacho</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero filtrar los ingresos del dashboard por método de despacho (recojo en bodega o delivery) para entender mejor cómo se distribuyen las ventas según el canal de atención
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Ingresos por recojo en bodega</strong><br>
                Dado que el dueño se encuentra en el dashboard<br>
                Cuando seleccione el filtro por método de despacho “recojo en bodega”<br>
                Entonces se deben mostrar únicamente los ingresos provenientes de pedidos con modalidad de recojo en bodega<br>
                <br>
                <strong>Escenario: Ingresos por delivery</strong><br>
                Dado que el dueño se encuentra en el dashboard<br>
                Cuando seleccione el filtro por método de despacho “delivery”<br>
                Entonces se deben mostrar únicamente los ingresos provenientes de pedidos entregados por delivery<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US26</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP04</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Ver la lista de cobros pendientes</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero visualizar todos los fiados pendientes de cobrar para saber a quién y cuánto le debo cobrar
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Lista de cobros pendientes</strong><br>
                Dado que el dueño se encuentra en la sección de mis finanzas<br>
                Cuando acceda a la lista de cobros pendientes<br>
                Entonces se deben mostrar a modo de resumen la lista de todos los cobros pendientes incluyendo datos relevantes como el cliente, monto, fecha y hora<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US27</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP04</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Marcar fiado como cobrado</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero marcar un fiado como cobrado para actualizar el crédito de mi clientes que pagan sus deudas
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Marcar el fiado como cobrado</strong><br>
                Dado que el dueño ha seleccionado un fiado de la lista de pendientes<br>
                Cuando elija marcarlo como cobrado<br>
                Entonces se debe retirar dicho cobro de la lista de pendientes<br>
                Y se debe añadir a los ingresos de la bodega con los datos correspondientes<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US28</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP05</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Añadir producto a la bodega desde catálogo</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero añadir productos a mi inventario desde un catálogo maestro para que mis clientes sepan que lo pueden encontrar en mi bodega sin mucho esfuerzo
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Añadir producto a inventario</strong><br>
                Dado que el dueño ha seleccionado un producto del catálogo<br>
                Cuando lo añada al inventario de su bodega<br>
                Entonces se debe mostrar dicho producto como disponible para pedidos en su bodega<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US29</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP05</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Quitar producto a la bodega desde catálogo</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero eliminar productos de mi inventario para evitar que mis clientes hagan pedidos de productos que no tengo disponibles
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Quitar producto a inventario</strong><br>
                Dado que el dueño ha seleccionado un producto de su inventario<br>
                Cuando seleccione retirarlo del inventario<br>
                Entonces se debe dejar de mostrar dicho producto como disponible para pedidos en su bodega<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US30</td>
            <td>Dueño</td>
            <td>Should have</td>
            <td>EP05</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Agregar precio personalizado</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero agregar precios personalizados a los productos que ofrezco en mi bodega para que los clientes me compren más
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Añadir precio personalizado</strong><br>
                Dado que el dueño ha seleccionado un producto de su inventario<br>
                Y ha ingresado un precio personalizado para este<br>
                Cuando confirme los cambios<br>
                Entonces se debe actualizar el precio personalizado para el producto seleccionado de la bodega<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US31</td>
            <td>Dueño</td>
            <td>Should have</td>
            <td>EP05</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Quitar precio personalizado</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero regresar los precios de los productos a lo habitual para ajustar su precio si es necesario
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Quitar precio personalizado</strong><br>
                Dado que el dueño ha seleccionado un producto de su inventario<br>
                Y ha borrado el precio personalizado para este<br>
                Cuando confirme los cambios<br>
                Entonces se debe actualizar el precio personalizado al precio de referencia<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US32</td>
            <td>Cliente</td>
            <td>Must have</td>
            <td>EP06</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Login mediante providers como cliente</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero autenticarme de forma segura mediante mi cuenta de Google para acceder fácil y rápidamente a las funciones de compra
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Inicio de sesión exitoso</strong><br>
                Dado que el cliente ha elegido iniciar sesión con Google<br>
                Y los datos ingresados en el provider son válidos<br>
                Cuando inicie sesión<br>
                Entonces se carga la vista de cliente.<br>
                <br>
                <strong>Escenario: Fallo en login</strong><br>
                Dado que el cliente intenta iniciar sesión con Google<br>
                Y los datos ingresados son inválidos<br>
                Cuando inicie sesión<br>
                Entonces se muestra un mensaje de error<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US33</td>
            <td>Tendero</td>
            <td>Must have</td>
            <td>EP06</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Login mediante providers como tendero</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero autenticarme de forma segura mediante mi cuenta de Google para acceder fácil y rápidamente a las funcionalidades para trabajar en la bodega
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Inicio de sesión exitoso</strong><br>
                Dado que el tendero ha elegido iniciar sesión con Google<br>
                Y los datos ingresados en el provider son válidos<br>
                Cuando inicie sesión<br>
                Entonces se carga la vista de tendero.<br>
                <br>
                <strong>Escenario: Fallo en login</strong><br>
                Dado que el tendero intenta iniciar sesión con Google<br>
                Y los datos ingresados son inválidos<br>
                Cuando inicie sesión<br>
                Entonces se muestra un mensaje de error<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US34</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP06</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Login mediante providers como dueño</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero autenticarme de forma segura mediante mi cuenta de Google para acceder fácil y rápidamente a las funcionalidades para digitalizar mi bodega
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Inicio de sesión exitoso</strong><br>
                Dado que el dueño ha elegido iniciar sesión con Google<br>
                Y los datos ingresados en el provider son válidos<br>
                Cuando inicie sesión<br>
                Entonces se carga la vista de dueño.<br>
                <br>
                <strong>Escenario: Fallo en login</strong><br>
                Dado que el dueño intenta iniciar sesión con Google<br>
                Y los datos ingresados son inválidos<br>
                Cuando inicie sesión<br>
                Entonces se muestra un mensaje de error<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US35</td>
            <td>Dueño</td>
            <td>Should have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Administrar perfil de bodega</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño quiero administrar la información de mi bodega para que sea fácil de identificar
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Actualizar datos de la bodega</strong><br>
                Dado que el dueño está autenticado y en el perfil de su tienda<br>
                Cuando modifique información (nombre, dirección, horario)<br>
                Entonces los cambios se guardan y son visibles para clientes<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US36</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Añadir tendero</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño de bodega quiero añadir tenderos para gestionar correctamente a mis trabajadores
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Añadir con éxito un tendero a la lista de trabajadores de bodega mediante código único de usuario</strong><br>
                Dado que el dueño ha seleccionado añadir un tendero a la lista de trabajadores mediante código único de cliente<br>
                Y ha ingresado un código válido<br>
                Cuando confirme su adición<br>
                Entonces se debe añadir dicho tendero a la lista de trabajadores de la bodega<br>
                Y mostrar un mensaje de confirmación<br>
                <br>
                <strong>Escenario: Añadir fallidamente un tendero a la lista de trabajadores de bodega mediante código único de cliente</strong><br>
                Dado que el dueño ha seleccionado añadir un tendero a la lista de trabajadores mediante código único de cliente<br>
                Y ha ingresado un código inválido<br>
                Cuando confirme su adición<br>
                Entonces se debe mostrar un mensaje de error<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US37</td>
            <td>Dueño</td>
            <td>Must have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Quitar tendero</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como dueño de bodega quiero quitar tenderos para eliminar trabajadores que ya no son parte de mi bodega
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Quitar tendero de lista de trabajadores de bodega</strong><br>
                Dado que el dueño se encuentra en la lista de trabajadores de su bodega<br>
                Cuando seleccione eliminar en un trabajador<br>
                Entonces se debe eliminar al tendero de la lista de trabajadores<br>
                Y se muestra un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US38</td>
            <td>Tendero</td>
            <td>Should</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Renunciar</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero renunciar a la bodega a la que estaba asociado para evitar problemas con el dueño
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Renunciar a bodega</strong><br>
                Dado que el tendero se encuentra en los detalles de la bodega para la que trabaja<br>
                Cuando presiona renunciar<br>
                Entonces se debe eliminar al tendero de la lista de trabajadores de la bodega<br>
                Y se muestra un mensaje de confirmación<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US39</td>
            <td>Tendero</td>
            <td>Could have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Visualizar información de bodega para tendero</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como tendero quiero visualizar información de la bodega para conocer datos relevantes sobre ella
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Visualizar información de bodega</strong><br>
                Dado que el tendero se encuentra en la pantalla principal<br>
                Cuando presiona bodega<br>
                Entonces se debe mostrar la información de la bodega para la que trabaja<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>US40</td>
            <td>Cliente</td>
            <td>Could have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Feed personalizada de productos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como cliente quiero obtener recomendaciones personalizadas según mi ubicación para descubrir en qué tiendas hay los mejores precios para ciertos productos
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Escenario: Visualizar información de bodega</strong><br>
                Dado que se tiene acceso a la ubicación del cliente
                Y existen bodegas registradas con precios personalizados más bajos que el catálogo maestro
                Cuando ingrese a la sección principal de la aplicación
                Entonces deben mostrarse qué las ofertas especiales indicando a qué tienda pertenecen
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS01</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener ordenes</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita obtener todos las ordenes asociadas a un shop, customer y/o status para que los usuarios autorizados puedan visualizar y gestionar la información.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Listar ordenes exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /orders/v1 <br>
            And los query params son correctamente completados <br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe incluir las ordenes encontradas <br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS02</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Crear orden</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita crear una orden para que los clientes puedan realizar pedidos a una bodega.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Crear orden exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /orders/v1 <br>
            And el cuerpo de la solicitud contiene una lista válida de productos, usuario, bodega, metodo de pago y metodo de recojo validos<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 201 Created <br>
            And el cuerpo de la respuesta debe devolver la Orden con todos los datos y su id <br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS03</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Rechazar orden</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita rechazar orden para que las bodegas decidan si coger un pedido o no.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Rechazar orden exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /orders/v1/{id}/reject <br>
            And el path de la solicitud contiene una un id de orden válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver la Orden con todos los datos y su id <br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS04</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Aceptar orden</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita aceptar orden para que las bodegas decidan si coger un pedido o no.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Aceptar orden exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /orders/v1/{id}/accept <br>
            And el path de la solicitud contiene una un id de orden válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver la Orden con todos los datos y su id <br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS05</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Avanzar orden</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita avanzar los estados de una orden para mantener la trazabilidad de estados para la tienda y para el cliente con respecto a un pedido relacionado a ellos.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Avanzar orden exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /orders/v1/{id}/advance <br>
            And el path de la solicitud contiene una un id de orden válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver la Orden con todos los datos y su id <br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS06</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Cancelar orden</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita cancelar una orden para que las bodegas o clientes decidan si continuar con su pedido o no.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Cancelar orden exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /orders/v1/{id}/cancel <br>
            And el path de la solicitud contiene una un id de orden válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver la Orden con todos los datos y su id <br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS07</td>
            <td>Developer</td>
            <td>Should Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Añadir producto favorito</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita añadir un producto favorito a un cliente para que tenga acceso más rápido a productos que más aprecia.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Añadir producto favorito exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /favorite-products/v1 <br>
            And el body de la solicitud contiene un cliente y producto de catalogo válidos<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver el producto favorito con todos los datos y su id <br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS08</td>
            <td>Developer</td>
            <td>Should Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener productos favoritos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita devolver los productos favoritos de los clientes para que tengan acceso rápido a ellos.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Listar productos favoritos exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /favorite-products/v1/by-customer/{id} <br>
            And el path de la solicitud contiene una un id de cliente válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de productos favoritos<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS09</td>
            <td>Developer</td>
            <td>Should Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Eliminar producto favorito</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita eliminar los productos favoritos  para reflejar los cambios en las necesidades del cliente.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Solicitud de eliminación exitosa</strong> <br>
            Given un usuario envía una solicitud DELETE al endpoint /favorite-products/v1/{id} <br>
            And el path de la solicitud contiene un id de producto favorito válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe retornar el id del producto eliminado<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS10</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Agregar cliente confiable</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita vincular a un cliente con una bodega para reflejar la confianza entre ambos.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Vincular cliente a bodega exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /trusted-customer/v1 <br>
            And el body de la solicitud contiene un cliente y bodega validos<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 201 Created <br>
            And el cuerpo de la respuesta debe devolver al cliente confiable con sus datos e id<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS11</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener clientes confiables por bodega</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a las bodegas conocer sus clientes confiables para mantener actualizada su lista de confianza.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Listar clientes confiables exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /trusted-customers/v1/by-shop/{id} <br>
            And el path de la solicitud contiene una un id de bodega válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de clientes confiables<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS12</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener clientes confiables por cliente</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a los clientes conocer los perfiles de cliente confiable que tienen en cada tienda.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Listar clientes confiables exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /trusted-customers/v1/by-customer/{id} <br>
            And el path de la solicitud contiene una un id de cliente válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de clientes confiables<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS13</td>
            <td>Developer</td>
            <td>Should Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Crear lista de productos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a clientes crear una lista de productos de compra para facilitar agregar productos a su bolsita de compras.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Crear lista de productos</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /shopping-list/v1 <br>
            And el body de la solicitud contiene productos de catalogo y cliente validos<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 201 Created <br>
            And el cuerpo de la respuesta debe devolver la lista de productos<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS14</td>
            <td>Developer</td>
            <td>Should Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Eliminar lista de productos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a clientes eliminar una lista de productos de compra para reflejar sus necesidades del momento.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Eliminar lista de productos</strong> <br>
            Given un usuario envía una solicitud DELETE al endpoint /shopping-lists/v1/{id}<br>
            And el path de la solicitud tiene un shopping list valido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver el id del shopping list eliminado<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS15</td>
            <td>Developer</td>
            <td>Should Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Actualizar lista de compras</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a clientes actualizar una lista de compras para reflejar sus necesidades.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Actualizar lista de productos exitosamente</strong> <br>
            Given un usuario envía una solicitud PATCH al endpoint /shopping-list/v1/{id} <br>
            And el path contiene un id valido de shopping list y el body contiene un name no nulo o productos validos<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver la lista de productos<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS16</td>
            <td>Developer</td>
            <td>Should Have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener listas de compras</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a clientes obtener sus listas de compras para acceder a ellas de forma más rápida.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener listas de productos exitosamente</strong> <br>
            Given un usuario envía una solicitud PATCH al endpoint /shopping-list/v1/by-customer/{id} <br>
            And el path contiene un id valido de cliente<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver las listas de productos<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS17</td>
            <td>Developer</td>
            <td>Could Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Recontratar a un tendero</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a los dueños de bodegas recontratar a tenderos que ya trabajaron en su bodega para facilitar el proceso de manejo de la bodega.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Recontratar a tendero exitosamente</strong> <br>
            Given un usuario envía una solicitud PATCH al endpoint /shopkeepers/v1/rehire/{id} <br>
            And el path contiene un id valido de tendero<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver los datos del tenedero y su id<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS18</td>
            <td>Developer</td>
            <td>Could Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Despedir a un tendero</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a los dueños de bodegas despedir a tenderos para reflejar los empleados reales de la bodega en la aplicación.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Despedir a tendero exitosamente</strong> <br>
            Given un usuario envía una solicitud PATCH al endpoint /shopkeepers/v1/fire/{id} <br>
            And el path contiene un id valido de tendero<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver los datos del tenedero y su id<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS19</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener tenderos por bodega</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a los dueños de bodegas conocer a los tenderos de su tienda para reflejar el personal real de la bodega.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener tenderos de bodega exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /shopkeepers/v1/by-shop/{id} <br>
            And el path contiene un id valido de bodega<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de tenderos con su información<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS20</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener tendero por correo electronico</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita acceder a la información de un tendero para conocer sus datos personales y de contacto.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener tendero exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /shopkeepers/v1/ <br>
            And se manda un correo valido por query param<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver un tendero con su información e id<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS21</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener dueño por correo electronico</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita acceder a la información de un dueño para conocer sus datos personales y de contacto.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener dueño exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /owners/v1/ <br>
            And se manda un correo valido por query param<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver un dueño con su información e id<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS22</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP04</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener pagos por tienda</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a los dueños de bodega conocer los pagos que se han realizado a su tienda para que mantengan un control correcto sobre sus finanzas.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener pagos exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /payments/v1 <br>
            And se manda un shop correcto por el path y un cliente por query params<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de pagos realizados a la tienda<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS23</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Agregar producto a inventario de bodega</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a los dueños de bodega agregar productos de un catalogo maestro a su inventario para mantener su bodega con los productos más actualizados.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Agregar producto exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /products/v1 <br>
            And se envía al body de la solicitud un shop y producto de catalogo válidos<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver el producto con su información e id<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS24</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Actualizar producto de bodega</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita a los dueños de bodega actualizar productos de su inventario para mantener su bodega con los productos más actualizados.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Actualizar producto exitosamente</strong> <br>
            Given un usuario envía una solicitud PATCH al endpoint /products/v1 <br>
            And se envía al body de la solicitud un producto, precio y disponibilidad válidas<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver el producto actualizado con su información e id.<br> <br>
            </td>
        </tr>
                <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS25</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener productos de inventario de bodega</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita obtener productos en base a una bodega, disponibilidad y/o categoria.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener productos exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /products/v1/by-shop/{id} <br>
            And se envía en el path un id de shop válido y disponibilidad y categoría válidas en los query params<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de productos<br> <br>
            </td>
        </tr>
        </tr>
                <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS26</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener bodegas por disponibilidad de productos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita obtener bodegas en base a una lista de productos para facilitar la elección de bodegas para un cliente.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener bodegas exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /shops/v1/by-products <br>
            And se envía en el body de la solicitud una lista de ids de productos de catalogo<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de bodegas<br> <br>
            </td>
        </tr>
        </tr>
                <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS27</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Crear bodega</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita crear bodegas para que el dueño lo maneje.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Crear bodega exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /shops/v1 <br>
            And se envía en el body de la solicitud un dueño, metodos de pago, metodos de recojo válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 201 Created <br>
            And el cuerpo de la respuesta debe devolver una bodega con su información e id<br> <br>
            </td>
        </tr>
        </tr>
                <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS28</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener bodega por id</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita obtener una bodega para consultar su información.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener bodega por id exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /shops/v1/{id} <br>
            And se envía en el path una bodega válida<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una bodega con su información e id<br> <br>
            </td>
        </tr>
        </tr>
                <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS29</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener bodega por dueño</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita obtener una bodega para consultar su información.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener bodega por dueño exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /shops/v1/by-owner/{id} <br>
            And se envía en el path un dueño válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una bodega con su información e id<br> <br>
            </td>
        </tr>
        </tr>
                <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS30</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP06</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Crear perfil de usuario</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita crear un perfil de usuario para que clientes, tenderos y dueños tengan acceso a las funcionalidades de la aplicación.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Crear perfil exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /profile/v1 <br>
            And se envía en el body de la solicitud la información necesaria<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 201 Created <br>
            And el cuerpo de la respuesta debe devolver el perfil con su información e id<br> <br>
            </td>
        </tr>
        </tr>
                <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS31</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP05</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener producto de catalogo por id</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita obtener un producto de catalogo por su identificar para conocer la información relevante del producto.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener producto de catalogo exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /catalog-products/v1/{id} <br>
            And se envía en el path un producto válido<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver un producto con su información e id<br> <br>
            </td>
        </tr>
        </tr>
                <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS32</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP05</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener producto de catalogo por categoria</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita obtener un producto de catalogo por su categoria para conocer la información relevante del producto.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener producto de catalogo exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /catalog-products/v1/by-category <br>
            And se envía una categoria valida por path<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de productos con su información e id<br> <br>
            </td>
        </tr>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS33</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP05</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener todos los productos de catalogo</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita obtener todos los productos del catalogo para conocer la información relevante del producto.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener producto de catalogo exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /catalog-products/v1 <br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de productos con su información e id<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS34</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Pagar deuda</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita pagar una deuda en una bodega con respecto a un pedido para que el dueño de la bodega mantenga sus finanzas estandarizadas.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Pagar deuda exitosamente</strong> <br>
            Given un usuario envía una solicitud POST al endpoint /debts/v1/{id/paid} <br>
            And se envía una deuda válida en el path<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver la deuda con su información e id<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>TS35</td>
            <td>Developer</td>
            <td>Must Have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Obtener deudas</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como Developer, quiero implementar un endpoint que permita obtener deudas en una bodega para que el dueño pueda ordernar sus finanzas.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Scenario: Obtener deudas exitosamente</strong> <br>
            Given un usuario envía una solicitud GET al endpoint /debts/v1 <br>
            And se envía un cliente, bodega y/o estado válidos<br>
            When el servidor recibe la solicitud <br> 
            Then debe responder con un código 200 Ok <br>
            And el cuerpo de la respuesta debe devolver una lista de deudas con su información<br> <br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SWR01</td>
            <td>Visitante del segmento Bodegas</td>
            <td>Should have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Hero section - Bodegas</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como visitante del landing page del segmento bodegas quiero una vista que resuma la propuesta de valor y me dirija fácilmente a la descarga o adquisición del producto.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Acceptance Criteria</strong><br>
                * Debe mostrar un título y subtítulo que resuman la propuesta de valor para bodegas.<br>
                * Debe incluir un botón o enlace claro hacia la descarga o adquisición del producto.<br>
                * Debe mostrar una imagen o ilustración relacionada con el contexto de bodegas.<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SWR02</td>
            <td>Visitante del segmento Bodegas</td>
            <td>Should have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Funcionalidades - Bodegas</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como visitante del landing page del segmento bodegas quiero visualizar claramente las funcionalidades principales del producto orientadas a mi tipo de negocio, para comprender sus beneficios y cómo me ayuda a mejorar mi gestión.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Acceptance Criteria</strong><br>
                * Deben presentarse al menos tres funcionalidades principales relevantes para el segmento bodegas.<br>
                * Cada funcionalidad debe incluir un ícono o imagen y una breve descripción.<br>
                * Debe ser visible en la misma página sin necesidad de navegación adicional.<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SWR03</td>
            <td>Visitante del segmento Bodegas</td>
            <td>Should have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Testimonios - Bodegas</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como visitante del segmento bodegas quiero leer testimonios de otros usuarios similares a mí, para ganar confianza en la solución y validar su efectividad.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Acceptance Criteria</strong><br>
                * Debe mostrar al menos tres testimonios de usuarios del segmento bodegas.<br>
                * Cada testimonio debe incluir nombre, foto, ubicación y comentario.<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SWR05</td>
            <td>Visitante del segmento Clientes</td>
            <td>Should have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Hero section - Clientes</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como visitante del landing page del segmento clientes quiero una sección principal atractiva que comunique la propuesta de valor y me motive a descargar o usar la aplicación.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Acceptance Criteria</strong><br>
                * Debe incluir un encabezado con el mensaje principal de valor para clientes.<br>
                * Debe mostrar un botón visible que dirija a la descarga o registro.<br>
                * Debe tener una imagen o elemento gráfico que represente el uso del producto por clientes.<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SWR06</td>
            <td>Visitante del segmento Clientes</td>
            <td>Should have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Funcionalidades - Clientes</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como visitante del landing page del segmento clientes quiero visualizar las funcionalidades clave orientadas a mi experiencia de usuario, para entender cómo el producto me beneficia directamente.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Acceptance Criteria</strong><br>
                * Deben mostrarse al menos tres funcionalidades principales relevantes para clientes.<br>
                * Cada funcionalidad debe tener un ícono o imagen explicativa y un breve texto descriptivo.<br>
                * La sección debe ser fácilmente escaneable y accesible en dispositivos móviles.<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SWR07</td>
            <td>Visitante del segmento Clientes</td>
            <td>Should have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Testimonios - Clientes</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como visitante del segmento clientes quiero leer opiniones y experiencias de otros usuarios para reforzar mi confianza antes de descargar o registrarme en el producto.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Acceptance Criteria</strong><br>
                * Debe mostrar al menos tres testimonios de usuarios del segmento clientes.<br>
                * Cada testimonio debe incluir nombre, foto, ubicación y comentario.<br>
                * Los testimonios deben presentarse en un formato atractivo, con opción de carrusel o scroll horizontal.<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SWR09</td>
            <td>Visitante</td>
            <td>Could have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Internacionalización</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como visitante del sitio web quiero poder cambiar el idioma entre español e inglés, para comprender la información de manera adecuada según mi preferencia lingüística.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Acceptance Criteria</strong><br>
                * Debe existir un selector visible para elegir entre español e inglés.<br>
                * Todo el contenido del sitio debe traducirse correctamente al idioma seleccionado.<br>
                * El idioma seleccionado debe mantenerse al navegar entre secciones del sitio.<br>
                * El idioma seleccionado debe ser capaz de afectar a las rutas visibles para el usuario para proporcionar una experiencia de navegación más intuitiva a usuarios no nativos digitales.
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SWR10</td>
            <td>Visitante</td>
            <td>Could have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Privacy Policy</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como visitante del sitio web quiero poder acceder y leer la política de privacidad de T’Compro, para entender cómo se recopila, utiliza y protege mi información personal mientras utilizo la aplicación y sus servicios.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Acceptance Criteria</strong><br>
                * El visitante debe poder acceder a la sección de Privacy Policy desde el menú principal y/o pie de página.<br>
                * La política debe mostrar claramente la información sobre:<br>
                * Información recopilada (datos básicos de usuario, historial de pedidos, preferencias).<br>
                * Uso de la información.<br>
                * Retención de datos y procedimiento para solicitud de eliminación.<br>
                * Compartición de información y servicios externos usados.<br>
                * Medidas de seguridad implementadas.<br>
                * Contacto para dudas o comentarios.<br>
                * La política debe mostrar la fecha de última actualización.<br>
                * Todo el contenido debe ser legible y accesible en dispositivos móviles y escritorio.
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SWR11</td>
            <td>Visitante</td>
            <td>Could have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Términos y Condiciones de Uso</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como visitante del sitio web quiero poder acceder y leer los términos y condiciones de uso de T’Compro, para entender mis responsabilidades, derechos y limitaciones al utilizar la aplicación, especialmente considerando que está en fase MVP.
            </td>
        </tr>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
                <strong>Acceptance Criteria</strong><br>
                * El visitante debe poder acceder a la sección de Términos y Condiciones desde el menú principal y/o pie de página.<br>
                * La sección debe mostrar claramente la información sobre:<br>
                * Uso de la app y prohibición de compartir credenciales.<br>
                * Registro y seguridad de la cuenta del usuario.<br>
                * Propiedad de los contenidos dentro de la app y restricciones de reproducción.<br>
                * Limitación de responsabilidad de T’Compro y advertencia sobre errores o interrupciones.<br>
                * Procedimiento de contacto para consultas (support@tcompro.app).<br>
                * Cambios en los términos y fecha de última actualización.<br>
                * Todo el contenido debe ser legible y accesible en dispositivos móviles y escritorio.<br>
                * Debe incluir una indicación visible de que la app se encuentra en fase MVP.
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SS01</td>
            <td>Equipo de desarrollo</td>
            <td>Must have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Lectura de QR</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como equipo de desarrollo quiero investigar acerca del funcionamiento de códigos QR para poder integrar funcionalidades en base a estos en la aplicación móvil
            </td>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Escenario: Revisar documentación de códigos QR</strong><br>
            Dado que el equipo necesita entender cómo funcionan los códigos QR y qué bibliotecas existen<br>
            Cuando el desarrollador revisa documentación oficial y repositorios<br>
            Entonces documenta las bibliotecas más adecuadas, sus características, compatibilidad con Android/iOS y limitaciones en un informe<br>
            <br>
            <strong>Escenario: Evaluar generación de códigos QR</strong><br>
            Dado que se necesita generar códigos QR dentro de la aplicación móvil<br>
            Cuando el desarrollador prueba la generación de códigos QR en Kotlin Multiplatform Mobile (KMM)<br>
            Entonces documenta los requisitos, posibles formatos, niveles de corrección de errores y ejemplos de integración en el informe<br>
            <br>
            <strong>Escenario: Evaluar lectura de códigos QR</strong><br>
            Dado que la aplicación debe poder escanear códigos QR de manera confiable<br>
            Cuando el desarrollador prueba la lectura de códigos QR en KMM, incluyendo Android e iOS<br>
            Entonces documenta bibliotecas efectivas, requerimientos de cámara, desempeño en distintas condiciones y posibles errores de decodificación en el informe<br>
            <br>
            <strong>Escenario: Evaluar compatibilidad con UI/UX móvil</strong><br>
            Dado que la funcionalidad QR requiere interacción del usuario<br>
            Cuando el desarrollador analiza la integración de UI (scanner en pantalla completa, animaciones, feedback)<br>
            Entonces documenta mejores prácticas de UI/UX y posibles limitaciones de diseño por plataforma en el informe<br>
            <br>
            <strong>Escenario: Prototipar funcionalidad QR</strong><br>
            Dado la necesidad de validar la viabilidad de integración de QR<br>
            Cuando el desarrollador construye un PoC mínimo (generar y escanear un QR dentro de la app KMM con comunicación interna de datos)<br>
            Entonces el PoC funciona en Android e iOS, está registrado en una rama del repositorio y referenciado en el informe<br>
            <br>
            <strong>Escenario: Estimar esfuerzo de implementación</strong><br>
            Dado que el equipo necesita planificar la integración de QR<br>
            Cuando el desarrollador desglosa la integración en tareas para UI, generación de QR, lectura de QR y seguridad<br>
            Entonces proporciona una estimación aproximada de puntos de historia y esfuerzo por plataforma en el informe<br>
            <br>
            <strong>Escenario: Documentar y compartir hallazgos</strong><br>
            Dado que el Spike está completo<br>
            Cuando el desarrollador compila todos los hallazgos en un informe compartido<br>
            Entonces el informe incluye pros/contras de bibliotecas, enfoque recomendado, limitaciones, riesgos y estimaciones, y es revisado en reunión de equipo<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SS02</td>
            <td>Equipo de desarrollo</td>
            <td>Must have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Lectura de QR</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como equipo de desarrollo quiero investigar acerca de bibliotecas para generación de gráficos en Kotlin para implementar funciones que utilicen gráficos para mostrar datos estadísticos
            </td>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Escenario: Revisar documentación de bibliotecas de gráficos</strong><br>
            Dado que el equipo necesita conocer las opciones disponibles para generar gráficos en Kotlin<br>
            Cuando el desarrollador revisa documentación oficial, repositorios y ejemplos de bibliotecas<br>
            Entonces documenta las bibliotecas más adecuadas, sus características, compatibilidad con Android/iOS y limitaciones en un informe<br>
            <br>
            <strong>Escenario: Evaluar tipos de gráficos disponibles</strong><br>
            Dado que se necesitan mostrar datos estadísticos de distintas formas<br>
            Cuando el desarrollador analiza los tipos de gráficos soportados por cada biblioteca (e.g., lineales, barras, pastel, radar)<br>
            Entonces documenta qué tipos son compatibles con las necesidades de la aplicación y posibles limitaciones en el informe<br>
            <br>
            <strong>Escenario: Evaluar integración con Kotlin Multiplatform</strong><br>
            Dado que la aplicación usa Kotlin Multiplatform Mobile (KMM)<br>
            Cuando el desarrollador prueba la compatibilidad de cada biblioteca con KMM y con Android/iOS<br>
            Entonces documenta requisitos, limitaciones y adaptación necesaria para integración multiplataforma en el informe<br>
            <br>
            <strong>Escenario: Evaluar rendimiento y consumo de recursos</strong><br>
            Dado que los gráficos deben ser rápidos y no afectar la experiencia del usuario<br>
            Cuando el desarrollador analiza impacto en rendimiento, consumo de memoria y FPS en distintos dispositivos<br>
            Entonces documenta hallazgos y posibles optimizaciones en el informe<br>
            <br>
            <strong>Escenario: Prototipar generación de gráficos</strong><br>
            Dado la necesidad de validar la viabilidad de las bibliotecas seleccionadas<br>
            Cuando el desarrollador construye un PoC mínimo generando gráficos representativos de datos estadísticos en KMM<br>
            Entonces el PoC funciona en Android e iOS, está registrado en una rama del repositorio y referenciado en el informe<br>
            <br>
            <strong>Escenario: Estimar esfuerzo de implementación</strong><br>
            Dado que el equipo necesita planificar la integración de gráficos<br>
            Cuando el desarrollador desglosa la integración en tareas (generación, actualización dinámica, personalización, animaciones)<br>
            Entonces proporciona una estimación aproximada de puntos de historia y esfuerzo por plataforma en el informe<br>
            <br>
            <strong>Escenario: Documentar y compartir hallazgos</strong><br>
            Dado que el Spike está completo<br>
            Cuando el desarrollador compila todos los hallazgos en un informe compartido<br>
            Entonces el informe incluye pros/contras de cada biblioteca, enfoque recomendado, limitaciones, riesgos, estimaciones y es revisado en reunión de equipo<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SS03</td>
            <td>Equipo de desarrollo</td>
            <td>Must have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Integración con Supabase</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como equipo de desarrollo quiero investigar acerca de la integración con el servicio de autenticación mediante providers de supabase para permitir a los usuarios registrarse e iniciar sesión de esa manera
            </td>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Escenario: Revisar documentación de autenticación Supabase</strong><br>
            Dado que el equipo necesita entender cómo funciona la autenticación mediante providers en Supabase<br>
            Cuando el desarrollador revisa la documentación oficial de Supabase Auth, ejemplos y SDKs disponibles para Kotlin y Flutter<br>
            Entonces documenta las capacidades, limitaciones y requisitos de integración en un informe<br>
            <br>
            <strong>Escenario: Evaluar autenticación con distintos providers</strong><br>
            Dado que la plataforma debe permitir registro e inicio de sesión mediante distintos providers (Google, Apple)<br>
            Cuando el desarrollador prueba la configuración y flujo de autenticación de cada provider<br>
            Entonces documenta compatibilidad, pasos de integración y posibles limitaciones de cada provider en el informe<br>
            <br>
            <strong>Escenario: Evaluar integración con Kotlin Multiplatform Mobile (KMM)</strong><br>
            Dado que la aplicación móvil usa KMM<br>
            Cuando el desarrollador prueba la integración de Supabase Auth en Android e iOS usando KMM<br>
            Entonces documenta los requisitos de integración, librerías necesarias y diferencias por plataforma en el informe<br>
            <br>
            <strong>Escenario: Evaluar integración con backend</strong><br>
            Dado que el backend Spring Boot debe validar tokens y manejar sesiones<br>
            Cuando el desarrollador prueba la verificación de JWT y el manejo de usuarios autenticados con Supabase<br>
            Entonces documenta los endpoints necesarios, flujos de validación y posibles problemas en el informe<br>
            <br>
            <strong>Escenario: Identificar implicaciones de seguridad</strong><br>
            Dado que la autenticación maneja datos sensibles de usuarios<br>
            Cuando el desarrollador analiza riesgos de seguridad (e.g., token expirable, revocación de sesiones, OAuth flows)<br>
            Entonces documenta medidas de mitigación, buenas prácticas y recomendaciones de cumplimiento en el informe<br>
            <br>
            <strong>Escenario: Prototipar autenticación con providers</strong><br>
            Dado que se necesita validar la viabilidad de la integración<br>
            Cuando el desarrollador construye un PoC mínimo que permita registro e inicio de sesión mediante al menos un provider en Android, iOS y web<br>
            Entonces el PoC funciona en todas las plataformas, está registrado en una rama del repositorio y referenciado en el informe<br>
            <br>
            <strong>Escenario: Estimar esfuerzo de implementación</strong><br>
            Dado que el equipo necesita planificar la integración completa<br>
            Cuando el desarrollador desglosa tareas por plataforma (KMM, Angular, backend Spring Boot)<br>
            Entonces proporciona estimaciones aproximadas de puntos de historia y esfuerzo en el informe<br>
            <br>
            <strong>Escenario: Documentar y compartir hallazgos</strong><br>
            Dado que el Spike está completo<br>
            Cuando el desarrollador compila todos los hallazgos en un informe compartido<br>
            Entonces el informe incluye pros/contras, enfoque recomendado, limitaciones, riesgos, estimaciones y es revisado en reunión de equipo<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>SS04</td>
            <td>Equipo de desarrollo</td>
            <td>Must have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Geolocalización</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                Como equipo de desarrollo quiero investigar acerca del funcionamiento de geolocalización para utilizarlo en las funciones que la requieren
            </td>
        <tr>
            <th colspan="4">Acceptance Criteria</th>
        </tr>
        <th colspan="4">Acceptance Criteria</th>
        </tr>
        <tr>
            <td colspan="4">
            <strong>Escenario: Revisar documentación y APIs de geolocalización</strong><br>
            Dado que el equipo necesita entender las APIs disponibles en Flutter y Kotlin<br>
            Cuando el desarrollador revisa la documentación oficial, SDKs, límites de uso y ejemplos para cada plataforma<br>
            Entonces documenta en un informe las capacidades, limitaciones, costes y requisitos de integración<br>
            <br>
            <strong>Escenario: Evaluar permisos y privacidad</strong><br>
            Dado que la geolocalización implica datos sensibles<br>
            Cuando el desarrollador revisa flujos de solicitud de permisos y comportamiento de cada plataforma<br>
            Entonces documenta los requisitos de consentimiento, impactos en UX y buenas prácticas en el informe<br>
            <br>
            <strong>Escenario: Medir precisión, frecuencia y consumo energético</strong><br>
            Dado que la precisión y la frecuencia afectan la utilidad y la batería<br>
            Cuando el desarrollador realiza pruebas en Android (Kotlin) e iOS (Flutter) con distintos modos de precisión<br>
            Entonces registra métricas de precisión, latencia y consumo energético y recomienda configuraciones óptimas en el informe<br>
            <br>
            <strong>Escenario: Evaluar integración en Flutter y Kotlin</strong><br>
            Dado que se deben soportar ambas tecnologías<br>
            Cuando el desarrollador prueba librerías de geolocalización en Flutter y en Kotlin nativo<br>
            Entonces documenta diferencias de implementación, limitaciones y ejemplos mínimos de código en el informe<br>
            <br>
            <strong>Escenario: Geocodificación y mapas</strong><br>
            Dado que la aplicación necesitará convertir coordenadas en direcciones y mostrar mapas<br>
            Cuando el desarrollador evalúa paquetes y librerías compatibles con Flutter y Kotlin<br>
            Entonces documenta compatibilidad, límites y ejemplos de integración en el informe<br>
            <br>
            <strong>Escenario: Integración con backend</strong><br>
            Dado que el backend debe recibir y validar datos de ubicación<br>
            Cuando el desarrollador define endpoints y formato de datos en pruebas básicas<br>
            Entonces documenta endpoints necesarios, esquema de datos y recomendaciones de seguridad en el informe<br>
            <br>
            <strong>Escenario: Prototipar geolocalización</strong><br>
            Dado que se necesita validar la viabilidad técnica<br>
            Cuando el desarrollador construye un PoC mínimo que obtenga ubicación y muestre en un mapa tanto en Flutter como en Kotlin<br>
            Entonces el PoC funciona en ambas plataformas, está en una rama del repositorio y referenciado en el informe<br>
            <br>
            <strong>Escenario: Estimar esfuerzo de implementación</strong><br>
            Dado que el equipo necesita planificar<br>
            Cuando el desarrollador desglosa tareas de geolocalización en Flutter y Kotlin<br>
            Entonces proporciona estimaciones aproximadas de esfuerzo y riesgos en el informe<br>
            <br>
            <strong>Escenario: Documentar y compartir hallazgos</strong><br>
            Dado que el Spike está completo<br>
            Cuando el desarrollador compila hallazgos y presenta al equipo<br>
            Entonces el informe incluye pros/contras, enfoque recomendado, limitaciones, riesgos, estimaciones y se revisa en reunión de equipo<br>
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>EP01</td>
            <td>Clientes</td>
            <td>Must have</td>
            <td>EP01</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Pedidos</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                El sistema debe permitir a los clientes armar una lista de productos para realizar un pedido a cualquiera de las bodegas cercanas que puedan satisfacerlo
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>EP02</td>
            <td>Tenderos</td>
            <td>Must have</td>
            <td>EP02</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Despacho</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                El sistema debe permitir a los tenderos revisar los pedidos realizados a su tienda, permitiéndoles conocer los detalles más relevantes para atenderlos y gestionar un estado que comunique eficazmente el proceso de atención
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>EP03</td>
            <td>Dueños</td>
            <td>Must have</td>
            <td>EP03</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Fiados</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                El sistema debe permitir a los dueños gestionar reglas bajo las cuales clientes de su confianza pueden realizar pedidos fiados
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>EP04</td>
            <td>Dueños</td>
            <td>Should have</td>
            <td>EP04</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Finanzas</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                El sistema debe permitir a los dueños conocer detalles sobre las ventas realizadas mediante la aplicación, según diversos criterios útiles para la toma de decisiones
            </td>
        </tr>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>EP05</td>
            <td>Dueños</td>
            <td>Must have</td>
            <td>EP05</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Inventario</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                El sistema debe permitir a los dueños agregar fácilmente la lista de productos disponibles en su bodega
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>EP06</td>
            <td>Usuarios</td>
            <td>Must have</td>
            <td>EP06</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Autenticación</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                El sistema debe permitir a todos los usuarios autenticarse fácilmente
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>EP07</td>
            <td>Dueños</td>
            <td>Must have</td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Gestión de bodega</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                El sistema debe permitir a los dueños establecer configuraciones sobre su bodega, incluyendo la lista de personal tendero como detalles de información de la bodega
            </td>
        </tr>
        <tr>
            <th>Story ID</th>
            <th>User</th>
            <th>Priority</th>
            <th>Epic</th>
        </tr>
        <tr>
            <td>EP08</td>
            <td>Visitante</td>
            <td>Must have</td>
            <td>EP08</td>
        </tr>
        <tr>
            <th scope="row">Title</th>
            <td colspan="3">Landing page</td>
        </tr>
        <tr>
            <th colspan="4">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                T'Compro debe contar con una landing page que logre enganchar a posibles usuarios de la aplicación móvil.
            </td>
        </tr>
    </tbody>
</table>
