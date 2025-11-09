import yaml

class ConfigLoader:
    def __init__(self, base_path="ml/config"):
        self.base_path = base_path
        self.usdm_data_dictionary = self.load_yaml("usdm_data_dictionary.yaml")
        self.llm_models = self.load_yaml("llm_models.yaml")

    def load_yaml(self, filename):
        with open(f"{self.base_path}/{filename}", 'r') as f:
            return yaml.safe_load(f)

    def get_config_data(self):
        return {
            "usdm_data_dictionary": self.usdm_data_dictionary,
            "llm_models": self.llm_models
        }
