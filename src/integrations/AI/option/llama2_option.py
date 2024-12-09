from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from src.integrations.AI.base_ai import BaseAI

class Llama2Option(BaseAI):
    def __init__(self, model_name: str = "meta-llama/Llama-2-7b-chat-hf", device: str = "auto"):
        self.model_name = model_name
        self.device = device
        self.pipeline = None

    def load_model(self):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name, use_fast=False)
        model = AutoModelForCausalLM.from_pretrained(self.model_name, device_map=self.device)
        
        self.pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_length=1024,
            temperature=0.7,
            top_p=0.9
        )

    def prepare_prompt(self, question: str, context: str = "") -> str:
        # Este prompt se puede ajustar según el formato esperado del modelo chat
        if context.strip():
            prompt = f"Context:\n{context}\n\nUser:\n{question}\nAssistant:"
        else:
            prompt = f"User:\n{question}\nAssistant:"
        return prompt

    def generate_response(self, prompt: str) -> str:
        response = self.pipeline(prompt, do_sample=True, max_length=512)[0]["generated_text"]
        return response

    def getJSONresponse(self, prompt: str) -> str:
        response = self.pipeline(prompt, do_sample=True, max_length=512)[0]
        return response
