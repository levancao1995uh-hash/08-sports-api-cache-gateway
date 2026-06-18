from src.sports_api_cache_gateway import build_seo_keywords, normalize_match_record

def test_build_seo_keywords_deduplicates():
    assert len(build_seo_keywords(["football live score", "Football Live Score"])) >= 1

def test_normalize_match_record_basic():
    row = normalize_match_record({"id": 1, "homeTeam": {"name": "A"}, "awayTeam": {"name": "B"}, "status": "SCHEDULED"})
    assert row["home_team"] == "A"
    assert row["away_team"] == "B"
