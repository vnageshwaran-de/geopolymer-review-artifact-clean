import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, csv, re
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
def load(path):
    for enc in ('utf-8-sig','cp1252','latin-1'):
        try:
            with open(path, encoding=enc) as f: return list(csv.DictReader(f))
        except UnicodeDecodeError: continue
em = [r for r in load('/sessions/funny-trusting-euler/mnt/aus_paper/stage5/extraction_master.csv') if not r['duplicate_of']]
n = len(em); assert n == 677
def yr(r):
    y = int(r['year']); return 2026 if y==2027 else y

# ---------- F2 maturity ladder ----------
def stage(r):
    t=r['T_task']; fl=r['trust_flags']; p=r['P_physics']
    if t=='experiment-selection': return 7
    if t=='inverse-design': return 6
    if p.split('(')[0] in ('III-claimed','IV-claimed','V-candidate'): return 5
    if 'UQ' in fl or 'calibration' in fl: return 4
    if 'XAI' in fl: return 3
    if 'optim' in t: return 2
    return 1
years = list(range(2013,2027))
S = np.zeros((8,len(years)))
for r in em:
    S[stage(r)-1, years.index(yr(r))] += 1
labels = ["1. ML prediction","2. Optimization/MOO","3. Explainable AI","4. Uncertainty-aware",
          "5. Physics-informed (claimed)","6. Inverse design","7. Adaptive (simulated)","8. Autonomous"]
colors = plt.cm.viridis(np.linspace(0.05,0.95,8))
fig, ax = plt.subplots(figsize=(13,7.5))
bottom = np.zeros(len(years))
for i in range(8):
    ax.bar(years, S[i], bottom=bottom, color=colors[i], label=labels[i], width=0.75)
    bottom += S[i]
ax.set_xlabel("Publication year",fontsize=14); ax.set_ylabel(f"Unique studies (n = {n})",fontsize=14)
ax.set_title("Population of the AI-maturity ladder in geopolymer research, 2013–2026",fontsize=17)
ax.legend(loc='upper left',fontsize=11)
ax.text(0.98,0.965,"Autonomous stage: 0 studies detected\nAdaptive: 3 (all simulated)\n2026 bar includes one in-press item indexed 2027",
        transform=ax.transAxes,ha='right',va='top',fontsize=11,style='italic')
plt.tight_layout(); plt.savefig('/tmp/figs/F2_maturity_ladder.png',dpi=200); plt.close()

# ---------- F3 taxonomy ----------
fig, ax = plt.subplots(figsize=(12,7)); ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,10)
axes_l = [("M  Material system","#8d6e63"),("T  AI task","#1976d2"),("R  Trust profile (8 flags)","#7b1fa2"),
          ("P  Physics integration (I–V)","#689f38"),("E  Environmental function","#f57c00"),("D  Deployment maturity","#c2185b")]
for i,(t,c) in enumerate(axes_l):
    y=8.2-1.35*i
    ax.add_patch(FancyBboxPatch((0.4,y),4.2,1.0,boxstyle="round,pad=0.03",fc='white',ec=c,lw=2.5))
    ax.text(2.5,y+0.5,t,ha='center',va='center',fontsize=14)
    ax.add_patch(FancyArrowPatch((4.6,y+0.5),(5.6,5.0),arrowstyle='-|>',mutation_scale=18,lw=2,color='#37474f'))
ax.add_patch(FancyBboxPatch((5.6,3.4),2.6,3.2,boxstyle="round,pad=0.05",fc='#eceff1',ec='#37474f',lw=2))
ax.text(6.9,5.0,"ONE\nPRE-REGISTERED\nCODING\n(729 records →\n677 unique profiles,\nreleased)",ha='center',va='center',fontsize=13)
views = [("View A: AI-maturity ladder\n(headline Fig. 2)",7.9),("View B: Six-axis facets\n(analysis; Tables 2–5)",5.0),("View C: Translation pipeline\n(section order §7–14)",2.1)]
for t,y in views:
    ax.add_patch(FancyBboxPatch((8.9,y-0.75),2.9,1.5,boxstyle="round,pad=0.05",fc='#e8f5e9',ec='#2e7d32',lw=2))
    ax.text(10.35,y,t,ha='center',va='center',fontsize=13)
    ax.add_patch(FancyArrowPatch((8.2,5.0),(8.9,y),arrowstyle='-|>',mutation_scale=18,lw=2,color='#37474f'))
ax.text(6,9.6,"Figure 3. The multidimensional taxonomy: one coding, three views",ha='center',fontsize=17)
plt.savefig('/tmp/figs/F3_taxonomy.png',dpi=200,bbox_inches='tight'); plt.close()

# ---------- F4 trust heatmap ----------
cohorts = [("2013–2019",2013,2019),("2020–2021",2020,2021),("2022–2023",2022,2023),("2024",2024,2024),("2025",2025,2025),("2026",2026,2026)]
dims = [("Explainability",lambda f:'XAI' in f),("Uncertainty",lambda f:'UQ' in f),("Calibration",lambda f:'calibration' in f),
        ("External valid.",lambda f:'ext-val' in f),("OOD/transfer",lambda f:('OOD' in f or 'transfer' in f)),("Reproducibility",lambda f:'repro' in f)]
H = np.zeros((len(dims),len(cohorts))); Ns=[]
for j,(lab,a,b) in enumerate(cohorts):
    sub=[r for r in em if a<=yr(r)<=b]; Ns.append(len(sub))
    for i,(dl,fn) in enumerate(dims):
        H[i,j]=100*sum(1 for r in sub if fn(r['trust_flags']))/len(sub)
fig, ax = plt.subplots(figsize=(12,6.2))
im=ax.imshow(H,cmap='YlOrRd',aspect='auto',vmin=0,vmax=40)
ax.set_xticks(range(len(cohorts))); ax.set_xticklabels([f"{c[0]}\n(n={N})" for c,N in zip(cohorts,Ns)],fontsize=12)
ax.set_yticks(range(len(dims))); ax.set_yticklabels([d[0] for d in dims],fontsize=13)
for i in range(len(dims)):
    for j in range(len(cohorts)):
        ax.text(j,i,f"{H[i,j]:.0f}",ha='center',va='center',fontsize=12,color='white' if H[i,j]>22 else 'black')
ax.set_title("Trust-practice prevalence (%) by publication cohort — unique studies, n = 677",fontsize=15)
cb=fig.colorbar(im); cb.set_label("% of cohort",fontsize=12)
plt.tight_layout(); plt.savefig('/tmp/figs/F4_trust_heatmap.png',dpi=200); plt.close()

# ---------- F6 env pyramid ----------
fig, ax = plt.subplots(figsize=(12,7)); ax.axis('off')
rungs=[("ISO/boundary-explicit LCA: 2/76 (3%)",2,"#1b5e20"),("LCA performed: 13/76 (17%)",13,"#558b2f"),
       ("Carbon inside optimization objective\n(primary treatment): 19/76 (25%)",19,"#f9a825"),
       ("Emission factors (quantified, no LCA): 21/76 (28%)",21,"#e65100"),
       ("Environmental framing without\nquantification: 21/76 (28%)",21,"#b71c1c")]
y=4.4
for lab,v,c in rungs:
    w=0.3+3.4*v/21
    ax.add_patch(plt.Rectangle((0.2,y),w,0.75,fc=c))
    ax.text(w+0.45,y+0.37,lab,va='center',fontsize=15)
    y-=1.02
ax.set_xlim(0,10); ax.set_ylim(-0.4,6.4)
ax.text(0.2,5.9,"Environmental-evidence ladder among the 76 cluster-audited studies\n(drawn from the 150 carbon/LCA-flagged unique studies; corpus-wide, 44.8% of 677\nquantify no environmental variable at all)",fontsize=16,va='top')
ax.text(0.2,-0.15,"Note: 25 studies place carbon inside an optimization objective in total; 19 carry it as their primary environmental\ntreatment (shown). Rungs are mutually exclusive primary treatments; every audited study had environmental framing.",fontsize=11,color='#455a64')
plt.savefig('/tmp/figs/F6_env_pyramid.png',dpi=200,bbox_inches='tight'); plt.close()
print("all figs done; cohort Ns:",Ns)
