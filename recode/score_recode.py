"""Score a completed blind recode against the original corpus codes (answer key).
Usage: python3 score_recode.py <completed_recode.csv>
Computes per-axis % agreement and Cohen's kappa as reported in Supplementary Table S9."""
import csv, re, sys
from collections import Counter
comp = sys.argv[1] if len(sys.argv)>1 else 'recode_procedural_blind_completed.csv'
rec = {r['sample_id']: r for r in csv.DictReader(open(comp))}
key = {r['sample_id']: r for r in csv.DictReader(open('recode_answer_key_DO_NOT_SEND.csv'))}
def kappa(pairs):
    n=len(pairs); po=sum(1 for a,b in pairs if a==b)/n
    ca=Counter(a for a,_ in pairs); cb=Counter(b for _,b in pairs)
    pe=sum(ca[c]*cb.get(c,0) for c in ca)/n**2
    return po,(po-pe)/(1-pe) if pe<1 else 1.0
def pnorm(p): m=re.match(r'(I{1,3}|IV|V)',p.strip()); return m.group(1) if m else p
def tnorm(t): return 'prediction' if t.strip()=='prediction+UQ' else t.strip()
T=[];P=[];Me=0;Mo=0;En=[]
flags=['XAI','UQ','calibration','ext-val','OOD','repro-signal']; F={f:[] for f in flags}
for sid in rec:
    r,k=rec[sid],key[sid]
    T.append((tnorm(r['T']),tnorm(k['T']))); P.append((pnorm(r['P']),pnorm(k['P'])))
    rM=set(x.strip() for x in r['M'].split(';')); kM=set(x.strip() for x in k['M'].split(';'))
    Me+=rM==kM; Mo+=bool(rM&kM)
    En.append(('none-explicit' in r['E'],'none-explicit' in k['E']))
    kt=set(x.strip() for x in re.split(r'[;+/]',k['trust']))
    if k['T']=='prediction+UQ': kt.add('UQ')
    rt=set(x.strip() for x in r['flags'].split(';') if x.strip())
    for f in flags: F[f].append((f in rt, f in kt or (f=='OOD' and 'transfer' in kt)))
n=len(rec)
for name,pairs in [('T full',T),('P full',P),('E none-vs-any',En)]+[(f'flag {f}',F[f]) for f in flags]:
    po,kp=kappa(pairs); print(f"{name}: {po:.1%} kappa {kp:.3f}")
print(f"M exact {Me/n:.1%} overlap {Mo/n:.1%}")
