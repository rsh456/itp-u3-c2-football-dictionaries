def players_by_country_and_position(squads_list):
    country_list={}
    position_list={}
    result={}
    f_list={}
    for player in squads_list:
        play_cl = players_as_dictionaries(player)
        country= player[6]
        position= player[1]
        result.setdefault(country,{})
        result[country].setdefault(position,[])    
        result[country][position].append(play_cl)
    return result

def players_as_dictionaries(squad):
    player={
            'caps': squad[4],
            'club': squad[5],
            'club_country': squad[7],
            'country':  squad[6],
            'date_of_birth':  squad[3],
            'name':  squad[2],
            'number':  squad[0],
            'position':  squad[1],
            'year':  squad[-1]
        }
    return player
