import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if len(seqs)==0:
        return np.array([],dtype='int').reshape(0,0)
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)

    sequences=[]
    for seq in seqs:
        if len(seq) < max_len:
            seq += [pad_value] * (max_len - len(seq))
            sequences.append(seq)
        elif len(seq) == max_len:
            sequences.append(seq)
        else:
            sequences.append(seq[:max_len])
    return np.array(sequences)
    