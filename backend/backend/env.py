import os
import tempfile

from dotenv import load_dotenv

load_dotenv()

DEBUG_MODE = os.getenv("ASKTUBE_DEBUG_MODE", "on")
APP_DIR = os.getenv("ASKTUBE_APP_DIR", os.path.join(tempfile.gettempdir(), "asktube"))
LANGUAGE_PREFER_USAGE: str = os.getenv("ASKTUBE_LANGUAGE_PREFER_USAGE", "en")
AUDIO_CHUNK_SHORT_DURATION: int = int(os.getenv("ASKTUBE_AUDIO_CHUNK_SHORT_DURATION", 30))
AUDIO_CHUNK_DURATION: int = int(os.getenv("ASKTUBE_AUDIO_CHUNK_DURATION", 600))

GEMINI_API_KEY = os.getenv("ASKTUBE_GEMINI_API_KEY", None)
OPENAI_API_KEY = os.getenv("ASKTUBE_OPENAI_API_KEY", None)
CLAUDE_API_KEY = os.getenv("ASKTUBE_CLAUDE_API_KEY", None)
VOYAGEAI_API_KEY = os.getenv("ASKTUBE_VOYAGEAI_API_KEY", None)

EMBEDDING_PROVIDER = os.getenv("ASKTUBE_EMBEDDING_PROVIDER", "gemini")
GEMINI_EMBEDDING_MODEL = os.getenv("ASKTUBE_GEMINI_EMBEDDING_MODEL", "models/text-embedding-004")
OPENAI_EMBEDDING_MODEL = os.getenv("ASKTUBE_OPENAI_EMBEDDING_MODEL", "text-embedding-ada-002")
VOYAGEAI_EMBEDDING_MODEL = os.getenv("ASKTUBE_VOYAGEAI_EMBEDDING_MODEL", "voyage-large-2")

LOCAL_EMBEDDING_MODEL = os.getenv("ASKTUBE_LOCAL_EMBEDDING_MODEL", "intfloat/multilingual-e5-large")
LOCAL_EMBEDDING_DEVICE = os.getenv("ASKTUBE_LOCAL_EMBEDDING_DEVICE", "cpu")

LOCAL_WHISPER_MODEL = os.getenv("ASKTUBE_LOCAL_WHISPER_MODEL", "base")
LOCAL_WHISPER_DEVICE = os.getenv("ASKTUBE_LOCAL_WHISPER_DEVICE", "cpu")
