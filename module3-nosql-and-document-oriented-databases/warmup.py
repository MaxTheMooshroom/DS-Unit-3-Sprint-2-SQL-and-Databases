def road_length(island):
  length = 0
  for i, row in enumerate(island):
    for j, col in enumerate(row):

      if col == 'I': # if this cell is island

        # LEFT
        if j != 0: # boundary check
          if row[j-1] == 'W': # is neighbor water
            length += 1 # add road
        else: # map boundaries get roads
          length += 1 # add road

        # RIGHT
        if j != (len(row) - 1): # boundary check
          if row[j+1] == 'W': # is neighbor water
            length += 1 # add road
        else: # map boundaries get roads
          length += 1 # add road

        # UP
        if i != 0: # boundary check
          if island[i-1][j] == 'W': # is neighbor water
            length += 1 # add road
        else: # map boundaries get roads
          length += 1

        # DOWN
        if i != (len(island) - 1): # boundary check
          if island[i+1][j] == 'W': # is neighbor water
            length += 1 # add road
        else: # map boundaries get roads
          length += 1 # add road

  return length