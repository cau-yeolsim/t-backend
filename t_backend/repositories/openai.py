from langchain.chat_models import ChatOpenAI
from langchain.chat_models.base import (
    BaseChatModel,
)
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.schema.messages import BaseMessage
from redis import Redis

from t_backend.langchain.prompts import SYSTEM_TEMPLATE, HUMAN_TEMPLATE
from t_backend.settings import settings


class OpenAIRepository:
    chat: BaseChatModel
    system_message_prompt_template: SystemMessagePromptTemplate
    _redis_client: Redis

    def __init__(self, redis_client: Redis):
        self.chat = ChatOpenAI(
            temperature=0,
            openai_api_key=settings.OPENAI_API_KEY,
            model_name="gpt-4",
            streaming=True,
        )
        self._redis_client = redis_client
        self.system_message_prompt_template = SystemMessagePromptTemplate.from_template(
            SYSTEM_TEMPLATE
        )
        self.human_message_prompt_template = HumanMessagePromptTemplate.from_template(
            HUMAN_TEMPLATE
        )

    def send_message(self, message_id: int, messages: list[BaseMessage]) -> str:
        chat_prompt_template = ChatPromptTemplate.from_messages(
            [self.system_message_prompt_template, self.human_message_prompt_template]
        )
        final_prompt = chat_prompt_template.from_messages(messages).format_prompt(
            output_language="ko",
            max_words=15,
        )
        full_content = ""
        for chunk in self.chat.stream(final_prompt):
            full_content += chunk.content
            self._redis_client.set(str(message_id), full_content)
        return full_content
