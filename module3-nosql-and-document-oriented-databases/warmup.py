def road_length(island):
  length = 0
  for i, row in enumerate(island):
    for j, col in enumerate(row):

      if col == 'I': # if this cell is island

        # LEFT
        if j == 0 or row[j-1] == 'W': # is neighbor water or a boundary?
          length += 1

        # RIGHT
        if j == (len(row) - 1) or row[j+1] == 'W': # is neighbor water or a boundary?
          length += 1

        # UP
        if i == 0 or island[i-1][j] == 'W': # is neighbor water or a boundary?
          length += 1

        # DOWN
        if i == (len(island) - 1) or island[i+1][j] == 'W': # is neighbor water or a boundary?
          length += 1 # add road

  return length