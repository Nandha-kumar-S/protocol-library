import json
import yaml
import logging
import requests
from openai import AzureOpenAI

# Suppress INFO logs from the httpx library
logging.getLogger("httpx").setLevel(logging.WARNING)

class GenAIModel:
    def __init__(self, model_name='o3', temperature=0, top_p=0, max_tokens=8000):
        self.config = self.load_config('ml/config/llm_models.yaml')
        self.model_name = self.config.get('CHOSEN_MODEL', model_name)
        self.mode = self.config.get('MODE', 'openai')  # Default to 'openai' library

        self.api_key = self.config[self.model_name].get('api_key')
        self.endpoint = self.config[self.model_name].get('api_endpoint')
        self.api_version = self.config[self.model_name].get('api_version', '2024-02-01')
        self.deployment_name = self.config[self.model_name].get('deployment_name')

        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens

        if self.mode == 'openai' and not self.deployment_name:
            raise ValueError(f"'deployment_name' not found in config for model {self.model_name}")

        self.client = AzureOpenAI(
            api_key=self.api_key,
            azure_endpoint=self.endpoint,
            api_version=self.api_version
        )
        self.system_prompt = 'You are a helpful assistant.'
    
    def load_config(self, config_file='ml/config/llm_models.yaml'):
        with open(config_file, 'r') as file:
            return yaml.safe_load(file)

    def infer(self, prompt):
        if self.mode == 'request':
            return self._infer_request(prompt)
        else:
            return self._infer_openai(prompt)

    def _get_llm_response(self, messages):
        try:
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=messages,
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Failed to make the request. Error: {e}")
            return None

    def _infer_openai(self, prompt):
        """
        Performs inference using the official openai library.
        """
        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        raw_output = self._get_llm_response(messages)
        if raw_output is None:
            return {}

        pro_output = raw_output.replace("```json\n", '|||').replace("```json", '|||')
        pro_output = pro_output.split("|||")[-1].split("```")[0].strip()
        try:
            parsed_output = json.loads(pro_output)
            return parsed_output
        except Exception as e:
            print(f"Failed to parse JSON response: {e} \n {raw_output}")
            return {}

    def _infer_request(self, prompt):
        """
        Performs inference using the requests library.
        """
        headers = {
            'Content-Type': 'application/json',
            'api-key': self.api_key
        }

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        payload = {
            "messages": messages,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "max_tokens": self.max_tokens
        }

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes
            raw_output = response.json()['choices'][0]['message']['content']
        except requests.RequestException as e:
            print(f"Failed to make the request. Error: {e}")
            return {}

        # Reuse the same JSON parsing logic
        pro_output = raw_output.replace("```json\n", '|||').replace("```json", '|||')
        pro_output = pro_output.split("|||")[-1].split("```")[0].strip()
        try:
            parsed_output = json.loads(pro_output)
            return parsed_output
        except Exception as e:
            print(f"Failed to parse JSON response: {e} \n {raw_output}")
            return {}

    def chosen_model_name(self):
        return str(self.model_name)