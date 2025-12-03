#### Services Documentation Evidence for Sprint Review


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
      <td><code>/shopping-list/v1</code></td>
      <td>Obtener lista de compras con query params</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        customerId = 10001
        name = "semana"
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>[
  {
    "id": 10004,
    "customerId": 10001,
    "name": "COMPRAS SEMANA CASA DE MAMÁ",
    "items": [
      {
        "id": 10010,
        "catalogProductId": 1,
        "name": "Plátano de isla 1kg",
        "description": "Fruta tropical muy consumida en Perú",
        "price": 3.5,
        "quantity": 5,
        "imageUrl": "https://wongfood.vtexassets.com/arquivos/ids/547829-1200-auto?v=637896154275230000&width=1200&height=auto&aspect=true"
      }
    ]
  },
  {
    "id": 10010,
    "customerId": 10001,
    "name": "COMPRAS SEMANALES",
    "items": [
      {
        "id": 10014,
        "catalogProductId": 8,
        "name": "Agua San Luis 625ml",
        "description": "Agua mineral sin gas",
        "price": 1.8,
        "quantity": 3,
        "imageUrl": "https://production-tailoy-repo-magento-statics.s3.amazonaws.com/imagenes/872x872/productos/i/a/g/agua-san-luis-sin-gas-625ml-5024-default-1.jpg"
      },
      {
        "id": 10016,
        "catalogProductId": 14,
        "name": "Chifles Karinto 38gr",
        "description": "Snacks de plátano frito",
        "price": 2,
        "quantity": 3,
        "imageUrl": "https://d20f60vzbd93dl.cloudfront.net/uploads/tienda_003842/tienda_003842_e306aa5a60ca265f2dceae43f8bae9dba381a484_producto_large_85.png?not-from-cache-please"
      }
    ]
  }
]</pre>
      </td>
      <td><strong>http://20.201.98.91:8080/shopping-list/v1</strong></td>
    </tr>
    <tbody>
</table>