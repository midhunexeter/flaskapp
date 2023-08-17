def map_values():
    # maps pieces from FEN to a specific value
    return {
        'K': 5,   'k': -5,
        'Q': 4,   'q': -4,
        'R': 3,   'r': -3,
        'B': 2,   'b': -2,
        'N': 1,   'n': -1,
        '0': 0
    }

def map_vectors():
    # maps pieces from FEN to a specific vector
    return {
        'K': [1, 0, 0, 0, 0],
        'Q': [0, 1, 0, 0, 0], 
        'R': [0, 0, 1, 0, 0],
        'B': [0, 0, 0, 1, 0],
        'N': [0, 0, 0, 0, 1],
        'k': [-1, 0, 0, 0, 0],
        'q': [0, -1, 0, 0, 0],
        'r': [0, 0, -1, 0, 0],
        'b': [0, 0, 0, -1, 0],
        'n': [0, 0, 0, 0, -1],
        '0': [0, 0, 0, 0, 0],
    }

def fens2tensor(fens_arr, piece_map, is_reshape):
    """
    Converts a list of fens into a tensor, ready to be fed into a ML algorithm.
    
    Args:
        fens_arr   - array of fens without w/b: '8/3n4/5Q2/q2r1N2/2k2K2/3N4/3R4/8'
        piece_map  - a dictionary that maps each of the pieces to some value. It also need to have a key '0' for  
        is_reshape - boolean. Whether the data will be 8x8x? or 64x?
    """
    pieces = set(['K', 'Q', 'R', 'B', 'N', 'k', 'q', 'r', 'b', 'n'])
    numbers= set(['1', '2', '3', '4', '5', '6', '7', '8'])
    
    if is_reshape:
        shape = (8, 8) if isinstance(piece_map['0'], int) else (8, 8, len(piece_map['0']))
    
    if len(piece_map) != 11:
        raise Exception('Wrong prieces map', piece_map)
        
    if len(pieces & set(piece_map)) != 10:
        raise Exception('Pieces map misses some pieces')
    
    data = []
    for fen in fens_arr:
        modified_fen = []
        for char in fen.replace("/", ""):
            if char in numbers:
                modified_fen += ['0'] * int(char)
            elif char in pieces:
                modified_fen += [char]
            else:
                raise Exception('Wrong FEN', (fen, char))
        
        tmp = [piece_map[i] for i in modified_fen]
        if is_reshape:
            out = np.reshape(tmp, shape)
        else:
            out = np.array(tmp)
            
        data.append(out)
    
    return np.stack(data, axis=0)


