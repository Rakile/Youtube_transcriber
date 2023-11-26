# Youtube_transcriber
A small application to transcribe/translate a youtube clip or a local video or audio file. It uses the free to use OpenAI whisper, and if keys are provided, can also speak the transcription.
Just run the runme.bat to create the virtual environment and also start the application.

Or if you are on another platform (not tested)
Run:

python -m venv youtube_transcriber

Then activate the environment:

.\youtube_transcriber\Scripts\activate.bat  or maybe ./youtube_transcriber/Scripts/activate.sh (if on linux)

Then start the application:

python transcriber_v2.py

Usage:

YouTube Transcriber uses OpenAI's whisper models, and you can choose from: tiny, small, base, medium  and the large modell. (If they are not downloaded yet,
they will be downloaded as you choose them). See https://github.com/openai/whisper for more information about the different models.

If you have access to NovelAI, and can create a Persistent API token, see: https://docs.novelai.net/text/UserSettings/account.html , you can have NovelAI speak the transcribed text to you.

Also, if you have access to an OpenAI API Key, you can use it to let OpenAI speak the transcribed text for you.

If you don't have access to any of the above two, you can just leave those blank. This will get you the transcribed text, but with no voice-over afterwards.
