from . import fetcher

def latency() -> float:
    return fetcher.measure_latency()
