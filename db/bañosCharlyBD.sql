CREATE TABLE Producto(
    Id VARCHAR(14),
    Tipo VARCHAR(200),
    Nombre VARCHAR(200),
    Precio DECIMAL(7,2),
    Existencia INT,
    Resurtible BOOLEAN,
    PRIMARY KEY(Id)
);

CREATE TABLE Empleado(
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

CREATE TABLE Proveedor(
    Id INT AUTO_INCREMENT,
    Rfc VARCHAR(13),
    Nombre VARCHAR(350),
    Telefono VARCHAR(13),
    direccion VARCHAR(350),
    Activo BOOLEAN DEFAULT TRUE,
    PRIMARY KEY(Id)
);

CREATE TABLE Compra(
    Id INT,
    Folio INT, --conjunto de compras
    Producto INT,
    Precio DECIMAL(7,2),
    Cantidad INT,
    PRIMARY KEY(Id),
    FOREIGN KEY(Folio)REFERENCES Ticket_compra(Folio),
    FOREIGN KEY(Producto)REFERENCES Producto(Id)
);

CREATE TABLE Ticket_compra(
    Folio INT,
    Fecha DATE,
    Id_empleado int,
    Id_proveedor int,
    FOREIGN KEY(Id_empleado)REFERENCES Empleado(Id),
    FOREIGN KEY(Id_proveedor)REFERENCES Proveedor(RFC)
);

CREATE TABLE Venta(
    Id INT,
    Folio INT,
    Producto INT,
    Color VARCHAR(150),
    Cantidad INT,
    FOREIGN KEY(Folio)REFERENCES Ticket_venta(Folio),
    PRIMARY KEY(Id),
    FOREIGN KEY(Producto)REFERENCES Producto(Id),
);

CREATE TABLE Ticket_venta(
    Folio INT,
    Fecha DATE,
    Id_empleado int,
    RFC_Cliente VARCHAR(13),
    FOREIGN KEY(Id_empleado)REFERENCES Empleado(Id),
);







--Disparadores para las tablas
--trigger para restar la existencia del producto despues de registrar una venta
delimiter //
create trigger existenciaVenta before insert on Ventas for each row
begin
update Producto set Existencia=Existencia-new.cantidad where Codigo_p=new.Producto;
end
//
delimiter ;

-- trigger para sumar la existencia del producto cuando realizamos una compra del producto
DELIMITER //
create trigger existenciaCompra After insert on Compras for each row
begin
update Producto set Existencia=Existencia+new.cantidad where Codigo_p=new.Producto;
end
//
delimiter ;

