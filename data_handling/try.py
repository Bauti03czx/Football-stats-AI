from kloppy import wyscout

dataset = wyscout.load(
    event_data="data/wyscout/events_Italy.json",
    match_data="data/wyscout/matches_Italy.json",
    player_data="data/wyscout/players_Italy.json",
    # Optional arguments
    event_types=["shot", "pass"],
    coordinates="wyscout"
)

dataset.to_df().head()