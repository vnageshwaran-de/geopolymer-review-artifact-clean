import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
# arithmetic guards
assert 3+4+15+14+31+3 == 70 and 894-70 == 824 and 824-58 == 766
assert 6+28+3 == 37 and 766-37 == 729 and 729-52 == 677
assert 4+21+28+14+31+6 == 104 and 70-3+37 == 104
fig, ax = plt.subplots(figsize=(10.5, 13)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,15)
def box(x,y,w,h,text,fc,ec,fs=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05",fc=fc,ec=ec,lw=2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs)
def arr(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=22,lw=2,color='#37474f'))
box(0.3,13.3,4.6,1.5,"Records identified n = 1,214\nScopus Family A n=774 · ScienceDirect n=320\nCrossref n=100 · SpringerLink n=20\n(per-source counts post internal dedup)","#e8f5e9","#2e7d32",12)
box(5.6,13.5,4.1,1.1,"IEEE Xplore n=13\n(all conference papers\n→ excluded at source, EC4)","#f5f5f5","#9e9e9e",11)
arr(2.6,13.3,2.6,12.7)
box(0.3,11.6,4.6,1.1,"Duplicate records removed\nbefore screening n = 320\n(fallback records matched to Scopus)","#fff3e0","#ef6c00",12)
arr(2.6,11.6,2.6,11.0)
box(0.3,9.9,4.6,1.1,"Unique records screened n = 894\n100% dual screening (primary + 1 design)\nκ_A=0.830 · κ_B=0.689 · 59 adjudicated","#e3f2fd","#1565c0",12)
box(5.6,8.1,4.1,2.3,"Removed at title–abstract n = 70\nduplicates found in screening: 3\nEC1 preprint/non-journal: 4\nEC2 out of scope: 15\nEC4 conference: 14\nEC5 non-construction: 31\nEC7 venue quality: 3","#ffebee","#c62828",11)
ax.add_patch(FancyArrowPatch((4.9,10.3),(5.6,9.8),arrowstyle='-|>',mutation_scale=22,lw=2,color='#37474f'))
arr(2.6,9.9,2.6,9.3)
box(0.3,8.2,4.6,1.1,"Records retained after\ntitle–abstract screen n = 824","#f3e5f5","#6a1b9a",12)
box(5.6,6.1,4.1,1.2,"Context Corpus n = 58\n(reviews & adjacent evidence;\nnot in synthesis counts)","#f5f5f5","#616161",11)
ax.add_patch(FancyArrowPatch((4.9,8.5),(5.6,7.0),arrowstyle='-|>',mutation_scale=22,lw=2,color='#37474f'))
arr(2.6,8.2,2.6,7.6)
box(0.3,6.3,4.6,1.3,"Full-text eligibility decisions n = 49\ninclude 12 · exclude 37\n(EC2: 6 · EC3: 28 · EC7: 3)","#fff3e0","#ef6c00",12)
arr(2.6,6.3,2.6,5.7)
box(0.3,4.5,4.6,1.2,"Records included n = 729\n(2013–2026; frozen 21 Aug 2026)","#e8f5e9","#2e7d32",13)
box(5.6,3.4,4.1,1.5,"Duplicate reports identified\nin synthesis audit n = 52\n(flagged, not deleted;\nstage5/duplicate_audit.csv)","#fff3e0","#ef6c00",11)
ax.add_patch(FancyArrowPatch((4.9,4.9),(5.6,4.5),arrowstyle='-|>',mutation_scale=22,lw=2,color='#37474f'))
arr(2.6,4.5,2.6,3.9)
box(0.3,2.4,4.6,1.5,"CORE CORPUS\nn = 677 unique primary studies\n(729 records)","#e8f5e9","#1b5e20",15)
ax.text(5,14.95,"Figure 1. PRISMA 2020 flow of study identification and selection",ha='center',fontsize=16)
ax.text(0.3,1.0,"Balance: 894 − 70 = 824 · 824 − 58 (context) = 766 · 766 − 37 = 729 included (717 direct + 12 full-text inclusions).\nTotal excluded 104 = 67 title–abstract (EC1 4, EC2 15, EC4 14, EC5 31, EC7 3) + 37 full text (EC2 6, EC3 28, EC7 3).\n729 records − 52 duplicate reports = 677 unique studies. Query families B–F (Scopus; n=403/42/123/367/180) were\ncoverage checks: eligible hits verified subsumed by Family A + fallback; 0 unique additions. Full reconciliation: Suppl. Table S1.",fontsize=10,color='#455a64')
plt.savefig('/tmp/figs/F1_prisma.png',dpi=200,bbox_inches='tight'); plt.close(); print("ok")
