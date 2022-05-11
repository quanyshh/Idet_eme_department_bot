from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
ADMIN = env.list("ADMIN")
# IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

PG_USER = env.str("PG_USER")
PG_PASS = env.str("PG_PASS")
host = env.str("ip")
DB_NAME = env.str("DB_NAME")

POSTGREURI = f"postgresql://{PG_USER}:{PG_PASS}@{host}/{DB_NAME}"