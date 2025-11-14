<h4 id="services-documentation-evidence-for-sprint-review-1">Services Documentation Evidence for Sprint Review</h4>

Al finalizar el sprint, se ha completado con todas las funcionalidades propuestas del Backend. Se presenta a continuación una tabla informativa:

<table style="font-size: 90%; width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>Acción</th>
      <th>HTTP</th>
      <th>Ejemplo de solicitud</th>
      <th>Ejemplo de respuesta</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>/orders/v1</code></td>
      <td>Obtener ordenes con query params</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        shopId: 10001
        customerId: 10002
        status: PLACED
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 10008,
    "orderlines": [
      {
        "id": 10018,
        "name": "Alimento para perro Dog Chow 1kg",
        "description": "Nutrición completa para perros adultos",
        "price": 4.5,
        "quantity": 5,
        "catalogProductId": 15
      }
    ],
    "customerId": 10001,
    "shopId": 10002,
    "paymentMethod": "CASH",
    "pickupMethod": "DELIVERY",
    "status": "DELIVERED"
  },
  {
    "id": 10009,
    "orderlines": [
      {
        "id": 10019,
        "name": "Arena para gato",
        "description": "Arena absorbente para mascotas",
        "price": 3.8,
        "quantity": 4,
        "catalogProductId": 16
      },
      {
        "id": 10020,
        "name": "Papel higiénico Elite x4",
        "description": "Suave y resistente",
        "price": 6.5,
        "quantity": 2,
        "catalogProductId": 10
      }
    ],
    "customerId": 10001,
    "shopId": 10002,
    "paymentMethod": "CASH",
    "pickupMethod": "DELIVERY",
    "status": "DELIVERED"
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Orders/getAllOrders</strong></td>
    </tr>
    <tr>
      <td><code>/orders/v1</code></td>
      <td>Crear orden</td>
      <td><code>POST</code></td>
      <td>
        <pre>{
  "orderlines": [
    {
      "productCatalogId": 42,
      "quantity": 2
    }
  ],
  "customerId": 10002,
  "shopId": 10001,
  "paymentMethod": "CASH",
  "pickupMethod": "DELIVERY"
}</pre>
      </td>
      <td>
        <strong>201 Created</strong>
        <pre>{
  "id": 10010,
  "orderlines": [
    {
      "id": 10021,
      "name": "Costilla de res",
      "description": "Ideal para guisos",
      "price": 10,
      "quantity": 2,
      "catalogProductId": 42
    }
  ],
  "customerId": 10002,
  "shopId": 10001,
  "paymentMethod": "CASH",
  "pickupMethod": "DELIVERY",
  "status": "PLACED"
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Orders/createOrder</strong></td>
    </tr>
        <tr>
      <td><code>/orders/v1/{id}/accept</code></td>
      <td>Aceptar orden</td>
      <td><code>POST</code></td>
      <td>
        <pre>
        id = 10010
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10010,
  "orderlines": [
    {
      "id": 10021,
      "name": "Costilla de res",
      "description": "Ideal para guisos",
      "price": 10,
      "quantity": 2,
      "catalogProductId": 42
    }
  ],
  "customerId": 10002,
  "shopId": 10001,
  "paymentMethod": "CASH",
  "pickupMethod": "DELIVERY",
  "status": "ACCEPTED"
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Orders/acceptOrder</strong></td>
    </tr>
    <tr>
      <td><code>/orders/v1/{id}/reject</code></td>
      <td>Rechazar orden</td>
      <td><code>POST</code></td>
      <td>
        <pre>
        id = 10010
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10010,
  "orderlines": [
    {
      "id": 10021,
      "name": "Costilla de res",
      "description": "Ideal para guisos",
      "price": 10,
      "quantity": 2,
      "catalogProductId": 42
    }
  ],
  "customerId": 10002,
  "shopId": 10001,
  "paymentMethod": "CASH",
  "pickupMethod": "DELIVERY",
  "status": "REJECTED"
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Orders/rejectOrder</strong></td>
    </tr>
    <tr>
      <td><code>/orders/v1/{id}/cancel</code></td>
      <td>Cancelar orden</td>
      <td><code>POST</code></td>
      <td>
        <pre>
        id = 10010
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10010,
  "orderlines": [
    {
      "id": 10021,
      "name": "Costilla de res",
      "description": "Ideal para guisos",
      "price": 10,
      "quantity": 2,
      "catalogProductId": 42
    }
  ],
  "customerId": 10002,
  "shopId": 10001,
  "paymentMethod": "CASH",
  "pickupMethod": "DELIVERY",
  "status": "CANCELED"
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Orders/cancelOrder</strong></td>
    </tr>
    <tr>
      <td><code>/orders/v1/{id}/advance</code></td>
      <td>Avanzar orden</td>
      <td><code>POST</code></td>
      <td>
        <pre>
        id = 10010
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10010,
  "orderlines": [
    {
      "id": 10021,
      "name": "Costilla de res",
      "description": "Ideal para guisos",
      "price": 10,
      "quantity": 2,
      "catalogProductId": 42
    }
  ],
  "customerId": 10002,
  "shopId": 10001,
  "paymentMethod": "CASH",
  "pickupMethod": "DELIVERY",
  "status": "DELIVERED"
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Orders/advanceOrder</strong></td>
    </tr>
    <tbody>
    <tr>
      <td><code>/favorite-products/v1</code></td>
      <td>Crear producto favorito</td>
      <td><code>POST</code></td>
      <td>
        <pre>{
  "catalogProductId": 41,
  "customerId": 10001
}</pre>
      </td>
      <td>
        <strong>201 Created</strong>
        <pre>{
  "id": 10005,
  "catalogProductId": 41,
  "name": "Pechuga de pollo",
  "description": "Corte magro y versátil",
  "price": 13,
  "customerId": 10001
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Favorite%20Products/createFavoriteProduct</strong></td>
    </tr>
    <tr>
      <td><code>/favorite-products/v1/by-customer/{id}</code></td>
      <td>Obtener productos favoritos de cliente</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        id = 10001
        </pre>
      </td>
      <td>
        <strong>201 Created</strong>
        <pre>[
  {
    "id": 10000,
    "catalogProductId": 20,
    "name": "Cebolla roja",
    "description": "Base de la cocina peruana",
    "price": 2.2,
    "customerId": 10001
  },
  {
    "id": 10002,
    "catalogProductId": 21,
    "name": "Yogurt Laive fresa",
    "description": "Yogurt bebible sabor fresa",
    "price": 5.5,
    "customerId": 10001
  },
  {
    "id": 10003,
    "catalogProductId": 30,
    "name": "Aceite Primor 1L",
    "description": "Aceite vegetal para cocinar",
    "price": 4.2,
    "customerId": 10001
  },
  {
    "id": 10005,
    "catalogProductId": 41,
    "name": "Pechuga de pollo",
    "description": "Corte magro y versátil",
    "price": 13,
    "customerId": 10001
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Favorite%20Products/getAllFavoriteProductsByCustomer</strong></td>
    </tr>
        <tr>
      <td><code>/favorite-products/v1/{id}</code></td>
      <td>Eliminar producto favorito</td>
      <td><code>DELETE</code></td>
      <td>
        <pre>
        id = 10005
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>
        10005
        </pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Favorite%20Products/deleteFavoriteProduct</strong></td>
    </tr>
        <tr>
      <td><code>/trusted-customers/v1</code></td>
      <td>Crear cliente confiable</td>
      <td><code>POST</code></td>
      <td>
        <pre>{
  "customerId": 10000,
  "shopId": 10002,
  "creditLimit": 250
}</pre>
      </td>
      <td>
        <strong>201 Created</strong>
        <pre>{
  "id": 10005,
  "creditLimit": 250,
  "customerId": 10000
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Trusted%20Customers/createTrustedCustomer</strong></td>
    </tr>
    <tr>
      <td><code>/trusted-customers/v1/by-shop/{id}</code></td>
      <td>Obtener clientes confiables por bodega</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        id = 10002
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>  {
    "id": 10005,
    "creditLimit": 250,
    "customerId": 10000
  }</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Trusted%20Customers/getTrustedCustomersByShopId</strong></td>
    </tr>
<tr>
      <td><code>/trusted-customers/v1/by-customer/{id}</code></td>
      <td>Obtener clientes confiables por cliente</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        id = 10000
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 10000,
    "creditLimit": 500,
    "customerId": 10000
  },
  {
    "id": 10004,
    "creditLimit": 1000,
    "customerId": 10000
  },
  {
    "id": 10005,
    "creditLimit": 250,
    "customerId": 10000
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Trusted%20Customers/getTrustedCustomersByCustomerId</strong></td>
    </tr>
     <tr>
      <td><code>/shopping-list/v1</code></td>
      <td>Crear lista de productos</td>
      <td><code>POST</code></td>
      <td>
        <pre>{
  "customerId": 10002,
  "name": "COMPRAS DE LA CASA SEMANAL",
  "items": [
    {
      "productCatalogId": 15,
      "quantity": 2
    },
    {
      "productCatalogId": 19,
      "quantity": 1
    }
  ]
}</pre>
      </td>
      <td>
        <strong>201 Created</strong>
        <pre>{
  "id": 10003,
  "customerId": 10002,
  "name": "COMPRAS DE LA CASA SEMANAL",
  "items": [
    {
      "id": 10008,
      "catalogProductId": 15,
      "name": "Alimento para perro Dog Chow 1kg",
      "description": "Nutrición completa para perros adultos",
      "price": 4.5,
      "quantity": 2
    },
    {
      "id": 10009,
      "catalogProductId": 19,
      "name": "Tomate",
      "description": "Fresco y jugoso",
      "price": 3,
      "quantity": 1
    }
  ]
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shopping%20List/createShoppingList</strong></td>
    </tr>
         <tr>
      <td><code>/shopping-list/v1/by-customer/{id}</code></td>
      <td>Obtener lista de productos por cliente</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        id = 10002
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 10003,
    "customerId": 10002,
    "name": "COMPRAS DE LA CASA SEMANAL",
    "items": [
      {
        "id": 10008,
        "catalogProductId": 15,
        "name": "Alimento para perro Dog Chow 1kg",
        "description": "Nutrición completa para perros adultos",
        "price": 4.5,
        "quantity": 2
      },
      {
        "id": 10009,
        "catalogProductId": 19,
        "name": "Tomate",
        "description": "Fresco y jugoso",
        "price": 3,
        "quantity": 1
      }
    ]
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shopping%20List/getAllShoppingListsByCustomer</strong></td>
    </tr>
    <tr>
      <td><code>/shopping-list/v1/{id}</code></td>
      <td>Actualizar lista de compras</td>
      <td><code>PATCH</code></td>
      <td>
        <pre>{
  "name": "LISTA DE COMPRAS SEMANALES DE LA CASA"
}
id = 10003
</pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10003,
  "customerId": 10002,
  "name": "LISTA DE COMPRAS SEMANALES DE LA CASA",
  "items": [
    {
      "id": 10008,
      "catalogProductId": 15,
      "name": "Alimento para perro Dog Chow 1kg",
      "description": "Nutrición completa para perros adultos",
      "price": 4.5,
      "quantity": 2
    },
    {
      "id": 10009,
      "catalogProductId": 19,
      "name": "Tomate",
      "description": "Fresco y jugoso",
      "price": 3,
      "quantity": 1
    }
  ]
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shopping%20List/updateShoppingList</strong></td>
    </tr>
        <tr>
      <td><code>/shopping-list/v1/{id}</code></td>
      <td>Eliminar lista de compras</td>
      <td><code>DELETE</code></td>
      <td>
        <pre>
        id = 10003
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>
        10003
        </pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shopping%20List/deleteShoppingList</strong></td>
    </tr>
    <tr>
      <td><code>/shopkeepers/v1/fire/{id}</code></td>
      <td>Despedir a tendero</td>
      <td><code>PATCH</code></td>
      <td>
        <pre>
        id = 10000
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10000,
  "shopId": 10005,
  "authId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "firstName": "Camo",
  "lastName": "Sanchez",
  "email": "camo@gmail.com",
  "phone": "+51984412159",
  "isHired": false
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shopkeepers/fireShopkeeper</strong></td>
    </tr>
        <tr>
      <td><code>/shopkeepers/v1/rehire/{id}</code></td>
      <td>Recontratar a tendero</td>
      <td><code>PATCH</code></td>
      <td>
        <pre>
        id = 10000
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10000,
  "shopId": 10005,
  "authId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "firstName": "Camo",
  "lastName": "Sanchez",
  "email": "camo@gmail.com",
  "phone": "+51984412159",
  "isHired": true
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shopkeepers/rehireShopkeeper</strong></td>
    </tr>
    <tr>
      <td><code>/shopkeepers/v1</code></td>
      <td>Obtener tendero por correo electronico</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        email = camo@gmail.com
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10000,
  "shopId": 10005,
  "authId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "firstName": "Camo",
  "lastName": "Sanchez",
  "email": "camo@gmail.com",
  "phone": "+51984412159",
  "isHired": true
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shopkeepers/getShopkeeperByEmailAddress</strong></td>
    </tr>
        <tr>
      <td><code>/owners/v1</code></td>
      <td>Obtener dueño por correo electronico</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        email = garcarmel19@gmail.com
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10008,
  "authId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "firstName": "CARMELA",
  "lastName": "GARCIA",
  "email": "garcarmel19@gmail.com",
  "phone": "+51958741123"
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Owners/getOwnerByEmailAddress</strong></td>
    </tr>
            <tr>
      <td><code>/payments/v1</code></td>
      <td>Obtener pagos</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        customerId = 10001
        shopId = 10002
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 10000,
    "customerId": 10001,
    "orderId": 10008,
    "amount": 25.20,
    "paymentMethodId": 2,
    "shopId": 10002
  },
  {
    "id": 10001,
    "customerId": 10001,
    "orderId": 10020,
    "amount": 10.80,
    "paymentMethodId": 1,
    "shopId": 10002
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Payments/getPayments</strong></td>
    </tr>
    <tr>
      <td><code>/products/v1</code></td>
      <td>Crer producto en inventario</td>
      <td><code>POST</code></td>
      <td>
        <pre>{
  "shopId": 10002,
  "price": 4.20,
  "catalogProductId": 20
}</pre>
      </td>
      <td>
        <strong>201 Created</strong>
        <pre>{
  "id": 10004,
  "shopId": 10002,
  "catalogProductId": 20,
  "price": 4.2,
  "isAvailable": true
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Products/createProduct</strong></td>
    </tr>
        <tr>
      <td><code>/products/v1</code></td>
      <td>Actualizar producto en inventario</td>
      <td><code>PATCH</code></td>
      <td>
        <pre>{
  "productId": 10004,
  "price": 4.50
}</pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10004,
  "shopId": 10002,
  "catalogProductId": 20,
  "price": 4.5,
  "isAvailable": true
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Products/updateProduct</strong></td>
    </tr>
            <tr>
      <td><code>/products/v1/by-shop/{id}</code></td>
      <td>Obtener productos de bodega</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        id = 10001
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 10001,
    "shopId": 10001,
    "catalogProductId": 16,
    "price": 3.8,
    "isAvailable": true
  },
  {
    "id": 10002,
    "shopId": 10001,
    "catalogProductId": 18,
    "price": 3,
    "isAvailable": true
  },
  {
    "id": 10003,
    "shopId": 10001,
    "catalogProductId": 19,
    "price": 3.8,
    "isAvailable": true
  },
  {
    "id": 10000,
    "shopId": 10001,
    "catalogProductId": 15,
    "price": 4,
    "isAvailable": false
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Products/getProductsBy</strong></td>
    </tr>
    <tr>
      <td><code>/products/v1/by-shop/{id}</code></td>
      <td>Obtener productos de bodega</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        id = 10001
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 10001,
    "shopId": 10001,
    "catalogProductId": 16,
    "price": 3.8,
    "isAvailable": true
  },
  {
    "id": 10002,
    "shopId": 10001,
    "catalogProductId": 18,
    "price": 3,
    "isAvailable": true
  },
  {
    "id": 10003,
    "shopId": 10001,
    "catalogProductId": 19,
    "price": 3.8,
    "isAvailable": true
  },
  {
    "id": 10000,
    "shopId": 10001,
    "catalogProductId": 15,
    "price": 4,
    "isAvailable": false
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Products/getProductsBy</strong></td>
    </tr>
        <tr>
      <td><code>/shops/v1/by-products</code></td>
      <td>Obtener tiendas por lista de productos disponibles</td>
      <td><code>GET</code></td>
      <td>
        <pre>{
  "ids": [
    16,19,18
  ]
}</pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 10001,
    "ownerId": 10007,
    "paymentMethods": [
      "CASH"
    ],
    "pickupMethods": [
      "SHOP_PICK_UP"
    ],
    "maxCreditPerCustomer": 200
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shops/getShopsByProducts</strong></td>
    </tr>
            <tr>
      <td><code>/shops/v1</code></td>
      <td>Crear bodega</td>
      <td><code>POST</code></td>
      <td>
        <pre>{
  "OwnerId": 10009,
  "paymentMethods": [
    "CASH"
  ],
  "pickupMethods": [
    "DELIVERY"
  ],
  "maxCreditPerCustomer": 100
}</pre>
      </td>
      <td>
        <strong>201 CREATED</strong>
        <pre>{
  "id": 10003,
  "ownerId": 10009,
  "paymentMethods": [
    "CASH"
  ],
  "pickupMethods": [
    "DELIVERY"
  ],
  "maxCreditPerCustomer": 100
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shops/createShop</strong></td>
    </tr>
                <tr>
      <td><code>/shops/v1/{id}</code></td>
      <td>Obtener bodega</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        id = 10003
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10003,
  "ownerId": 10009,
  "paymentMethods": [
    "CASH"
  ],
  "pickupMethods": [
    "DELIVERY"
  ],
  "maxCreditPerCustomer": 100
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shops/getShopById</strong></td>
    </tr>
                    <tr>
      <td><code>/shops/v1/by-owner/{id}</code></td>
      <td>Obtener bodega por dueño</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        id = 10009
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10003,
  "ownerId": 10009,
  "paymentMethods": [
    "CASH"
  ],
  "pickupMethods": [
    "DELIVERY"
  ],
  "maxCreditPerCustomer": 100
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Shops/getShopByOwnerId</strong></td>
    </tr>
            <tr>
      <td><code>/profile/v1</code></td>
      <td>Crear perfil de usuario</td>
      <td><code>POST</code></td>
      <td>
        <pre>{
  "authId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "firstName": "Maria",
  "lastName": "Ramos",
  "email": "marramos@gmail.com",
  "phone": "+51951123201",
  "role": "SHOP_OWNER"
}</pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10009,
  "authId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "firstName": "Maria",
  "lastName": "Ramos",
  "email": "marramos@gmail.com",
  "phone": "+51951123201",
  "role": "SHOP_OWNER"
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Profile/signUp</strong></td>
    </tr>
    <tr>
      <td><code>/catalog-products/v1/{id}</code></td>
      <td>Obtener producto de catalogo</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        id = 40
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 40,
  "name": "Queso Edam",
  "description": "Queso semiduro",
  "category": "DAIRY",
  "price": 4.5
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Catalog%20Products/getCatalogProductsById</strong></td>
    </tr>
    <tr>
      <td><code>/catalog-products/v1/by-category</code></td>
      <td>Obtener producto de catalogo por categoria</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        category = PRODUCE
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 1,
    "name": "Plátano de isla",
    "description": "Fruta tropical muy consumida en Perú",
    "category": "PRODUCE",
    "price": 3.5
  },
  {
    "id": 2,
    "name": "Papa amarilla",
    "description": "Ideal para puré y guisos",
    "category": "PRODUCE",
    "price": 2.8
  },
  {
    "id": 19,
    "name": "Tomate",
    "description": "Fresco y jugoso",
    "category": "PRODUCE",
    "price": 3
  },
  {
    "id": 20,
    "name": "Cebolla roja",
    "description": "Base de la cocina peruana",
    "category": "PRODUCE",
    "price": 2.2
  },
  {
    "id": 37,
    "name": "Zanahoria",
    "description": "Verdura rica en vitamina A",
    "category": "PRODUCE",
    "price": 2.8
  },
  {
    "id": 38,
    "name": "Espinaca",
    "description": "Verdura de hoja verde",
    "category": "PRODUCE",
    "price": 3
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Catalog%20Products/getAllCatalogProductsByCategory</strong></td>
    </tr>
                            <tr>
      <td><code>/catalog-products/v1</code></td>
      <td>Obtener productos de catalogo</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 1,
    "name": "Plátano de isla",
    "description": "Fruta tropical muy consumida en Perú",
    "category": "PRODUCE",
    "price": 3.5
  },
  {
    "id": 2,
    "name": "Papa amarilla",
    "description": "Ideal para puré y guisos",
    "category": "PRODUCE",
    "price": 2.8
  },
  {
    "id": 3,
    "name": "Leche Gloria",
    "description": "Leche evaporada en lata",
    "category": "DAIRY",
    "price": 5
  },
  {
    "id": 4,
    "name": "Queso fresco",
    "description": "Queso artesanal de vaca",
    "category": "DAIRY",
    "price": 4.2
  },
  {
    "id": 5,
    "name": "Pollo entero",
    "description": "Pollo fresco sin vísceras",
    "category": "MEAT",
    "price": 12
  },
  {
    "id": 6,
    "name": "Carne molida de res",
    "description": "Ideal para hamburguesas y guisos",
    "category": "MEAT",
    "price": 8.5
  },
  {
    "id": 7,
    "name": "Inca Kola 500ml",
    "description": "Gaseosa peruana sabor única",
    "category": "BEVERAGES",
    "price": 2
  },
  {
    "id": 8,
    "name": "Agua San Luis 625ml",
    "description": "Agua mineral sin gas",
    "category": "BEVERAGES",
    "price": 1.8
  },
  {
    "id": 9,
    "name": "Detergente Bolívar 1kg",
    "description": "Para lavado de ropa",
    "category": "HOUSE",
    "price": 15
  },
  {
    "id": 10,
    "name": "Papel higiénico Elite x4",
    "description": "Suave y resistente",
    "category": "HOUSE",
    "price": 6.5
  },
  {
    "id": 11,
    "name": "Arroz Costeño 1kg",
    "description": "Grano largo y suave",
    "category": "GROCERY",
    "price": 3.2
  },
  {
    "id": 12,
    "name": "Fideos Don Vittorio 500g",
    "description": "Fideos tipo spaghetti",
    "category": "GROCERY",
    "price": 2.8
  },
  {
    "id": 13,
    "name": "Galletas Casino",
    "description": "Galletas rellenas de vainilla",
    "category": "SNACKS",
    "price": 1.5
  },
  {
    "id": 14,
    "name": "Chifles",
    "description": "Snacks de plátano frito",
    "category": "SNACKS",
    "price": 2
  },
  {
    "id": 15,
    "name": "Alimento para perro Dog Chow 1kg",
    "description": "Nutrición completa para perros adultos",
    "category": "PET",
    "price": 4.5
  },
  {
    "id": 16,
    "name": "Arena para gato",
    "description": "Arena absorbente para mascotas",
    "category": "PET",
    "price": 3.8
  },
  {
    "id": 17,
    "name": "Sal común 500g",
    "description": "Para cocina diaria",
    "category": "OTHER",
    "price": 1
  },
  {
    "id": 18,
    "name": "Vinagre blanco",
    "description": "Para cocina y limpieza",
    "category": "OTHER",
    "price": 2.5
  },
  {
    "id": 19,
    "name": "Tomate",
    "description": "Fresco y jugoso",
    "category": "PRODUCE",
    "price": 3
  },
  {
    "id": 20,
    "name": "Cebolla roja",
    "description": "Base de la cocina peruana",
    "category": "PRODUCE",
    "price": 2.2
  },
  {
    "id": 21,
    "name": "Yogurt Laive fresa",
    "description": "Yogurt bebible sabor fresa",
    "category": "DAIRY",
    "price": 5.5
  },
  {
    "id": 22,
    "name": "Mantequilla Gloria",
    "description": "Ideal para panes y repostería",
    "category": "DAIRY",
    "price": 6
  },
  {
    "id": 23,
    "name": "Chuleta de cerdo",
    "description": "Corte jugoso para parrilla",
    "category": "MEAT",
    "price": 14
  },
  {
    "id": 24,
    "name": "Filete de pescado",
    "description": "Pescado fresco sin espinas",
    "category": "MEAT",
    "price": 9
  },
  {
    "id": 25,
    "name": "Coca-Cola 500ml",
    "description": "Gaseosa clásica",
    "category": "BEVERAGES",
    "price": 2.5
  },
  {
    "id": 26,
    "name": "Jugo Cifrut 1L",
    "description": "Jugo de frutas tropicales",
    "category": "BEVERAGES",
    "price": 3
  },
  {
    "id": 27,
    "name": "Lavavajillas Sapolio",
    "description": "Para limpieza de platos",
    "category": "HOUSE",
    "price": 7
  },
  {
    "id": 28,
    "name": "Esponja multiuso",
    "description": "Para cocina y baño",
    "category": "HOUSE",
    "price": 5
  },
  {
    "id": 29,
    "name": "Lentejas 500g",
    "description": "Legumbre rica en hierro",
    "category": "GROCERY",
    "price": 3.8
  },
  {
    "id": 30,
    "name": "Aceite Primor 1L",
    "description": "Aceite vegetal para cocinar",
    "category": "GROCERY",
    "price": 4.2
  },
  {
    "id": 31,
    "name": "Chocolates Sublime",
    "description": "Chocolate con maní",
    "category": "SNACKS",
    "price": 1.8
  },
  {
    "id": 32,
    "name": "Galletas Oreo",
    "description": "Galletas rellenas de crema",
    "category": "SNACKS",
    "price": 2.2
  },
  {
    "id": 33,
    "name": "Alimento para gato Whiskas 500g",
    "description": "Nutrición para gatos adultos",
    "category": "PET",
    "price": 6.5
  },
  {
    "id": 34,
    "name": "Shampoo para perro",
    "description": "Limpieza y cuidado de mascotas",
    "category": "PET",
    "price": 4
  },
  {
    "id": 35,
    "name": "Bicarbonato de sodio",
    "description": "Usos múltiples en cocina y limpieza",
    "category": "OTHER",
    "price": 2
  },
  {
    "id": 36,
    "name": "Ajo molido",
    "description": "Condimento esencial",
    "category": "OTHER",
    "price": 3.5
  },
  {
    "id": 37,
    "name": "Zanahoria",
    "description": "Verdura rica en vitamina A",
    "category": "PRODUCE",
    "price": 2.8
  },
  {
    "id": 38,
    "name": "Espinaca",
    "description": "Verdura de hoja verde",
    "category": "PRODUCE",
    "price": 3
  },
  {
    "id": 39,
    "name": "Leche UHT Laive",
    "description": "Leche larga duración",
    "category": "DAIRY",
    "price": 5.8
  },
  {
    "id": 40,
    "name": "Queso Edam",
    "description": "Queso semiduro",
    "category": "DAIRY",
    "price": 4.5
  },
  {
    "id": 41,
    "name": "Pechuga de pollo",
    "description": "Corte magro y versátil",
    "category": "MEAT",
    "price": 13
  },
  {
    "id": 42,
    "name": "Costilla de res",
    "description": "Ideal para guisos",
    "category": "MEAT",
    "price": 10
  },
  {
    "id": 43,
    "name": "Agua Cielo 625ml",
    "description": "Agua mineral sin gas",
    "category": "BEVERAGES",
    "price": 2.2
  },
  {
    "id": 44,
    "name": "Gaseosa Pepsi 500ml",
    "description": "Gaseosa sabor cola",
    "category": "BEVERAGES",
    "price": 3.5
  },
  {
    "id": 45,
    "name": "Limpiador multiusos",
    "description": "Para pisos y superficies",
    "category": "HOUSE",
    "price": 8
  },
  {
    "id": 46,
    "name": "Toalla de cocina",
    "description": "Absorbente y reutilizable",
    "category": "HOUSE",
    "price": 6
  },
  {
    "id": 47,
    "name": "Harina Blanca Flor 1kg",
    "description": "Para repostería y panadería",
    "category": "GROCERY",
    "price": 3
  },
  {
    "id": 48,
    "name": "Azúcar rubia 1kg",
    "description": "Endulzante natural",
    "category": "GROCERY",
    "price": 2.5
  },
  {
    "id": 49,
    "name": "Chizitos",
    "description": "Snacks de maíz inflado",
    "category": "SNACKS",
    "price": 1.8
  },
  {
    "id": 50,
    "name": "Galletas Field",
    "description": "Galletas surtidas",
    "category": "SNACKS",
    "price": 2.2
  }
]</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Catalog%20Products/getAllCatalogProducts</strong></td>
    </tr>
        <tr>
      <td><code>/debts/v1/{id}/paid</code></td>
      <td>Pagar deuda</td>
      <td><code>POST</code></td>
      <td>
        <pre>
        id = 10001
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10001,
  "customerId": 10003,
  "orderId": 10008,
  "amount": 25.20,
  "shopId": 10001,
  "status": "PAID"
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Debts/markDebtAsPaid</strong></td>
    </tr>
            <tr>
      <td><code>/debts/v1</code></td>
      <td>Obtener deudas de bodega</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        customerId = 10003
        shopId = 10001
        status = PAID
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>{
  "id": 10001,
  "customerId": 10003,
  "orderId": 10008,
  "amount": 25.20,
  "shopId": 10001,
  "status": "PAID"
}</pre>
      </td>
      <td><strong>http://4.156.241.223:8080/swagger-ui/index.html#/Debts/getDebts</strong></td>
    </tr>
    <tbody>
</table>