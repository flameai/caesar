from common.fastapi.app import App
from common.db.postgres.fastapi import Postgres
from common.db.redis.fastapi import Redis

from source.endpoints.change_membership import router as membership_change_router


class CaesarApp(App):
    component_classes = [Postgres, Redis]


app = CaesarApp()
app.include_router(membership_change_router)

if __name__ == "__main__":
    app.run()
