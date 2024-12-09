from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from src.integrations.AI.base_ai import BaseAI

class Llama31Option(BaseAI):
    def __init__(self, model_name: str = "meta-llama/Llama-3.1-8B-Instruct", device: str = "auto"):
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
        if context.strip():
            prompt = f"Context:\n{context}\n\nQuestion:\n{question}\nAnswer:"
        else:
            prompt = f"Question:\n{question}\nAnswer:"
        return prompt

    def generate_response(self, prompt: str) -> str:
        response = self.pipeline(prompt, do_sample=True, max_length=512)[0]["generated_text"]
        return response

    def getJSONresponse(self, prompt: str) -> str:
        response = self.pipeline(prompt, do_sample=True, max_length=512)[0]
        return response
