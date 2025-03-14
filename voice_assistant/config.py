# voice_assistant/config.py

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    """
    Configuration class to hold the model selection.
    
    Attributes:
        TRANSCRIPTION_MODEL (str): The model to use for transcription (only 'fastwhisperapi').
        RESPONSE_MODEL (str): The model to use for response generation (only 'ollama').
        TTS_MODEL (str): The model to use for text-to-speech (only 'kokoro').
        LOCAL_MODEL_PATH (str): Path to the local model.
    """
    # Model selection - streamlined for offline use only
    TRANSCRIPTION_MODEL = 'fastwhisperapi'
    RESPONSE_MODEL = 'ollama'
    TTS_MODEL = 'kokoro'

    # Kokoro TTS settings
    KOKORO_VOICE = 'am_michael'  # Default to the cowboy voice
    KOKORO_SPEED = 1.2  # Playback speed (>1 is faster)
    
    # LLM Selection
    OLLAMA_LLM = "hf.co/unsloth/gemma-3-4b-it-GGUF:latest"
    
    # Path for local models
    LOCAL_MODEL_PATH = os.getenv("LOCAL_MODEL_PATH")

    # Directory paths
    TEMP_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "temp")
    TEMP_AUDIO_DIR = os.path.join(TEMP_DIR, "audio")
    
    # Audio file paths
    INPUT_AUDIO = os.path.join(TEMP_AUDIO_DIR, "input.mp3")
    OUTPUT_AUDIO = os.path.join(TEMP_AUDIO_DIR, "output.wav")

    @staticmethod
    def validate_config():
        """
        Validate the configuration to ensure it's set to use the offline models.
        
        Raises:
            ValueError: If models are not set to use offline options.
        """
        Config._validate_model('TRANSCRIPTION_MODEL', ['fastwhisperapi'])
        Config._validate_model('RESPONSE_MODEL', ['ollama'])
        Config._validate_model('TTS_MODEL', ['kokoro'])

    @staticmethod
    def _validate_model(attribute, valid_options):
        model = getattr(Config, attribute)
        if model not in valid_options:
            raise ValueError(
                f"Invalid {attribute}. Must be one of {valid_options}"
            )
        
    @staticmethod
    def _validate_api_key(model_attr, model_value, api_key_attr):
        if getattr(Config, model_attr) == model_value and not getattr(Config, api_key_attr):
            raise ValueError(f"{api_key_attr} is required for {model_value} models")