import os


def basedir() -> str:
    return os.path.abspath(os.path.dirname(__file__))


def make_sqlite_url(name: str) -> str:
    return "sqlite:///" + os.path.join(basedir(), name)


class Config(object):
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DB_URL") or make_sqlite_url(os.getenv("DB_NAME", "app.db"))
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    NLP_MODEL_NAME = os.getenv("NLP_MODEL_NAME", "roberta-large-nli-stsb-mean-tokens")
