from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)
class ContaContabil:
    id: int
    desc: str
    status: Optional[str] = None
    deve_star: str