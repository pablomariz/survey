import json
from typing import Union, List, Dict, Optional

def format_answer(answer: Optional[Union[str, List[Dict[str, str]]]]) -> Optional[Union[str, List[Dict[str, str]]]]:
    if answer is None:
        return None
 
    if isinstance(answer, str):
        try:
            parsed_answer = json.loads(answer)
            if isinstance(parsed_answer, list):
                return parsed_answer
            else:
                return answer
        except json.JSONDecodeError:
            return answer
    elif isinstance(answer, list):
        for item in answer:
            if not isinstance(item, dict) or not all(isinstance(key, str) for key in item.keys()):
                raise ValueError("A lista deve conter dicionários com chaves de string.")
        return answer
    else:
        raise ValueError("Tipo de resposta não suportado.")
