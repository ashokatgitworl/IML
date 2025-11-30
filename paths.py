import os
from pathlib import Path

# Base directory (parent of the folder where this file lives)
ROOT_DIR = Path(__file__).resolve().parent.parent

ENV_FPATH = ROOT_DIR / ".env"

CODE_DIR = ROOT_DIR / "code"

APP_CONFIG_FPATH = ROOT_DIR / "workspaces/IML" / "config" / "config.yaml"
PROMPT_CONFIG_FPATH = ROOT_DIR / "workspaces/IML" / "config" / "prompt_config.yaml"
OUTPUTS_DIR = ROOT_DIR / "workspaces/IML" / "outputs"

DATA_DIR = ROOT_DIR / "workspaces/IML" / "Source"
PUBLICATION_FPATH = DATA_DIR / "publication.md"

VECTOR_DB_DIR = OUTPUTS_DIR / "vector_db"
CHAT_HISTORY_DB_FPATH = OUTPUTS_DIR / "chat_history.db"

# Chroma Cloud details
CHROMA_URLL = "chromadb-cloud-production.up.railway.app"
CHROMA_PORTT = "443"
