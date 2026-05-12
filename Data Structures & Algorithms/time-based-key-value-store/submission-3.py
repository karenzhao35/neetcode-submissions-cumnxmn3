import bisect

class TimeMap:

    def __init__(self):
        self.timestamp_map = {}
        self.value_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_map[key] = self.timestamp_map.get(key, []) + [timestamp]
        self.value_map[key] = self.value_map.get(key, []) + [value]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp_map: return ""
        position = bisect.bisect(self.timestamp_map[key], timestamp) - 1
        if position < 0: return ""

        print(position, self.timestamp_map[key], self.value_map[key])

        return self.value_map[key][position]
        
