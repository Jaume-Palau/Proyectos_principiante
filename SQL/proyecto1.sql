
# HAY UN ERROR EN EL PROYECTO!!!
# SE HAN CREADO LAS TABLAS EN WORLD!!
# FALTA CORREGIRLO!!! (ya esta corregido en proyecto1-FINAL-.sql)
# Al final de este escript se eliminan las tablas creadas en world

# PROYECTO FINAL :  BASE DE DATOS DE UNA BIBLIOTECA

# CREACION de la tabla: libros
CREATE TABLE libros (
	id INT AUTO_INCREMENT,
    titulo VARCHAR(30),
    autor VARCHAR(30),
    año_publicacion INT,
    disponible BOOLEAN ,
    
    PRIMARY KEY (id)
    );
ALTER TABLE libros
MODIFY disponible BOOLEAN DEFAULT TRUE;

# CREACION de la tabla: usuarios
CREATE TABLE usuarios (
	id INT AUTO_INCREMENT,
    nombre VARCHAR(30),
    email VARCHAR(30) UNIQUE,
    
    PRiMARY KEY (id)
    );
    
# CREACION de la tabla: prestamos
CREATE TABLE prestamos (
	id INT AUTO_INCREMENT,
    libro_id INT,
    usuario_id INT,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    
    PRIMARY KEY(id), 
    FOREIGN KEY(libro_id) REFERENCES libros(id),
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

# INSERTAR datos en la tabla: libros
ALTER TABLE libros MODiFY año_publicacion INT;
INSERT INTO libros 
	(titulo,autor,año_publicacion)
VALUES 
	('Cien años de soledad','Gabriel Garcia Márquez','1967'),
	('1984', 'George Orwell', 1949),
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605),
    ('El Hobbit', 'J.R.R. Tolkien', 1937),
    ('La sombra del viento', 'Carlos Ruiz Zafón', 2001)
;

# INSERTAR datos en la tabla: usuarios
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
	(24,1,'2025-12-08'),
    (27,5,'2025-12-08')
;

##################################################

# CREAR INDICE POR TITULOS:
CREATE INDEX idx_titulos ON libros(titulo);
# CREAR INDICE POR USUARIOS:
CREATE INDEX idx_usuario_id ON prestamos(usuario_id);

# CONSULTAS OBLIGATORIAS:
# 1. Libros disponibles (solo los no prestados).
SELECT id,titulo
FROM libros 
WHERE id NOT IN (SELECT libro_id FROM prestamos);
# 2. Préstamos activos (mostrar libro + usuario + fecha).
SELECT l.titulo, u.nombre, p.fecha_prestamo,
# 3. Días transcurridos desde el préstamo (usar DATEDIFF ).
DATEDIFF(CURDATE(),p.fecha_prestamo) AS dias_prestado
FROM libros l
INNER JOIN prestamos p
ON l.id = p.libro_id
INNER JOIN usuarios u
ON p.usuario_id = u.id
;

##################################################

# ACTIVIDAD EXTRA:
# Eliminar autores de libros
ALTER TABLE libros DROP COLUMN autor;

# CREACION de la tabla: autores
CREATE TABLE autores (
	id INT AUTO_INCREMENT,
    nombre VARCHAR(100),
    
    PRIMARY KEY(id)
    );
    
# CREACION de la tabla intermedia: libros_autores
CREATE TABLE libros_autores (
	id_libro INT,
    id_autor INT,
    
    FOREIGN KEY(id_libro) REFERENCES libros(id),
    FOREIGN KEY(id_autor) REFERENCES autores(id)
);

#CORRECCIONES:
ALTER TABLE libros_autores 
MODIFY id_libro INT NOT NULL;

ALTER TABLE libros_autores 
MODIFY id_autor INT NOT NULL;

ALTER TABLE libros_autores
ADD PRIMARY KEY (id_libro,id_autor);

##################################################

# INSERTAR nuevos datos en tabla autores:
INSERT INTO autores (nombre)
	VALUES
		('Gabriel Garcia Márquez'),
		('George Orwell'),
		('Miguel de Cervantes'),
		('J.R.R. Tolkien'),
		('Carlos Ruiz Zafón');

# INSERTAR nuevos datos en tabla libros_autores:
INSERT INTO libros_autores (id_libro, id_autor)
VALUES
    (24, 1),  -- Cien años de soledad → Gabriel García Márquez
    (25, 2),  -- 1984 → George Orwell
    (26, 3),  -- Don Quijote → Miguel de Cervantes
    (27, 4),  -- El Hobbit → J.R.R. Tolkien
    (28, 5);  -- La sombra del viento → Carlos Ruiz Zafón

##################################################

# Consulta: "Libros de un autor específico".
SELECT l.titulo, a.nombre
FROM libros l
INNER JOIN libros_autores la
ON l.id = la.id_libro
INNER JOIN autores a
ON la.id_autor = a.id
WHERE a.nombre = 'Carlos Ruiz Zafón';

##################################################

#### ELIMINAR TABLAS CREADAS POR ERROR EN WORLD ####
USE world;

DROP TABLE IF EXISTS libros_autores;
DROP TABLE IF EXISTS prestamos;
DROP TABLE IF EXISTS autores;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS libros;
