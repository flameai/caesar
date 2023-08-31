from common.fastapi.app import App
from common.db.postgres.fastapi import Postgres


class CaesarApp(App):
    component_classes = [Postgres]


app = CaesarApp()

if __name__ == "__main__":
    app.run()
