"""
1. Lista de productos y precios:
Se proporciona una lista de productos disponibles en el Okidoki Market con sus precios correspondientes.
Solicitud del monto de dinero disponible:
Se solicita al usuario que ingrese el monto de dinero disponible en la JUNAEB.
Se verifica que el monto sea un número entero positivo.

2. Ciclo de compras:
Mientras haya al menos $300 en la cuenta, se muestra el saldo disponible y las opciones de compra.
Se solicita al usuario que elija un producto.
Se verifica si la elección es válida (entre 1 y 5).
Se verifica si hay suficiente dinero para comprar el producto.
Si se puede comprar el producto, se deduce el precio del saldo disponible y se informa al usuario.

3. Mensaje final:
Si el saldo es menor a $300, se informa al usuario que no puede hacer más compras y se muestra el saldo restante.
"""

# Lista de productos en Okidoki Market
listproduct = """
Lista de productos en Okidoki Market:
1. Desodorante: $300
2. Sopa para uno: $2500
3. Chocolate: $300
4. Barra de cereal: $600
5. Agua mineral grande: $1800
"""
# Opciones de compra con sus precios
optionsbuy = """
Opciones de compra:
1. Desodorante          - $300
2. Sopa para uno        - $2500
3. Chocolate            - $300
4. Barra de cereal      - $600
5. Agua mineral grande  - $1800
"""
# Precios de los productos
prices = {
    1: 300,
    2: 2500,
    3: 300,
    4: 600,
    5: 1800,
}
# Solicitar el monto de dinero disponible al usuario
while True:
    try:
        print(listproduct)
        account_balance = int(input('Introduce el monto de dinero que tienes en la JUNAEB: '))
        if account_balance < 0:
            print('Por favor ingresa un número positivo.')
        else:
            break
    except ValueError:
        print('Por favor ingrese un número entero.')

# Ciclo de compras mientras haya al menos $300 en la cuenta
while account_balance >= 300:
    print(f'Tienes ${account_balance} disponibles.')
    print(optionsbuy)
    
    # Solicitar al usuario que elija un producto
    try:
        product_choice = int(input('¿Qué producto deseas comprar? (1-5): '))
        # Verificar si la elección es válida
        if product_choice in prices:
            # Verificar si hay suficiente dinero para comprar el producto
            if account_balance >= prices[product_choice]:
                account_balance -= prices[product_choice]
                print(f'Has comprado el producto. Te quedan ${account_balance}')
            else:
                print('No tienes suficiente dinero para comprar este producto.')
        else:
            print('Opción inválida. Por favor ingrese un número entre 1 y 5.')
    except ValueError:
        print('Por favor ingrese un número entero entre 1 y 5.')
# Mensaje final si no se puede hacer más compras
if account_balance < 300:
    print('Te quedan menos de $300. No puedes hacer más compras.')
    print(f'Dinero restante: ${account_balance}')