def canonical_preference_pairs(records: list) -> dict:
    """
    Returns a dict with pairs: a list of prompt_id, winner_id, loser_id dictionaries.
    """
    ans={"pairs":[]}
    for prompt in records:
        prompt_id=prompt['prompt_id']
        candidates=prompt['candidates']
        ranks=[]
        for candidate in candidates:
            candidate_id=candidate['id']
            candidate_rank=candidate['rank']
            ranks.append((candidate_rank,candidate_id))
        ranks=sorted(ranks,key=lambda x:x[0])
        print(ranks)
        for i in range(len(ranks)):
            for j in range(i+1,len(ranks)):
                ans['pairs'].append({"prompt_id":prompt_id,"winner_id":ranks[i][1],"loser_id":ranks[j][1]})
    return ans
