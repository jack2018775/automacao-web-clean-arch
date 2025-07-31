from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True)
class ContaContabil:
    id: int
    desc: str
    deve_star: Optional[str] = None
    status: Optional[str] = None