from abc import ABCMeta, abstractmethod


class ChatBase(metaclass=ABCMeta):

    @abstractmethod
    def create_sentence(self) -> str: pass

    @abstractmethod
    def sentence_classification(self) -> str: pass

    @abstractmethod
    def sentence_summary(self) -> str: pass

    @abstractmethod
    def short_answer_question(self) -> str: pass

    @abstractmethod
    def inference_of_correct_answers(self) -> str: pass

    @abstractmethod
    def conversion_of_speech(self) -> str: pass

    @abstractmethod
    def question_and_answer(self) -> str: pass
