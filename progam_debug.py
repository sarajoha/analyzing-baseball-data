def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    aggregated_stats_dict = {}
    for row in statistics:
        statsdict = {playerid : row[playerid]}
        for field in fields:
            if field not in statsdict:
                statsdict.update({field: int(row[field])})
            else:
                value = statsdict[field]
                add = int(row[field])
                statsdict[field] = value + add

    aggregated_stats_dict[row[playerid]] = statsdict

    return aggregated_stats_dict

print(aggregate_by_player_id([{'player': '1', 'stat1': '3', 'stat2': '4', 'stat3': '5'},
{'player': '1', 'stat1': '2', 'stat2': '1', 'stat3': '8'},
{'player': '1', 'stat1': '5', 'stat2': '7', 'stat3': '4'}],
'player', ['stat1', 'stat2']))