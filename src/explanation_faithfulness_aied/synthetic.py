import numpy as np, pandas as pd

def make_cases(n=300,seed=23):
    rng=np.random.default_rng(seed); vocab=['evidence','feedback','question','elaboration','uptake','example','reasoning','prompt']
    rows=[]
    for i in range(n):
        p=float(rng.uniform(.55,.95)); comp=float(rng.beta(3,4)*.45); suff=float(rng.beta(2,5)*.25); top=rng.choice(vocab,3,replace=False).tolist(); pert=top.copy()
        if rng.random()<.35: pert[-1]=rng.choice([x for x in vocab if x not in pert])
        rows.append({'case_id':f'C{i:04d}','p_original':p,'p_without_top':max(.01,p-comp),'p_top_only':max(.01,p-suff),'top_features':'|'.join(top),'perturbed_top_features':'|'.join(pert),'random_delta':float(rng.beta(2,8)*.15)})
    return pd.DataFrame(rows)
