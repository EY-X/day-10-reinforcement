my_list = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

# north_trains = []
# east_trains = []

# for row in my_list:
#     if row['train'] == '111':
#         direction = row['direction']
#     if row['train'] == '80B':
#         frequent = row['frequency_in_minutes']
#     if row['direction'] == 'north':
#         north_trains.append(row)
#     if row['direction'] == 'east':
#         east_trains.append(row)

def train_direction(direction, trains):
    new_trains = []
    for train in trains:
        if train['direction'] == direction:
            new_trains.append(train)
    return new_trains

print(train_direction('north', my_list))
train_direction('east', my_list)
train_direction('west', my_list)

