# 🛒 Optimizador de Compras Mercado Libre

Este repositorio contiene un modelo de optimización diseñado para ayudarte a **minimizar el costo total de tus compras en Mercado Libre**, considerando **precios, vendedores y políticas de envío gratuito**.

## ❓ El Problema

Cuando compras en Mercado Libre, es común encontrar lo siguiente:

- Un producto puede tener el **precio más bajo** si lo compras de forma individual a un vendedor específico.
- Sin embargo, ese mismo vendedor **cobra el costo de envío** (por ejemplo, $3.500 o $4.000).
- Si compras **otro producto** que también necesitas, de otro vendedor barato, **se vuelve a cobrar otro envío**.

💸 **¿El resultado?** Terminas pagando más por el **despacho duplicado**, aunque hayas elegido los productos más baratos uno por uno.

---

## 💡 La Oportunidad de Ahorro

Mercado Libre actualmente no cuenta con una herramienta que ayude a los usuarios a minimizar el gasto total de sus compras. Por ejemplo, si se implementara un algoritmo que, en base al carrito inicial, recomendara a qué vendedor comprarle cada producto, muchos usuarios podrían evitar pagar envíos duplicados. Esto se debe a que varios vendedores ofrecen envío gratis cuando el total de la compra supera ciertos montos, como los $30.000 CLP. Sin esa optimización, es común que los usuarios terminen pagando más, incluso cuando eligen los productos de menor precio individual.


Esto abre una oportunidad:

> A veces es **mejor pagar un poco más por el producto**, si eso significa que puedes **agrupar productos del mismo vendedor y evitar pagar el despacho**.

### 🧠 Ejemplo:

| Producto | Vendedor | Precio | Envío | Total |
|----------|----------|--------|-------|-------|
| A        | X        | $15.000| $4.000| $19.000 |
| B        | Z        | $18.000| $3.000| $21.000 |
| C        | Y        | $10.000| $3.500| $13.500 |

Total: **$53.500**

Pero si compras A y B al **mismo vendedor** (por $16.000 y $20.000) → **Total = $36.000**, y superas los $30.000 ⇒ **Envío Gratis**  
Agregando el C a Y con envío, el total es **$36.000 + $10.000 + $3.500 = $49.500**

📉 ¡Ahorraste $4.000 eligiendo vendedores distintos!

---

## ✅ Solución

Este proyecto genera **todas las combinaciones posibles de vendedores por producto** y calcula el **costo total real**, considerando:

- Precio del producto
- Envío por vendedor (si no se supera el umbral)
- Reglas de **envío gratis desde los $30.000**

Devuelve la **combinación óptima de compra** con el **menor costo final**.

En base a ello el cliente podría elegir comprarle al mismo vendedor y ahorrar mucho dinero en su compra.

Futuras adaptaciones podrían considerar el uso de modelos predictivos para hacer recomendaciones de compras que puedan llevar a ahorros futuros.

