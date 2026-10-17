import math
from collections import Counter


def bleu_score(candidate: list, reference: list, max_n: int) -> float:
    """
    Returns the unsmoothed BLEU score.
    """

    c_len = len(candidate)
    r_len = len(reference)

    if c_len == 0 or max_n <= 0:
        return 0.0

    bp = 1.0 if c_len >= r_len else math.exp(1 - r_len / c_len)

    log_precision_sum = 0.0

    for n in range(1, max_n + 1):
        candidate_ngrams = Counter(
            tuple(candidate[i:i + n])
            for i in range(c_len - n + 1)
        )
        reference_ngrams = Counter(
            tuple(reference[i:i + n])
            for i in range(r_len - n + 1)
        )
        total = sum(candidate_ngrams.values())
        if total == 0:
            return 0.0

        matches = sum(
            min(count, reference_ngrams[ngram])
            for ngram, count in candidate_ngrams.items()
        )
        precision = matches / total
        if precision == 0:
            return 0.0

        log_precision_sum += math.log(precision)
        
    geometric_mean = math.exp(log_precision_sum / max_n)

    return bp * geometric_mean