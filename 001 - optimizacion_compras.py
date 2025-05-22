#######################################
# Optimizador de Compras Mercado Libre
#######################################

# Autor: Nahuel Canelo
# correo: nahuelcaneloaraya@gmail.com

########################
# IMPORTAMOS LIBRERÍA
########################

import pandas as pd
from io import StringIO
import itertools

##########################
# FUNCIONES A UTILIZAR
##########################


UMBRAL_ENVIO_GRATIS = 30000


# Crea una lista PRODUCTO VENDEDOR para luego hacer la combinatoria con itertools.product
def obtener_opciones_por_producto(df):

    productos = df['producto'].unique()
    return [df[df['producto'] == p].to_dict('records') for p in productos]


# Recibe una combinación de productos (uno por producto) y calcula el costo total
# con reglas de envío.
def calcular_costo_total(combinacion):

    df_comb = pd.DataFrame(combinacion)
    costo_productos = df_comb['precio'].sum()

    # Agrupar por vendedor
    total_por_vendedor = df_comb.groupby('vendedor')['precio'].sum()
    vendedores = df_comb['vendedor'].unique()

    # Aplicar regla de envío
    costo_envios = 0
    for v in vendedores:
        total_v = total_por_vendedor[v]
        if total_v < UMBRAL_ENVIO_GRATIS:
            envio_v = df_comb[df_comb['vendedor'] == v]['envio'].max()
            costo_envios += envio_v

    return costo_productos + costo_envios


# Creamos una función que explora todas las combinaciones y retorna la mejor.
def encontrar_mejor_combinacion(df):
    opciones = obtener_opciones_por_producto(df)

    mejor_costo = float('inf')
    mejor_comb = None

    for comb in itertools.product(*opciones):
        costo = calcular_costo_total(comb)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_comb = comb

    return pd.DataFrame(mejor_comb), mejor_costo


# -------- FUNCIÓN PRINCIPAL --------

def optimizar_compras(df):
    combinacion_optima, costo_total = encontrar_mejor_combinacion(df)

    print("\n🛒 Combinación óptima de compra:")
    print(combinacion_optima)
    print(f"\n💸 Costo total mínimo: ${costo_total:,.0f}")

    return combinacion_optima, costo_total




########################################
# CREAMOS DATA
########################################

# Estamos interesados en comprar el producto A, B y C,
# los cuales son vendidos por los vendedores X, Y, Z
# se desea encontrar aquella combinación de compra que ahorre la mayor cantidad de dinero


# Creamos la data
data = """producto,vendedor,precio,envio
A,X,15000,4000
A,Y,16000,3500
B,X,20000,4000
B,Z,18000,3000
C,Y,10000,3500
C,Z,9500,2500"""

# Convertir a DataFrame
df = pd.read_csv(StringIO(data))

# Mostrar resultado
print(df)


##################################
# EJECUTAMOS
##################################
optimizar_compras(df)