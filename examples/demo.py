from pathlib import Path
import json
from explanation_faithfulness_aied.synthetic import make_cases
from explanation_faithfulness_aied.core import evaluate_cases
root=Path(__file__).resolve().parents[1]; (root/'results').mkdir(exist_ok=True)
df=make_cases(); out=evaluate_cases(df); out.to_csv(root/'results'/'synthetic_faithfulness_cases.csv',index=False)
metrics={c:round(float(out[c].mean()),3) for c in ['comprehensiveness','sufficiency_gap','stability_jaccard','faithfulness_index']}; (root/'results'/'demo_metrics.json').write_text(json.dumps(metrics,indent=2)); print(json.dumps(metrics,indent=2))
