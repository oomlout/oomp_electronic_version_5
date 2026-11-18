"""Public links only: electronics builds do not access the project checkout."""
import json
from pathlib import Path
from urllib.parse import quote

CONFIG=json.loads((Path(__file__).resolve().parent/'repository_config.json').read_text(encoding='utf-8'))

def project_usage_url(identifier):
    return CONFIG['project_pages_url'].rstrip('/')+'/usage/index.html#'+quote(identifier,safe='')
