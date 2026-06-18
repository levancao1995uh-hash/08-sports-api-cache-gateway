# API 接入说明

| 数据源 | 用途 | 限制 |
| --- | --- | --- |
| football-data.org | 提供 /v4/matches、/v4/competitions/{id}/matches、/v4/teams/{id}/matches、/v4/competitions/{id}/standings 等端点，适合赛程、比赛、球队和积分榜。 | 需遵守官方条款与频率限制 |
| TheSportsDB | 免费体育 API 可用于实体和事件数据；2 分钟 Livescores 属于 Premium 能力，适合作为可选增强。 | 需遵守官方条款与频率限制 |
| openfootball/football.json | 公开领域 JSON 赛程与赛果数据，无需 API key，适合作为离线数据包、测试样例和回退数据源。 | 需遵守官方条款与频率限制 |
