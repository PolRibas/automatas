# from src.integrations.AI.option.llama2_option import Llama2Option
from src.integrations.AI.option.falcon_option import FalconOption
# from src.integrations.AI.option.llama31_option import Llama31Option
from ..common import config
from huggingface_hub import HfApi

def test_models():
    # Instanciar los modelos
    # llama_model = Llama2Option()
    falcon_model = FalconOption()
    # llama31_model = Llama31Option()

    # Cargar los modelos
    # llama_model.load_model()
    falcon_model.load_model()
    # llama31_model.load_model()

    # Preguntas
    question = "Who are you?"
    question_json = "Who are you? answer in JSON: {\"name\": \"Falcon\"}"

    # Lista de modelos a probar
    models = [
        # (llama_model, "Llama2Option"),
        (falcon_model, "FalconOption"),
        # (llama31_model, "Llama31Option")
    ]

    for model, name in models:
        # Preparar prompt y generar respuesta normal
        prompt = model.prepare_prompt(question)
        response = model.generate_response(prompt)
        print(f"--- {name} Response ---")
        print(response)

        # Preparar prompt y generar respuesta JSON
        prompt_json = model.prepare_prompt(question_json)
        json_response = model.getJSONresponse(prompt_json)
        print(f"--- {name} JSON Response ---")
        print(json_response)

def main():
    print("Runing Project One")
    api = HfApi(token=config.HUGGINGFACE_API_KEY)
    whoami_info = api.whoami()
    print("Logged in as:", whoami_info["name"])
    test_models()