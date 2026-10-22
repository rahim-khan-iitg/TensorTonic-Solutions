import numpy as np

def wasserstein_critic_loss(real_scores: list, fake_scores: list) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    real_scores=np.array(real_scores).mean()
    fake_scores=np.array(fake_scores).mean()
    score=fake_scores-real_scores
    return score.item()