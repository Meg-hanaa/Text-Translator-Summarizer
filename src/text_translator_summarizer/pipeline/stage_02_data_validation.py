from text_translator_summarizer.config.configuration import ConfigurationManager
from text_translator_summarizer.components.data_validation import DataValidation
from text_translator_summarizer import config
from text_translator_summarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()