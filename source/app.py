from common.fastapi.app import App
from common.db.postgres.fastapi import Postgres
from common.db.redis.fastapi import Redis


class CaesarApp(App):
    component_classes = [Postgres, Redis]


app = CaesarApp()

if __name__ == "__main__":
    app.run()
