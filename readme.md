## 1 - Ventas
* Fecha - Date
* RFC cliente - Text
* Lista
    - Producto (Categoria, Nombre) - ComboBox
    - Precio    - SpinBox Double "round(2)"
    - Cantidad  - SpinBox Int
    - Color     - Text
    - Total     - SpinBox Double Disabled "round(2)"
    - Eliminar este producto de la venta - Button
* Agregar - Button
## 2 - Compras
* Fecha - Date
* Nombre provedor - ComboBox
* Lista
    - Producto (Categoria, Nombre) - ComboBox
    - Precio    - SpinBox Double "round(2)"
    - Cantidad  - SpinBox Int
    - Total     - SpinBox Double Disabled "round(2)"
    - Eliminar este producto de la venta - Button
## 3 - Productos
* Ver
    - Categoria      - ComboBox
    - Nombre         - ComboBox
    - Precio         - SpinBox Double Disabled "round(2)"
    - Resurtible     - CheckBox Disabled
    - Ver existencia - SpinBox Int Disabled
* Agregar
    - Categoria          - Text
    - Nombre             - Text
    - Precio             - SpinBox Double "round(2)"
    - Resurtible         - CheckBox True
    - existe             - CheckBox False
    - Agregar existencia - SpinBox Int "solo si *existe esta activado*"
* Editar  
    - Categoria          - ComboBox
    - Nombre             - ComboBox
    - Precio             - SpinBox Double "round(2)"
    - Resurtible         - CheckBox 
    - existe             - CheckBox False
    - Agregar existencia - SpinBox Int "solo si *existe esta activado*"
## 4 - Provedores
* Ver
    - Nombre         - ComboBox
    - Rfc            - Text Disabled
    - Telefono       - Text Disabled
    - Direccion      - Text Disabled
    - Activo         - CheckBox Disabled
* Agregar
    - Nombre         - Text
    - Rfc            - Text
    - Telefono       - Text
    - Direccion      - Text
* Editar 
    - Nombre         - ComboBox
    - Rfc            - Text
    - Telefono       - Text
    - Direccion      - Text
    - Activo         - CheckBox
## 5 - Tickets
* Opiones de Filtro - Radio Button
    - Buscar folio - Text
    - Buscar por fecha unica- Date
    - Buscar por rango de fecha - Date
    - Limpiar - Button
* Lista de folios - Table
    - Folio
        - Folio                 - Campo
        - Fecha                 - Campo
        - Tipo                  - Campo
        - Nombre del producto   - Campo
        - Precio                - Campo
        - Cantidad              - Campo
        - Total                 - Campo
        - Color                 - Campo
        - Empleado              - Campo
        - Rfc                   - Campo
    - Total ticket              - Campo
* Generar ticket - Button "creara un excel"
## 6 - Corte de caja
* Lista de folios - Table
    - Folio                 - Campo
    - Fecha                 - Campo
    - Total ticket          - Campo
* Total General             - Campo
* Generar ticket - Button "creara un excel"
## 8 - Respaldos
* Generar respaldo    - Button
* Recuperar respaldo  - Button
## 7 - Perfil
### Empleado
* Editar sus datos personales
* Editar Nombre de usuario
* Editar correo
* Editar contraseña
#### Acciones
* Generar ventas
* Ver tickets
* productos
    - Ver
    - Agregar
* provedores
    - Ver
    - Agregar
* Tickets
### - Administrador
* Editar datos personales de empleados
* ver correo y username de empleados
* Crear empleados
* Habilitar/deshabilitar empleados
### Acciones
* Generar ventas
* Realizar compras
* productos
    - Ver
    - Agregar
    - Editar  
* productos
    - Ver
    - Agregar
    - Editar 
* Registrar provedores
* Tickets
* Generar corte de caja
* Generar respaldo
* Recuperar Respaldo
