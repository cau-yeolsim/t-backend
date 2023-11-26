import os

from langchain.chat_models import ChatOpenAI
from langchain.chat_models.base import (
    BaseChatModel,
)
from t_backend.langchain.prompts import SYSTEM_TEMPLATE, HUMAN_TEMPLATE
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)


class OpenAIRepository:
    chat: BaseChatModel
    system_message_prompt_template: SystemMessagePromptTemplate

    def __init__(self):
        self.chat = ChatOpenAI(
            temperature=0,
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
            model_name="gpt-3.5-turbo",
        )
        self.system_message_prompt_template = SystemMessagePromptTemplate.from_template(
            SYSTEM_TEMPLATE
        )
        self.human_message_prompt_template = HumanMessagePromptTemplate.from_template(
            HUMAN_TEMPLATE
        )

    def send_message(self, message: str):
        chat_prompt_template = ChatPromptTemplate.from_messages(
            [self.system_message_prompt_template, self.human_message_prompt_template]
        )
        final_prompt = chat_prompt_template.format_prompt(
            output_language="ko",
            max_words=15,
            sample_text=message,
        ).to_messages()
        return self.chat(final_prompt)
