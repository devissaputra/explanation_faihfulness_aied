# Calculation reading guide: ../CALCULATIONS.md (repository root).
# Comprehensiveness = max(0,p-p_without); sufficiency gap = max(0,p-p_only).
# Jaccard overlap measures set stability. Clipping discards negative effects. The weighted faithfulness index is a heuristic on supplied synthetic probabilities, not a validated explanation metric or a model perturbation experiment.

from __future__ import annotations
import numpy as np, pandas as pd

def comprehensiveness(p_original:float,p_without_top:float)->float: return float(max(0,p_original-p_without_top))
def sufficiency_gap(p_original:float,p_top_only:float)->float: return float(max(0,p_original-p_top_only))
def jaccard(a,b)->float:
    A,B=set(a),set(b); return 1.0 if not A and not B else len(A&B)/max(1,len(A|B))
def faithfulness_index(comp:float,suff_gap:float,stability:float,random_delta:float)->float:
    signal=max(0,comp-random_delta); return float(np.clip(.45*signal+.30*(1-suff_gap)+.25*stability,0,1))
def evaluate_cases(df:pd.DataFrame)->pd.DataFrame:
    out=[]
    for r in df.itertuples():
        comp=comprehensiveness(r.p_original,r.p_without_top); suff=sufficiency_gap(r.p_original,r.p_top_only); stab=jaccard(str(r.top_features).split('|'),str(r.perturbed_top_features).split('|'))
        out.append({'case_id':r.case_id,'comprehensiveness':comp,'sufficiency_gap':suff,'stability_jaccard':stab,'random_baseline_delta':r.random_delta,'faithfulness_index':faithfulness_index(comp,suff,stab,r.random_delta)})
    return pd.DataFrame(out)
