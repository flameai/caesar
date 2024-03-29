from common.fastapi.app import WebApp

from caesar.app import App
from caesar.endpoints.change_membership import (
    router as membership_change_router,
)

web_app = WebApp()

web_app.include_router(membership_change_router)

App.register_port(web_app)

if __name__ == "__main__":
    web_app.run()
