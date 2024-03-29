from common.hexagonal.app import App
from common.hexagonal.postgres import Postgres
from common.hexagonal.redis import Redis

App.register_adapter(Postgres)
App.register_adapter(Redis)
