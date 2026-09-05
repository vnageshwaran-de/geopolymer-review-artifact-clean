import csv, re, unicodedata

def norm(t):
    t = unicodedata.normalize('NFKD', t.lower())
    return re.sub(r'[^a-z0-9]', '', t)

# load existing corpus
existing = []
with open('corpus_screening.csv', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 0: continue
        parts = line.rstrip('\n').split('|')
        if len(parts) == 6:
            existing.append(dict(zip(['id','source','year','venue','title','decision'], parts)))
ex_by_norm = {}
for e in existing:
    # strip DOI parentheticals from CR titles for matching
    t = re.sub(r'\(10\.[^\)]*\)', '', e['title'])
    ex_by_norm[norm(t)] = e

# load scopus export
with open('scopus_familyA_export.csv', encoding='utf-8-sig') as f:
    scopus = list(csv.DictReader(f))

EC5_PAT = re.compile(r'adsorb|adsorpt|photocatal|\bdye\b|dyes\b|biodiesel|methylene blue|tetracycline|wastewater|waste water|effluent|catalytic|catalysis|catalyst|desalin|membrane distill|pollutant degrad|antibacterial|antimicrobial|drug delivery|pfas|phosphate recovery|h2 evolution|hydrogen production|co2 capture sorbent', re.I)
KEEP_PAT = re.compile(r'immobiliz|solidif|stabiliz', re.I)  # S/S construction-relevant → keep

matched, new = 0, 0
out = []
for s in scopus:
    n = norm(s['Title'])
    hit = ex_by_norm.get(n)
    if not hit:
        # prefix match for truncated titles
        for k, v in ex_by_norm.items():
            if len(k) > 40 and (k.startswith(n[:60]) or n.startswith(k[:60])):
                hit = v; break
    if hit:
        matched += 1
        out.append({'scopus_eid': s['EID'], 'doi': s['DOI'], 'year': s['Year'], 'venue': s['Source title'],
                    'title': s['Title'], 'doctype': s['Document Type'], 'status': 'MATCHED-' + hit['id'],
                    'decision': hit['decision'], 'cited_by': s['Cited by']})
    else:
        new += 1
        title = s['Title']
        if s['Document Type'] == 'Review':
            dec = 'CONTEXT-REVIEW'
        elif EC5_PAT.search(title) and not KEEP_PAT.search(title):
            dec = 'EXCLUDE-EC5-AUTO'
        else:
            dec = 'INCLUDE-PROVISIONAL'
        out.append({'scopus_eid': s['EID'], 'doi': s['DOI'], 'year': s['Year'], 'venue': s['Source title'],
                    'title': title, 'doctype': s['Document Type'], 'status': 'NEW-SCOPUS',
                    'decision': dec, 'cited_by': s['Cited by']})

with open('corpus_master.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader(); w.writerows(out)

# add existing records NOT found in scopus (from other sources) for completeness ledger
scopus_norms = {norm(s['Title']) for s in scopus}
only_fallback = [e for e in existing if norm(re.sub(r'\(10\.[^\)]*\)', '', e['title'])) not in scopus_norms
                 and not e['decision'].startswith('DUPLICATE')]

with open('corpus_fallback_only.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['id','source','year','venue','title','decision'])
    w.writeheader(); w.writerows(only_fallback)

from collections import Counter
c = Counter(o['decision'] for o in out if o['status'] == 'NEW-SCOPUS')
print(f'Scopus records: {len(scopus)}')
print(f'  matched to existing corpus: {matched}')
print(f'  new (not in fallback corpus): {new}')
print('  new-record auto-decisions:', dict(c))
print(f'Fallback-only records (unique, non-dup, not in Scopus A): {len(only_fallback)}')
fc = Counter(e['decision'] for e in only_fallback)
print('  their decisions:', dict(fc))
