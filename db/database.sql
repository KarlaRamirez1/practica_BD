CREATE TABLE IF NOT EXISTS Producto(
    Id VARCHAR(14),
    Tipo VARCHAR(200),
    Nombre VARCHAR(200),
    Precio DECIMAL(7,2),
    Descripcion VARCHAR(500),
    Existencia INT,
    Resurtible BOOLEAN,
    PRIMARY KEY(Id)
);

CREATE TABLE IF NOT EXISTS Empleado(
    Id INT AUTO_INCREMENT,
    Nombre VARCHAR(100),
    Apellido_p VARCHAR(100),
    Apellido_m VARCHAR(100),
    Nombre_usuario VARCHAR(100),
    Email VARCHAR(350),
    Contrasenia VARCHAR(21),
    Puesto INT,
    Salario DECIMAL(7,2),
    Activo BOOLEAN DEFAULT TRUE,
    PRIMARY KEY(Id)
);

CREATE TABLE IF NOT EXISTS Proveedor(
    Id INT AUTO_INCREMENT,
    Rfc VARCHAR(13),
    Nombre VARCHAR(350),
    Telefono VARCHAR(13),
    direccion VARCHAR(350),
    Activo BOOLEAN DEFAULT TRUE,
    PRIMARY KEY(Id)
);

CREATE TABLE IF NOT EXISTS Compra(
    Id INT,
    Folio INT,
    Producto INT,
    Unidades INT,
    PRIMARY KEY(Id),
    FOREIGN KEY(Folio)REFERENCES Ticket_compra(Folio),
    FOREIGN KEY(Producto)REFERENCES Producto(Id)
);

CREATE TABLE IF NOT EXISTS Ticket_compra(
    Folio INT,
    Fecha DATE,
    Id_empleado int,
    Id_proveedor int,
    FOREIGN KEY(Id_empleado)REFERENCES Empleado(Id),
    FOREIGN KEY(Id_proveedor)REFERENCES Proveedor(RFC)
);

CREATE TABLE IF NOT EXISTS Venta(
    Id INT,
    Folio INT,
    Producto INT,
    Color VARCHAR(150),
    Unidades INT,
    PRIMARY KEY(Id),
    FOREIGN KEY(Folio)REFERENCES Ticket_venta(Folio),
    FOREIGN KEY(Producto)REFERENCES Producto(Id)
);

CREATE TABLE IF NOT EXISTS Ticket_venta(
    Folio INT,
    Fecha DATE,
    Id_empleado int,
    RFC_Cliente VARCHAR(13),
    FOREIGN KEY(Id_empleado)REFERENCES Empleado(Id)
);