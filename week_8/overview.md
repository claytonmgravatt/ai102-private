| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 8    | June 27, 2024| [Develop Natural Language Processing Solutions with Azure AI Services](https://learn.microsoft.com/en-us/training/paths/develop-language-solutions-azure-ai/)                                | Modules 6-8                     |

## Study Guide Sections Covered
* Process speech by using Azure AI Speech
    - Implement text-to-speech
    - Implement speech-to-text
    - Improve text-to-speech by using Speech Synthesis Markup Language (SSML)
    - Implement custom speech solutions
    - Implement intent recognition *_Not covered by reading, but this is just a wrapper that does Speech-To-Text and sends to a CLU project_*
    - Implement keyword recognition

* Translate language
    - Translate text and documents by using the Azure AI Translator service
    - Implement custom translation, including training, improving, and publishing a custom model
    - Translate speech-to-speech by using the Azure AI Speech service
    - Translate speech-to-text by using the Azure AI Speech service
    - Translate to multiple languages simultaneously

# Develop Natural Language Processing Solutions with Azure AI Services

### Resources Used

Speech Service

Translator

## Speech

### Capabilities
 - *Speech to Text*
 - *Text to Speech*
 - *Speech Translation* : Speech -> Speech in another language
 - *Speaker Recognition* : Who is talking?
 - *Intent Recognition* : Integration with Conversational Language Understanding

#### One of the resources that requires a "region", rather than just key/endpoint.

#### Can configure output audio format
 - Audio File Type
 - Sample-rate
 - Bit-depth

#### Can configure different voices for TTS (Text To Speech):
 - Standard : More robot-ish (Deprecated!)
 - Neural : More natural sounding

#### Speech Synthesis Markup Language:
* XML-based syntax for better customization of how things are said.
    - Specify a speaking style, such as "excited" or "cheerful" when using a neural voice.
    - Insert pauses or silence.
    - Specify phonemes (phonetic pronunciations), for example to pronounce the text "SQL" as "sequel".
    - Adjust the prosody of the voice (affecting the pitch, timbre, and speaking rate).
    - Use common "say-as" rules, for example to specify that a given string should be expressed as a date, time, telephone number, or other form.
    - Insert recorded speech or audio, for example to include a standard recorded message or simulate background noise.

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" 
                     xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US"> 
    <voice name="en-US-AriaNeural"> 
        <mstts:express-as style="cheerful"> 
          I say tomato 
        </mstts:express-as> 
    </voice> 
    <voice name="en-US-GuyNeural"> 
        I say <phoneme alphabet="sapi" ph="t ao m ae t ow"> tomato </phoneme>. 
    </voice> 
</speak>
```

#### Custom Keywords via Speech Studio:
 * Allows for training a tiny model that only recognizing one word/phrase and can be exported to run on an edge device.
    - "Alexa", "Hey Google"
    - This is why most devices won't let you change the "wake word".

### _Discuss: Why would this be needed, doesn't Alexa know all words anyway?_

#### Custom Speech-To-Text via Speech Studio:
 * Allows for training models to better recognize text in specific scenarios.
    - Industry specific terminology : Linhenykus (dinosaur)
    - Specific hardware/background noise: Drive-through window
    - Company's specific products


## DEMO TIME

### Speech Translation

* Features
    - Speech -> translated text.
    - Speech -> translated speech (via performing above Text-To-Speech on translated text)

By default requires specifying the input language, but supports multiple targets.

"Multi-lingual" text translation is in preview, where it auto detects the spoken language (and it can switch).



### DEMO TIME

### Text Translation with Translator resrouce

* Features
    - Language detection
    - One-to-many translation (english -> French and German)
    - Script Transliteration (Japanese Hiragana to Latin characters)

 ### _Discuss: How could you implement speech -> translated speech if you didn't know the input language?_

* Supports training custom translation models

### DEMO TIME

## Example questions

### 1. Talky talky.
You work at a startup that's developing an innovative new ~~torture~~ interrogation device that reads funny jokes to encourage suspects to cooperate. Your team is tasked with implementing Text-To-Speech functionality. Fill in the missing part of the code.

```python
import os 
import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential

speech_api_key = os.environ.get("AZURE_SPEECH_API_KEY")
speech_region = os.environ.get("AZURE_SPEECH_REGION") 
credential = AzureKeyCredential(speech_api_key)

speech_config = speechsdk.SpeechConfig(
    subscription=speech_api_key, region=speech_region
)

audio_output_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

client = speechsdk._________(
    speech_config=speech_config, audio_config=audio_output_config
)

client.speak_text("Why don't scientists trust atoms? Because they make up everything.")
```

- a. SpeechRecognizer
- b. SpeechSynthesizer
- c. SpeechSpeaker
- d. SpeechSpeakerSynthesisRecognizer


### 2. Audio Adventures
VoiceGlobal, a startup building a next-generation multilingual conferencing platform, wants to enable users to listen to translated speech in real time. They require a solution that directly converts spoken language into another spoken language, making communication seamless between participants speaking different languages. Which Azure service should they use?

- a. Translator
- b. Speech
- c. Cognitive Search
- d. Bot Service

### 3. Global Chat Expansion
The WorldConverse team is enhancing chat for a global user base. One feature involves converting text from one script to another (e.g., Arabic to Latin script) to help users read familiar characters while retaining pronunciation. This will benefit users who speak the same language but use different writing systems.

Which Azure AI Translator feature provides this functionality?

- a. Text translation
- b. Language detection
- c. Speech translation
- d. Transliteration

## Project idea: SSML for reading plays.