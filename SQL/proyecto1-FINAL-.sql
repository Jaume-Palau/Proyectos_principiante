# PROYECTO FINAL :  BASE DE DATOS DE UNA BIBLIOTECA

CREATE DATABASE biblioteca;
USE biblioteca;

#### CREACION DE TABLAS ####

# CREACION de la tabla: libros
CREATE TABLE libros (
	id INT AUTO_INCREMENT NOT NULL,
    titulo VARCHAR(30) NOT NULL,
    año_publicacion INT NOT NULL,
    disponible BOOLEAN DEFAULT TRUE ,
    
    PRIMARY KEY (id)
    );
    
# CREACION de la tabla: autores
CREATE TABLE autores (
	id INT AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    
    PRIMARY KEY(id)
    );

# CREACION de la tabla intermedia: libros_autores
CREATE TABLE libros_autores (
	id_libro INT NOT NULL,
    id_autor INT NOT NULL,
    
    PRIMARY KEY(id_libro,id_autor),
    FOREIGN KEY(id_libro) REFERENCES libros(id),
    FOREIGN KEY(id_autor) REFERENCES autores(id)
);

# CREACION de la tabla: usuarios
CREATE TABLE usuarios (
	id INT AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    email VARCHAR(30) UNIQUE NOT NULL,
    
    PRiMARY KEY (id)
    );

# CREACION de la tabla: prestamos
CREATE TABLE prestamos (
	id INT AUTO_INCREMENT,
    libro_id INT NOT NULL,
    usuario_id INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE,
    
    PRIMARY KEY(id), 
    FOREIGN KEY(libro_id) REFERENCES libros(id),
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

#### INSERCION DE DATOS ####

# INSERTAR datos en la tabla libros:
INSERT INTO libros 
	(titulo,año_publicacion)
VALUES 
	('Cien años de soledad',1967),
	('1984', 1949),
    ('Don Quijote de la Mancha', 1605),
    ('El Hobbit', 1937),
    ('La sombra del viento', 2001)
;

# INSERTAR datos en tabla autores:
INSERT INTO autores (nombre)
	VALUES
		('Gabriel Garcia Márquez'),
		('George Orwell'),
		('Miguel de Cervantes'),
		('J.R.R. Tolkien'),
		('Carlos Ruiz Zafón')
	;

# INSERTAR datos en tabla libros_autores:
INSERT INTO libros_autores (id_libro, id_autor)
VALUES
    (1, 1),  -- Cien años de soledad → Gabriel García Márquez
    (2, 2),  -- 1984 → George Orwell
    (3, 3),  -- Don Quijote → Miguel de Cervantes
    (4, 4),  -- El Hobbit → J.R.R. Tolkien
    (5, 5)	 -- La sombra del viento → Carlos Ruiz Zafón
;          

# INSERTAR datos en la tabla usuarios:
INSERT INTO usuarios
	(nombre,email)
VALUES
	('Jaume','jps@gmail.com'),
	('Laura', 'laura@example.com'),
    ('Carlos', 'carlos@example.com'),
    ('Marta', 'marta@example.com'),
    ('Andrés', 'andres@example.com')
;
    
# INSERTAR prestamos activos (sin fecha de devolucion)
INSERT INTO prestamos 
	(libro_id,usuario_id,fecha_prestamo)
VALUES
	(2,1,'2025-12-08'),
    (3,5,'2025-12-08')
;	