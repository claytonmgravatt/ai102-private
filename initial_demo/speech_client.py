import os

from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk


class AzureSpeechClient:
    def __init__(self):
        load_dotenv()
        self.speech_config = self._get_speech_config()
        self.audio_input_config = speechsdk.audio.AudioConfig(
            use_default_microphone=True
        )
        self.audio_output_config = speechsdk.audio.AudioOutputConfig(
            use_default_speaker=True
        )
        self.speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=self.speech_config, audio_config=self.audio_input_config
        )
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config, audio_config=self.audio_output_config
        )

    def _get_speech_config(self) -> speechsdk.SpeechConfig:
        speech_api_key = os.environ.get("AZURE_SPEECH_API_KEY")
        speech_region = os.environ.get("AZURE_SPEECH_REGION")
        speech_config = speechsdk.SpeechConfig(subscription=speech_api_key, region=speech_region)
        speech_config.speech_synthesis_voice_name ="en-US-NancyNeural"
        return speech_config

    def get_text_from_speech(self) -> str:
        """Record and recognize speech from the microphone."""
        print("Speak now...")
        query = self.speech_recognizer.recognize_once()
        return query.text


    def get_speech_from_text(self, text: str) -> None:
        """Synthesize speech from text."""
        self.speech_synthesizer.speak_text(text)


### Example usage
if __name__ == '__main__':
    speech_client = AzureSpeechClient()
    user_input = speech_client.get_text_from_speech()
    print(user_input)
    speech_client.get_speech_from_text(user_input)
