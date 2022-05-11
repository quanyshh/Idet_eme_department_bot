from gino import Gino

# from data.config import POSTGREURI
# from utils.db_api.add_to_database import add_data



db = Gino()

async def create_db():
    await db.set_bind("postgresql://idet:Idet2050!@localhost/su_info") #"postgresql://idet:Idet2050!@localhost/su_info"


    # Создаем таблицы
    # await db.gino.drop_all()
    # await db.gino.create_all()
    # await add_data()

