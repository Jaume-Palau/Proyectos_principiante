'''LOGICA DEL ORM'''

# Importar los archivos (database.py, models.py)
from database import engine,Base,SessionLocal
from models import User

if __name__ == '__main__':
    # Crear la session que permite insertar,borrar,consultar...
    db = SessionLocal()
    # Crear tablas en MySQL
    Base.metadata.create_all(engine)
    # Crear objetos
    usuario1 = User(name = 'Jaume',age = 30)
    usuario2 = User(name = 'Claudia')
    # Insertar datos
    db.add(usuario1)
    db.add(usuario2)
    db.commit()
    # Hacer consultas
    resultado = db.query(User).all()
    db.close()