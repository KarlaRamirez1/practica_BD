CREATE TABLE Producto(
    Codigo_p int,
    Nombre_p varchar(200),
    Tipo VARCHAR(200),
    Precio DECIMAL(7,2),
    Existencia INT,
    Resurtible CHAR(2),
    Estado char(1) DEFAULT "A",
    PRIMARY KEY(Codigo_p)
);

CREATE TABLE Empleado(
    Codigo_EM INT AUTO_INCREMENT,
    Nombre VARCHAR(350),
    Puesto VARCHAR(350),
    Salario DECIMAL(7,2),
    email_empleado VARCHAR(350),
    contraseña VARCHAR(21),
    Estado char(1) DEFAULT "A",
    PRIMARY KEY(Codigo_EM)
);

CREATE TABLE Proveedor(
    RFC_Proveedor VARCHAR(13),
    Nombre_Ed VARCHAR(350),
    Tel_ed INT,
    direccion_ed VARCHAR(350),
    Estado char(1) DEFAULT "A",
    PRIMARY KEY(RFC_Proveedor)
);


CREATE TABLE Compras(
    Folio_Compra INT,
    Producto INT,
    Cantidad INT,
    Precio DECIMAL(7,2),
    Subtotal DECIMAL(7,2),
    IVA DECIMAL(7,2),
    proveedor int,
    PRIMARY KEY(folio_Compra),
    FOREIGN KEY(Producto)REFERENCES Producto(Codigo_p),
    FOREIGN KEY(proveedor)REFERENCES Proveedor(RFC_Proveedor)
);

CREATE TABLE Ventas(
    Folio_venta INT,
    Producto INT,
    Color VARCHAR(200),
    Cantidad INT,
    Subtotal DECIMAL(7,2),
    IVA DECIMAL(7,2),
    Total DECIMAL (7,2),
    Fecha DATE,
    RFC_Cliente VARCHAR(13),
    PRIMARY KEY(Folio_venta),
    FOREIGN KEY(Producto)REFERENCES Producto(Codigo_p),
);

CREATE TABLE Efectua(
    Empleado int,
    Compra int,
    FOREIGN KEY(Empleado)REFERENCES Empleado(Codigo_EM),
    FOREIGN KEY(Compra)REFERENCES Compras(Folio_Compra)
);

CREATE TABLE Realiza(
    id_empleado INT,
    id_venta INT,
    FOREIGN KEY(id_empleado)REFERENCES Empleado(Codigo_EM),
    FOREIGN KEY(id_venta)REFERENCES VEntas(Folio_venta)
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

