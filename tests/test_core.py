import pandas as pd
from explanation_faithfulness_aied.core import comprehensiveness,sufficiency_gap,jaccard,evaluate_cases

def test_metrics():
    assert abs(comprehensiveness(.8,.5)-.3)<1e-9
    assert sufficiency_gap(.8,.7)>0
    assert jaccard(['a','b'],['a','c'])==1/3

def test_eval():
    d=pd.DataFrame([dict(case_id='x',p_original=.8,p_without_top=.5,p_top_only=.75,top_features='a|b',perturbed_top_features='a|b',random_delta=.05)])
    assert 0<=evaluate_cases(d).faithfulness_index.iloc[0]<=1
