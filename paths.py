import os
from pathlib import Path


APP_ROOT = Path(__file__).resolve().parent
# CONFIG_PATH = APP_ROOT / "IMG" / "config" / "config.yaml"

# Base directory (parent of the folder where this file lives)
ROOT_DIR = Path(__file__).resolve().parent.parent

ENV_FPATH = ROOT_DIR / ".env"

CODE_DIR = ROOT_DIR / "code"

APP_CONFIG_FPATH = APP_ROOT / "IML" / "config.yaml"
PROMPT_CONFIG_FPATH = APP_ROOT /"IML" / "prompt_config.yaml"
OUTPUTS_DIR = ROOT_DIR / "workspaces/IML" / "outputs"

DATA_DIR = ROOT_DIR / "workspaces/IML" / "Source"
PUBLICATION_FPATH = DATA_DIR / "publication.md"

VECTOR_DB_DIR = OUTPUTS_DIR / "vector_db"
CHAT_HISTORY_DB_FPATH = OUTPUTS_DIR / "chat_history.db"

# Chroma Cloud details
CHROMA_URLL = "chromadb-cloud-production.up.railway.app"
CHROMA_PORTT = "443"
