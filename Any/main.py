from typing import Any

def process_data(data: Any = None) -> None:
    print(f"Recebido: {data}")

process_data()
process_data("Texto")   # Ok
process_data(123)       # Ok
process_data([1, 2, 3]) # Ok
