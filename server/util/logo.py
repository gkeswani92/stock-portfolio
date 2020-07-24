import requests
from functools import lru_cache
from requests.auth import HTTPBasicAuth
from typing import Optional


from server.config import load_private_configs

API_KEY = load_private_configs()["ticker_info"]["clearbit_api_key"]
URL = load_private_configs()["ticker_info"]["name_to_logo_api"]


@lru_cache(maxsize=1024)
def get_logo_url_for_company(name: str) -> Optional[str]:
    # Expected API behavior
    # 200	Successful lookup, result encoded in the response body.
    # 404	Company not found.
    # 422	Company name is invalid.
    response = requests.get(
        URL.format(company_name=name.split(" ")[0]), auth=(API_KEY, "")
    )
    status_code = response.status_code
    if status_code == 200:
        return response.json()["logo"]
    elif status_code == 404:
        raise ValueError(f"Invalid company name: {name}")
    else:
        return "https://upload.wikimedia.org/wikipedia/commons/c/ce/Example_image.png"
