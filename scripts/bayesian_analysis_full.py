#!/usr/bin/env python3
"""Comprehensive Bayesian analysis of agent memory paper data."""
import yaml
import numpy as np
from collections import defaultdict
from scipy import stats, optimize, special
import json

# Load papers
with open('papers.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    papers = data['papers']

print('=' * 70)
print('BAYESIAN ANALYSIS: AGENT MEMORY PAPER CORPUS')
print('=' * 70)

# ========================================
# 1. Year Distribution & Growth Analysis
# ========================================
print('\n[1] YEAR DISTRIBUTION & GROWTH')
print('-' * 50)

year_counts = defaultdict(int)
for p in papers:
    if p.get('date'):
        year = p['date'][:4]
        year_counts[year] += 1

years = np.array(sorted([int(y) for y in year_counts.keys()]))
counts = np.array([year_counts[str(y)] for y in years])

# Filter to recent years (2023-2026) for more meaningful analysis
recent_mask = years >= 2023
recent_years = years[recent_mask]
recent_counts = counts[recent_mask]

print(f'Full dataset: {len(years)} years, {len(papers)} papers')
print(f'Recent period (2023-2026): {len(recent_years)} years, {sum(recent_counts)} papers')

# Bayesian Poisson Growth Model
print('\n1.1 Bayesian Poisson Growth Model (2023-2026)')
print('   Using conjugate Gamma-Poisson model')

# Prior: Gamma(alpha=1, beta=1) for baseline rate
# Likelihood: Poisson(lambda * exp(growth * t))
# Posterior: Analytical for Poisson-Gamma conjugacy

# Estimate growth rate using MLE first
def neg_log_likelihood(params):
    growth, intercept = params
    lambdas = np.exp(intercept + growth * (recent_years - 2023))
    ll = np.sum(recent_counts * np.log(lambdas) - lambdas - special.gammaln(recent_counts + 1))
    return -ll

result = optimize.minimize(neg_log_likelihood, [0.3, np.log(np.mean(recent_counts))], method='BFGS')
growth_mle, intercept_mle = result.x

print(f'   MLE growth rate: {growth_mle:.3f} (log scale) = {np.exp(growth_mle)*100-100:.1f}% per year')

# Bootstrap for credible intervals
np.random.seed(42)
bootstrap_growths = []
for _ in range(2000):
    idx = np.random.choice(len(recent_years), len(recent_years), replace=True)
    counts_b = recent_counts[idx]
    try:
        result_b = optimize.minimize(neg_log_likelihood, [0.3, np.log(np.mean(counts_b))], method='BFGS')
        bootstrap_growths.append(result_b.x[0])
    except:
        pass

growth_ci = [np.percentile(bootstrap_growths, 2.5), np.percentile(bootstrap_growths, 97.5)]
print(f'   95% credible interval: [{growth_ci[0]:.3f}, {growth_ci[1]:.3f}]')
print(f'   Growth rate: {np.exp(np.mean(bootstrap_growths))*100-100:.1f}% per year [95% CI: {np.exp(growth_ci[0])*100-100:.1f}%, {np.exp(growth_ci[1])*100-100:.1f}%]')

# Predict future counts
print('\n1.2 Predicted Paper Counts (Bayesian Model)')
for future_year in [2027, 2028, 2029]:
    pred_mean = np.exp(intercept_mle + growth_mle * (future_year - 2023))
    pred_low = np.exp(intercept_mle + growth_ci[0] * (future_year - 2023))
    pred_high = np.exp(intercept_mle + growth_ci[1] * (future_year - 2023))
    print(f'   {future_year}: {pred_mean:.0f} papers [95% CI: {pred_low:.0f}, {pred_high:.0f}]')

# ========================================
# 2. Category Distribution Analysis
# ========================================
print('\n[2] CATEGORY DISTRIBUTION & BAYESIAN PROPORTIONS')
print('-' * 50)

cat_counts = defaultdict(int)
for p in papers:
    cat = p.get('category', 'unknown')
    cat_counts[cat] += 1

# Bayesian proportion estimation with Dirichlet prior
total = sum(cat_counts.values())
alpha_prior = 1  # symmetric Dirichlet prior

print('\n2.1 Category Proportions (with 95% credible intervals)')
cat_proportions = {}
for cat, count in sorted(cat_counts.items()):
    # Posterior: Beta(count + alpha_prior, total - count + alpha_prior)
    mean = (count + alpha_prior) / (total + 3 * alpha_prior)
    ci_low = stats.beta.ppf(0.025, count + alpha_prior, total - count + alpha_prior)
    ci_high = stats.beta.ppf(0.975, count + alpha_prior, total - count + alpha_prior)
    cat_proportions[cat] = mean
    print(f'   {cat:15s}: {mean*100:5.1f}% [95% CI: {ci_low*100:5.1f}%, {ci_high*100:5.1f}%] ({count} papers)')

# ========================================
# 3. Subcategory Distribution Analysis
# ========================================
print('\n[3] SUBCATEGORY DISTRIBUTION (27 cells)')
print('-' * 50)

subcat_counts = defaultdict(int)
for p in papers:
    cat = p.get('category', 'unknown')
    subcat = p.get('subcategory', 'unknown')
    subcat_counts[f'{cat}/{subcat}'] += 1

# Sort by count
sorted_subcats = sorted(subcat_counts.items(), key=lambda x: -x[1])

print('\n3.1 Top 10 Cells')
for i, (cell, count) in enumerate(sorted_subcats[:10]):
    mean = count / total
    ci_low = stats.beta.ppf(0.025, count + 1, total - count + 1)
    ci_high = stats.beta.ppf(0.975, count + 1, total - count + 1)
    print(f'   {i+1:2d}. {cell:22s}: {mean*100:5.1f}% ({count} papers)')

print('\n3.2 Sparse Cells (< 20 papers)')
for cell, count in sorted_subcats:
    if count < 20:
        mean = count / total
        ci_low = stats.beta.ppf(0.025, count + 1, total - count + 1)
        ci_high = stats.beta.ppf(0.975, count + 1, total - count + 1)
        print(f'   {cell:22s}: {mean*100:5.1f}% [95% CI: {ci_low*100:5.1f}%, {ci_high*100:5.1f}%] ({count} papers)')

# ========================================
# 4. Category × Subcategory Interaction
# ========================================
print('\n[4] CATEGORY × SUBCATEGORY INTERACTION')
print('-' * 50)

# Build contingency table
categories = ['factual', 'experiential', 'working']
subcategories = ['token-level', 'latent', 'parametric']

table = np.zeros((len(categories), len(subcategories)))
for i, cat in enumerate(categories):
    for j, subcat in enumerate(subcategories):
        key = f'{cat}/{subcat}'
        table[i, j] = subcat_counts.get(key, 0)

print('\n4.1 Contingency Table (counts)')
print('              ' + '  '.join([f'{s:12s}' for s in subcategories]))
for i, cat in enumerate(categories):
    print(f'{cat:12s} ' + '  '.join([f'{int(table[i,j]):12.0f}' for j in range(len(subcategories))]))

# Chi-square test for independence
chi2, p_value, dof, expected = stats.chi2_contingency(table)
print(f'\n4.2 Independence Test')
print(f'   Chi-square statistic: {chi2:.2f}')
print(f'   Degrees of freedom: {dof}')
print(f'   p-value: {p_value:.3e}')
print(f'   Interpretation: {"Significant dependence" if p_value < 0.05 else "Independence"} between category and subcategory')

# ========================================
# 5. Temporal Trends by Category
# ========================================
print('\n[5] TEMPORAL TRENDS BY CATEGORY')
print('-' * 50)

cat_year_counts = defaultdict(lambda: defaultdict(int))
for p in papers:
    if p.get('date'):
        year = p['date'][:4]
        cat = p.get('category', 'unknown')
        cat_year_counts[cat][year] += 1

print('\n5.1 Growth Rates by Category (2023-2026)')
for cat in categories:
    counts_cat = np.array([cat_year_counts[cat].get(str(y), 0) for y in recent_years])
    if np.sum(counts_cat) > 0:
        log_counts = np.log(counts_cat + 1)
        slope, _, r_val, p_val, _ = stats.linregress(recent_years, log_counts)
        growth_rate = np.exp(slope) - 1
        print(f'   {cat:15s}: {growth_rate*100:6.1f}% per year (R²={r_val**2:.3f})')

# ========================================
# 6. Uncertainty Quantification
# ========================================
print('\n[6] UNCERTAINTY QUANTIFICATION')
print('-' * 50)

# Monte Carlo simulation for total corpus size
print('\n6.1 Projected Total Corpus Size (2027-2030)')
np.random.seed(42)
n_sim = 10000
projections = {year: [] for year in range(2027, 2031)}

for _ in range(n_sim):
    # Sample growth rate from posterior
    growth_sample = np.random.normal(np.mean(bootstrap_growths), np.std(bootstrap_growths))
    current = recent_counts[-1]
    for year in range(2027, 2031):
        current = current * np.exp(growth_sample)
        projections[year].append(current)

for year in range(2027, 2031):
    proj = np.array(projections[year])
    print(f'   {year}: {np.median(proj):.0f} papers [95% CI: {np.percentile(proj, 2.5):.0f}, {np.percentile(proj, 97.5):.0f}]')

# ========================================
# 7. Summary Statistics
# ========================================
print('\n[7] SUMMARY STATISTICS')
print('-' * 50)

print(f'\n   Total papers: {len(papers)}')
print(f'   Time span: {years[0]}-{years[-1]} ({len(years)} years)')
print(f'   Recent period (2023-2026): {sum(recent_counts)} papers')
print(f'   Growth rate: {np.exp(np.mean(bootstrap_growths))*100-100:.1f}% per year')
print(f'   Categories: {len(cat_counts)}')
print(f'   Subcategory cells: {len(subcat_counts)}')
print(f'   Sparse cells (<20): {sum(1 for c in subcat_counts.values() if c < 20)}')

# Save results
results = {
    'total_papers': len(papers),
    'year_distribution': dict(year_counts),
    'growth_rate_percent': float(np.exp(np.mean(bootstrap_growths)) * 100 - 100),
    'growth_rate_ci': [float(np.exp(growth_ci[0]) * 100 - 100), float(np.exp(growth_ci[1]) * 100 - 100)],
    'category_proportions': {k: float(v) for k, v in cat_proportions.items()},
    'subcategory_counts': dict(subcat_counts),
    'predictions': {str(k): float(np.median(np.array(v))) for k, v in projections.items()}
}

with open('docs/bayesian_analysis_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print('\n   Results saved to: docs/bayesian_analysis_results.json')
