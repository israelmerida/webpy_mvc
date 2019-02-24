create database ria_iniciales;
use ria_iniciales;
create table clientes(
    id_clientes int(4) not null auto_increment primary key ,
    nombre_cliente varchar(20)not null,
    apellidos_cliente varchar(30) not null,
    colonia varchar (30) not null,
    calle varchar(30) not null);

create table productos(
    id_producto int(4) not null auto_increment primary key,
    nombre_producto varchar(20) not null,
    neto varchar(10) not null,
    marca varchar(20) not null,
    precio int(7) not null);

insert into clientes(nombre_cliente,apellidos_cliente,colonia,calle)
values('felix','Hernandez perez','santa maria','san pedro'),
('itzel','lopez castro','almoloya','8 de septiembre'),
('daniel','marquez luqueño','pedregal','hidalgo');

insert into productos (nombre_producto,neto,marca,precio)
values ('coca cola','600 ml','coca cola','12'),
('rufles','12 gm','sabritas','11'),
('agua','500 ml','alpura','8');

show tables;

select * from clientes;
describe clientes;

select * from productos;
describe productos;

create user 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
Grant ALL PRIVILEGES ON ria_iniciales.* TO'ria'@'localhost';
FLUSH PRIVILEGES;
