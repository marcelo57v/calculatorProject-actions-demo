class Memory:
    def __init__(self) -> None:
        self._store: dict[int, float] = {}
        self._next_id: int = 1

    def create(self, value: float) -> int:
        entry_id = self._next_id
        self._store[entry_id] = value
        self._next_id += 1
        return entry_id

    def read(self, entry_id: int) -> float:
        if entry_id not in self._store:
            raise ValueError(f"ID inválido: {entry_id}")
        return self._store[entry_id]

    def update(self, entry_id: int, value: float) -> None:
        if entry_id not in self._store:
            raise ValueError(f"ID inválido: {entry_id}")
        self._store[entry_id] = value

    def delete(self, entry_id: int) -> None:
        if entry_id not in self._store:
            raise ValueError(f"ID inválido: {entry_id}")
        del self._store[entry_id]

    def list_all(self) -> dict[int, float]:
        return self._store.copy()

    