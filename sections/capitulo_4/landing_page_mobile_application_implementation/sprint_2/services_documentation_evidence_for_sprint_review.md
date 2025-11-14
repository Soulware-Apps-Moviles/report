<h4 id="services-documentation-evidence-for-sprint-review-2">Services Documentation Evidence for Sprint Review</h4>

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
      <td><code>/catalog-products/v1/</code></td>
      <td>Obtener productos de catalogo con query params</td>
      <td><code>GET</code></td>
      <td>
        <pre>
        category = "MEAT"
        name = "pollo"
        </pre>
      </td>
      <td>
        <strong>200 Ok</strong>
        <pre>  {
    "id": 5,
    "name": "Pollo 1kg",
    "description": "Pollo fresco sin vísceras",
    "category": "MEAT",
    "price": 12,
    "imageUrl": "https://metroio.vtexassets.com/arquivos/ids/290311-1200-auto?v=638179316343400000&width=1200&height=auto&aspect=true"
  },
  {
    "id": 68,
    "name": "Pierna de pollo 1kg",
    "description": "Corte jugoso para estofados",
    "category": "MEAT",
    "price": 11,
    "imageUrl": "https://static.wixstatic.com/media/dd6ae4_ded2bbf2d0a84c0793232a5cb546ca63~mv2.jpg/v1/fill/w_540,h_391,al_c,lg_1,q_80,enc_avif,quality_auto/dd6ae4_ded2bbf2d0a84c0793232a5cb546ca63~mv2.jpg"
  }</pre>
      </td>
      <td><strong>http://20.201.98.91:8080/catalog-products/v1/</strong></td>
    </tr>
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