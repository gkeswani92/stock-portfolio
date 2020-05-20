from functools import lru_cache
from typing import Any
from typing import Dict
from typing import Optional

import yaml


@lru_cache(maxsize=1)
def load_private_configs() -> Optional[Dict[str, Any]]:
    with open('server/private_config.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        return yaml.load(file, Loader=yaml.FullLoader)

    return None
