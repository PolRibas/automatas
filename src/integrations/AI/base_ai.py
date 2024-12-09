from abc import ABC, abstractmethod

class BaseAI(ABC):
    @abstractmethod
    def load_model(self):
        """Load and prepare the model for inference."""
        pass

    @abstractmethod
    def prepare_prompt(self, question: str, context: str = "") -> str:
        """Prepare the prompt to send to the model, given a question and optional context."""
        pass

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Generate a response from the model given the prepared prompt."""
        pass

    @abstractmethod
    def getJSONresponse(self, prompt: str) -> str:
        """Generate a response from the model given the prepared prompt."""
        pass