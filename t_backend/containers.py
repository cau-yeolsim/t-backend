from dependency_injector import containers, providers

from t_backend import routers
from t_backend.database import Database
from t_backend.repositories.chat import ChatRepository
from t_backend.services.chat import ChatService
from t_backend.settings import settings


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=[routers])

    config = providers.Configuration()
    db = providers.Singleton(Database, db_url=settings.SQLALCHEMY_DATABASE_URL)

    chat_repository = providers.Factory(
        ChatRepository, session_factory=db.provided.session
    )
    chat_service = providers.Factory(ChatService, chat_repository=chat_repository)
