import yaml

class Zone:
    def __init__(self, name: str, lat: float, lon: float, neighbors: list[str] = None, id: str = None, region: str = None): # type: ignore
        self.id = id or name.lower().replace(" ", "_")
        self.name = name
        self.lat = lat
        self.lon = lon
        self.neighbors = neighbors or []
        self.region = region

    def coords(self):
        return self.lat, self.lon
    
    def __repr__(self):
        return f"<Zone {self.name} ({self.lat},{self.lon})>"

def load_zones(yaml_path="config/zones.yaml") -> list[Zone]:
    with open(yaml_path) as f:
        raw = yaml.safe_load(f)
    return [Zone(**zone) for zone in raw["zones"]]