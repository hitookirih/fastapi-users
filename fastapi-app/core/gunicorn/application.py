from fastapi import FastAPI
from gunicorn.app.base import BaseApplication


class Application(BaseApplication):
    def __init__(
        self,
        app: FastAPI,
        options: dict | None = None,
    ):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load(self):
        return self.application

    @property
    def config_options(self) -> dict:
        return {
            # pair
            k: v
            # for each option
            for k, v in self.options.items()
            # not empty key/ value
            if k in self.cfg.settings and v is not None
        }

    def load_config(self) -> None:
        for key, value in self.options.items():
            self.cfg.set(key.lower(), value)
