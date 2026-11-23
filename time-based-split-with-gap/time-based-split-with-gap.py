import numpy as np

def time_based_split(timestamps: list, train_end: int, gap: int, val_end: int) -> dict:
    timestamps = np.asarray(timestamps)
    indices = np.arange(len(timestamps))

    train_mask = timestamps < train_end

    val_mask = (timestamps >= train_end + gap) & (timestamps < val_end)

    return {
        "train_idx": indices[train_mask],
        "val_idx": indices[val_mask]
    }