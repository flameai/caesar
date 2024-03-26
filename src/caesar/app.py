from common.db.postgres.fastapi import Postgres
from common.db.redis.fastapi import Redis
from common.fastapi.app import App
from common.fastapi.config import Config

from caesar.endpoints.change_membership import (
    router as membership_change_router,
)

Config.add_app_component_class(Postgres)
Config.add_app_component_class(Redis)

app = App()

app.include_router(membership_change_router)

if __name__ == "__main__":
    app.run()
