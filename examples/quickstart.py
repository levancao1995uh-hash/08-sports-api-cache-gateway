"""Example quickstart for the project."""

from pathlib import Path
import json

sample = Path(__file__).resolve().parents[1] / 'data' / 'raw' / 'sample_matches.json'
print(json.loads(sample.read_text(encoding='utf-8'))[0])
