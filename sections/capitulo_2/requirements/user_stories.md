### User Stories

<table>
    <thead>
        <tr>
            <th scope="col">User Story ID</th>
            <th scope="col">Título</th>
            <th scope="col">Descripción</th>
            <th scope="col">Criterios de Aceptación</th>
            <th scope="col">Epic ID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th scope="row">US01</th>
            <td>Ver productos</td>
            <td>
                Como cliente quiero visualizar los productos que puedo comprar para organizar mi pedido lo más completo posible
            </td>
            <td>
                <strong>Escenario: Visualizar productos de catálogo</strong><br>
                Dado que el cliente se encuentra en la sección principal<br>
                Cuando hace scroll<br>
                Entonces se muestra una lista de productos a comprar<br>
            </td>
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US02</th>
            <td>Añadir producto a favoritos</td>
            <td>
                Como cliente quiero añadir productos a favoritos para acceder a ellos rápidamente en mis próximos pedidos.
            </td>
            <td>
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
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US03</th>
            <td>Quitar producto de favoritos</td>
            <td>
                Como cliente quiero quitar productos de favoritos para evitar comprar productos que ya no consumo
            </td>
            <td>
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
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US04</th>
            <td>Visualizar productos favoritos</td>
            <td>
                Como cliente quiero visualizar mis productos favoritos para añadirlos rápidamente a mi orden
            </td>
            <td>
                <strong>Escenario: Visualizar productos favoritos</strong><br>
                Dado que el cliente se encuentra en la sección principal<br>
                Cuando hace scroll<br>
                Entonces se muestra la lista de sus productos favoritos<br>
            </td>
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US05</th>
            <td>Compras recurrentes</td>
            <td>
                Como cliente quiero una lista de mis compras recurrentes para añadirlas rápidamente a mi orden
            </td>
            <td>
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
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US06</th>
            <td>Añadir producto</td>
            <td>
                Como cliente quiero añadir productos a mi carrito de compras para solventar mis necesidades del hogar
            </td>
            <td>
                <strong>Escenario: Añadir producto a carrito de compras</strong><br>
                Dado que el cliente se encuentra en la pantalla principal<br>
                Cuando selecciona añadir en un producto<br>
                Entonces se añade el producto al carrito de compras<br>
            </td>
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US07</th>
            <td>Quitar producto</td>
            <td>
                Como cliente quiero quitar productos de mi carrito de compras para eliminar un producto que sin querer escogí
            </td>
            <td>
                <strong>Escenario: Quitar producto del carrito de compras</strong><br>
                Dado que el cliente se encuentra en el carrito de compras<br>
                Cuando selecciona quitar en un producto<br>
                Entonces el producto se elimina del carrito de compras<br>
            </td>
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US08</th>
            <td>Realizar pedido</td>
            <td>
                Como cliente quiero realizar el pedido de mi carrito de compras para que la bodega empiece a armarla
            </td>
            <td>
                <strong>Escenario: Visualizar bodegas</strong><br>
                Dado que el cliente se encuentra en el carrito de compras<br>
                Cuando selecciona realizar pedido<br>
                Entonces se muestra las bodegas disponibles para realizar el pedido<br>
                <br>
                <strong>Escenario: Realizar pedido a bodega</strong><br>
                Dado que el cliente se encuentra en la confirmación del pedido con una bodega<br>
                Cuando selecciona pedir<br>
                Entonces el pedido se realiza<br>
                Y la bodega recibe un pedido a atender<br>
            </td>
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US09</th>
            <td>Seleccionar método de pago</td>
            <td>
                Como cliente quiero seleccionar un método de pago para manejar correctamente el control de mis finanzas
            </td>
            <td>
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
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US10</th>
            <td>Seleccionar delivery / recojo en bodega</td>
            <td>
                Como cliente quiero seleccionar una modalidad de recojo para tener mi pedido lo más antes posible
            </td>
            <td>
                <strong>Escenario: Visualizar modalidad de recojo</strong><br>
                Dado que el cliente se encuentra en la confirmación del pedido con una bodega<br>
                Cuando hace scroll<br>
                Entonces se muestra las modalidades de recojo<br>
            </td>
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US11</th>
            <td>Cancelar pedido como cliente</td>
            <td>
                Como cliente quiero cancelar mi pedido en la bodega para pedir en otra porque se demoraron mucho en atenderme
            </td>
            <td>
                <strong>Escenario: Cancelar pedido</strong><br>
                Dado que el cliente se encuentra en la pantalla de pedido<br>
                Cuando selecciona cancelar<br>
                Entonces el pedido se cancela<br>
            </td>
            <td>EP01</td>
        </tr>
        <tr> 
            <th scope="row">US12</th>
            <td>Visualizar pedido</td>
            <td>
                Como tendero quiero visualizar los pedidos que llegan a la bodega para organizar correctamente mi tiempo
            </td>
            <td>
                <strong>Escenario: Visualizar pedido</strong><br>
                Dado que el tendero se encuentra en la pantalla principal<br>
                Cuando selecciona un pedido<br>
                Entonces se muestra los detalles del pedido<br>
            </td>
            <td>EP02</td>
        </tr>
        <tr> 
            <th scope="row">US13</th>
            <td>Aceptar pedido</td>
            <td>
                Como tendero quiero aceptar un pedido de la bodega para realizar la venta
            </td>
            <td>
                <strong>Escenario: Aceptar pedido</strong><br>
                Dado que el tendero se encuentra en los detalles de un pedido<br>
                Cuando selecciona aceptar<br>
                Entonces el pedido se acepta<br>
                Y cambia a estado EN PREPARACIÓN<br>
            </td>
            <td>EP02</td>
        </tr>
        <tr> 
            <th scope="row">US14</th>
            <td>Rechazar pedido</td>
            <td>
                Como tendero quiero rechazar un pedido de la bodega para indicar que no puedo atenderlo
            </td>
            <td>
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
            <td>EP02</td>
        </tr>
        <tr> 
            <th scope="row">US15</th>
            <td>Marcar pedido como listo</td>
            <td>
                Como tendero quiero marcar un pedido como listo para que mi cliente sepa que puede pasar por él o que está en camino
            </td>
            <td>
                <strong>Escenario: Marcar pedido como listo</strong><br>
                Dado que el tendero se encuentra en los detalles de un pedido con estado EN PREPARACIÓN<br>
                Cuando selecciona pedido listo<br>
                Entonces el pedido cambia de estado a LISTO PARA RECOGER<br>
            </td>
            <td>EP02</td>
        </tr>
        <tr> 
            <th scope="row">US16</th>
            <td>Marcar pedido como entregado</td>
            <td>
                Como tendero quiero marcar un pedido como entregado para confirmar que entregué el producto y su cobro mediante el medio respectivo se ha efectuado
            </td>
            <td>
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
            <td>EP02</td>
        </tr>
        <tr> 
            <th scope="row">US17</th>
            <td>Cancelar pedido como tendero</td>
            <td>
                Como tendero quiero cancelar la atención de un pedido para dar a conocer que no me será posible atenderlo si ocurrió un problema en el proceso de atención
            </td>
            <td>
                <strong>Escenario: Cancelar pedido</strong><br>
                Dado que el tendero se encuentra en la pantalla de pedido<br>
                Cuando selecciona cancelar<br>
                Entonces el pedido se cancela<br>
            </td>
            <td>EP02</td>
        </tr>
        <tr> 
            <th scope="row">US18</th>
            <td>Añadir cliente a lista de clientes conFIABLES</td>
            <td>
                Como dueño quiero añadir a un cliente a la lista de conFIABLES para permitirle fiarse mediante compras en la aplicación que me facilita su seguimiento
            </td>
            <td>
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
            <td>EP03</td>
        </tr>
        <tr> 
            <th scope="row">US19</th>
            <td>Quitar cliente a lista de clientes conFIABLES</td>
            <td>
                Como dueño quiero quitar a un cliente de la lista de conFIABLES para evitar que los que no son responsables se sigan fiando
            </td>
            <td>
                <strong>Escenario: Quitar cliente de la lista de confiables</strong><br>
                Dado que el dueño se encuentra en la lista de conFIABLES<br>
                Y ha seleccionado a un cliente de la lista<br>
                Cuando elija retirarlo de la lista<br>
                Entonces dicho cliente debe ser retirado de la lista de conFIABLES<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
            <td>EP03</td>
        </tr>
        <tr> 
            <th scope="row">US20</th>
            <td>Ajustar crédito máximo</td>
            <td>
                Como dueño quiero determinar un monto máximo que mis clientes me pueden estar debiendo para evitar que se fíen demasiado dinero
            </td>
            <td>
                <strong>Escenario: Límite de crédito por defecto</strong><br>
                Dado que el dueño se encuentra en la sección de reglas de fiado<br>
                Y ha ajustado el crédito máximo de fiado<br>
                Cuando confirme los cambios<br>
                Entonces se debe actualizar el monto máximo de crédito para todos los fiados<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
            <td>EP03</td>
        </tr>
        <tr> 
            <th scope="row">US21</th>
            <td>Mostrar código de cliente</td>
            <td>
                Como cliente quiero conocer cuál es mi código único de cliente para que los bodegueros puedan añadirme a su lista de conFIABLES
            </td>
            <td>
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
            <td>EP03</td>
        </tr>
        <tr> 
            <th scope="row">US22</th>
            <td>Visualizar lista de clientes conFIABLES de bodega como tendero</td>
            <td>
                Como tendero quiero consultar la lista de confiables de la bodega para saber a quienes se les puede fiar y cuánto crédito llevan consumiendo
            </td>
            <td>
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
            <td>EP03</td>
        </tr>
        <tr> 
            <th scope="row">US23</th>
            <td>Dashboard de ingresos según periodo de tiempo</td>
            <td>
                Como dueño quiero visualizar información clara de los ingresos mediante la aplicación según periodo de tiempo (día, semana, mes) para poder sacar mis cuentas fácilmente
            </td>
            <td>
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
            <td>EP04</td>
        </tr>
        <tr> 
            <th scope="row">US24</th>
            <td>Dashboard de ingresos según periodo de tiempo</td>
            <td>
                Como dueño quiero filtrar los ingresos del dashboard por método de pago (efectivo, virtual o fiado) para analizar cómo se están distribuyendo mis ventas según la forma de pago
            </td>
            <td>
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
            <td>EP04</td>
        </tr>
        <tr> 
            <th scope="row">US25</th>
            <td>Dashboard de ingresos según periodo de tiempo</td>
            <td>
                Como dueño quiero filtrar los ingresos del dashboard por método de despacho (recojo en bodega o delivery) para entender mejor cómo se distribuyen las ventas según el canal de atención
            </td>
            <td>
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
            <td>EP04</td>
        </tr>
        <tr> 
            <th scope="row">US26</th>
            <td>Ver la lista de cobros pendientes</td>
            <td>
                Como dueño quiero visualizar todos los fiados pendientes de cobrar para saber a quién y cuánto le debo cobrar
            </td>
            <td>
                <strong>Escenario: Lista de cobros pendientes</strong><br>
                Dado que el dueño se encuentra en la sección de mis finanzas<br>
                Cuando acceda a la lista de cobros pendientes<br>
                Entonces se deben mostrar a modo de resumen la lista de todos los cobros pendientes incluyendo datos relevantes como el cliente, monto, fecha y hora<br>
            </td>
            <td>EP04</td>
        </tr>
        <tr> 
            <th scope="row">US27</th>
            <td>Marcar fiado como cobrado</td>
            <td>
                Como dueño quiero marcar un fiado como cobrado para actualizar el crédito de mi clientes que pagan sus deudas
            </td>
            <td>
                <strong>Escenario: Marcar el fiado como cobrado</strong><br>
                Dado que el dueño ha seleccionado un fiado de la lista de pendientes<br>
                Cuando elija marcarlo como cobrado<br>
                Entonces se debe retirar dicho cobro de la lista de pendientes<br>
                Y se debe añadir a los ingresos de la bodega con los datos correspondientes<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
            <td>EP04</td>
        </tr>
        <tr> 
            <th scope="row">US28</th>
            <td>Añadir producto a la bodega desde catálogo</td>
            <td>
                Como dueño quiero añadir productos a mi inventario desde un catálogo maestro para que mis clientes sepan que lo pueden encontrar en mi bodega sin mucho esfuerzo
            </td>
            <td>
                <strong>Escenario: Añadir producto a inventario</strong><br>
                Dado que el dueño ha seleccionado un producto del catálogo<br>
                Cuando lo añada al inventario de su bodega<br>
                Entonces se debe mostrar dicho producto como disponible para pedidos en su bodega<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
            <td>EP05</td>
        </tr>
        <tr> 
            <th scope="row">US29</th>
            <td>Quitar producto a la bodega desde catálogo</td>
            <td>
                Como dueño quiero eliminar productos de mi inventario para evitar que mis clientes hagan pedidos de productos que no tengo disponibles
            </td>
            <td>
                <strong>Escenario: Quitar producto a inventario</strong><br>
                Dado que el dueño ha seleccionado un producto de su inventario<br>
                Cuando seleccione retirarlo del inventario<br>
                Entonces se debe dejar de mostrar dicho producto como disponible para pedidos en su bodega<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
            <td>EP05</td>
        </tr>
        <tr> 
            <th scope="row">US30</th>
            <td>Agregar precio personalizado</td>
            <td>
                Como dueño quiero agregar precios personalizados a los productos que ofrezco en mi bodega para que los clientes me compren más
            </td>
            <td>
                <strong>Escenario: Añadir precio personalizado</strong><br>
                Dado que el dueño ha seleccionado un producto de su inventario<br>
                Y ha ingresado un precio personalizado para este<br>
                Cuando confirme los cambios<br>
                Entonces se debe actualizar el precio personalizado para el producto seleccionado de la bodega<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
            <td>EP05</td>
        </tr>
        <tr> 
            <th scope="row">US31</th>
            <td>Quitar precio personalizado</td>
            <td>
                Como dueño quiero regresar los precios de los productos a lo habitual para ajustar su precio si es necesario
            </td>
            <td>
                <strong>Escenario: Quitar precio personalizado</strong><br>
                Dado que el dueño ha seleccionado un producto de su inventario<br>
                Y ha borrado el precio personalizado para este<br>
                Cuando confirme los cambios<br>
                Entonces se debe actualizar el precio personalizado al precio de referencia<br>
                Y mostrar un mensaje de confirmación<br>
            </td>
            <td>EP05</td>
        </tr>
        <tr> 
            <th scope="row">US32</th>
            <td>Login mediante providers como cliente</td>
            <td>
                Como cliente quiero autenticarme de forma segura mediante mi cuenta de Google para acceder fácil y rápidamente a las funciones de compra
            </td>
            <td>
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
            <td>EP06</td>
        </tr>
        <tr> 
            <th scope="row">US33</th>
            <td>Login mediante providers como tendero</td>
            <td>
                Como tendero quiero autenticarme de forma segura mediante mi cuenta de Google para acceder fácil y rápidamente a las funcionalidades para trabajar en la bodega
            </td>
            <td>
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
            <td>EP06</td>
        </tr>
        <tr> 
            <th scope="row">US34</th>
            <td>Login mediante providers como dueño</td>
            <td>
                Como dueño quiero autenticarme de forma segura mediante mi cuenta de Google para acceder fácil y rápidamente a las funcionalidades para digitalizar mi bodega
            </td>
            <td>
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
            <td>EP06</td>
        </tr>
        <tr> 
            <th scope="row">US35</th>
            <td>Administrar perfil de bodega</td>
            <td>
                Como dueño quiero administrar la información de mi bodega para que sea fácil de identificar
            </td>
            <td>
                <strong>Escenario: Actualizar datos de la bodega</strong><br>
                Dado que el dueño está autenticado y en el perfil de su tienda<br>
                Cuando modifique información (nombre, dirección, horario)<br>
                Entonces los cambios se guardan y son visibles para clientes<br>
            </td>
            <td>EP07</td>
        </tr>
       <tr> 
            <th scope="row">US36</th>
            <td>Añadir tendero</td>
            <td>
                Como dueño de bodega quiero añadir tenderos para gestionar correctamente a mis trabajadores
            </td>
            <td>
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
            <td>EP07</td>
        </tr>
        <tr> 
            <th scope="row">US37</th>
            <td>Quitar tendero</td>
            <td>
                Como dueño de bodega quiero quitar tenderos para eliminar trabajadores que ya no son parte de mi bodega
            </td>
            <td>
                <strong>Escenario: Quitar tendero de lista de trabajadores de bodega</strong><br>
                Dado que el dueño se encuentra en la lista de trabajadores de su bodega<br>
                Cuando seleccione eliminar en un trabajador<br>
                Entonces se debe eliminar al tendero de la lista de trabajadores<br>
                Y se muestra un mensaje de confirmación<br>
            </td>
            <td>EP07</td>
        </tr>
       <tr>
            <th scope="row">US38</th>
            <td>Renunciar</td>
            <td>
                Como tendero quiero renunciar a la bodega a la que estaba asociado para evitar problemas con el dueño
            </td>
            <td>
                <strong>Escenario: Renunciar a bodega</strong><br>
                Dado que el tendero se encuentra en los detalles de la bodega para la que trabaja<br>
                Cuando presiona renunciar<br>
                Entonces se debe eliminar al tendero de la lista de trabajadores de la bodega<br>
                Y se muestra un mensaje de confirmación<br>
            </td>
            <td>EP07</td>
        </tr>
        <tr> 
            <th scope="row">US39</th>
            <td>Visualizar información de bodega para tendero</td>
            <td>
                Como tendero quiero visualizar información de la bodega para conocer datos relevantes sobre ella
            </td>
            <td>
                <strong>Escenario: Visualizar información de bodega</strong><br>
                Dado que el tendero se encuentra en la pantalla principal<br>
                Cuando presiona bodega<br>
                Entonces se debe mostrar la información de la bodega para la que trabaja<br>
            </td>
            <td>EP07</td>
        </tr>
        <tr>
            <th scope="row">EP01</th>
            <td>Pedidos</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th scope="row">EP02</th>
            <td>Despacho</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th scope="row">EP03</th>
            <td>Fiados</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th scope="row">EP04</th>
            <td>Finanzas</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th scope="row">EP05</th>
            <td>Inventario</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th scope="row">EP06</th>
            <td>Autenticación</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <th scope="row">EP07</th>
            <td>Gestión de bodega</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>

