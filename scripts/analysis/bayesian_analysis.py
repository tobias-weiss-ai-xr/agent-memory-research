#!/usr/bin/env python3
"""Robust Bayesian analysis for agent memory paper data."""
import yaml
import numpy as np
from collections import defaultdict
from scipy import stats, special
import json

# Load papers
with open('papers.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    papers = data['papers']

print('=' * 70)
print('ROBUST BAYESIAN ANALYSIS: AGENT MEMORY PAPER CORPUS')
print('=' * 70)

# ========================================
# 1. Basic Statistics
# ========================================
year_counts = defaultdict(int)
cat_year_counts = defaultdict(lambda: defaultdict(int))
cat_counts = defaultdict(int)
subcat_counts = defaultdict(int)

for p in papers:
    if p.get('date'):
        year = p['date'][:4]
        year_counts[year] += 1
        cat = p.get('category', 'unknown')
        cat_year_counts[cat][year] += 1
        cat_counts[cat] += 1
        subcat = p.get('subcategory', 'unknown')
        subcat_counts[f'{cat}/{subcat}'] += 1

years = np.array(sorted([int(y) for y in year_counts.keys()]))
counts = np.array([year_counts[str(y)] for y in years])

# Filter to 2023-2026 for recent analysis
recent_mask = years >= 2023
recent_years = years[recent_mask]
recent_counts = counts[recent_mask]

total_papers = len(papers)
print(f'\nTotal papers: {total_papers}')
print(f'Year range: {years[0]}-{years[-1]}')
print(f'Recent period (2023-2026): {sum(recent_counts)} papers')

# ========================================
# 2. Bayesian Growth Rate Estimation
# ========================================
print('\n' + '=' * 70)
print('[1] BAYESIAN GROWTH RATE ESTIMATION')
print('=' * 70)

# Use log-linear model with Bayesian credible intervals
log_counts = np.log(recent_counts + 1)

# Bootstrap for credible intervals
np.random.seed(42)
n_bootstrap = 5000
bootstrap_slopes = []
bootstrap_intercepts = []

for _ in range(n_bootstrap):
    # Sample years with replacement, but ensure we have variation
    idx = np.random.choice(len(recent_years), len(recent_years), replace=True)
    # If all x values are identical, use original
    if len(np.unique(recent_years[idx])) < 2:
        idx = np.arange(len(recent_years))
    slope, intercept, r_value, _, _ = stats.linregress(recent_years[idx], log_counts[idx])
    bootstrap_slopes.append(slope)
    bootstrap_intercepts.append(intercept)

bootstrap_slopes = np.array(bootstrap_slopes)
bootstrap_intercepts = np.array(bootstrap_intercepts)

# Growth rate in percentage
slope_mean = np.mean(bootstrap_slopes)
slope_ci_low = np.percentile(bootstrap_slopes, 2.5)
slope_ci_high = np.percentile(bootstrap_slopes, 97.5)

growth_rate = np.exp(slope_mean) - 1
growth_ci_low = np.exp(slope_ci_low) - 1
growth_ci_high = np.exp(slope_ci_high) - 1

print(f'\nOverall Growth Rate (2023-2026):')
print(f'  Point estimate: {growth_rate*100:.1f}% per year')
print(f'  95% CI: [{growth_ci_low*100:.1f}%, {growth_ci_high*100:.1f}%]')
print(f'  R²: {np.corrcoef(recent_years, log_counts)[0,1]**2:.3f}')

# ========================================
# 3. Category-wise Bayesian Analysis
# ========================================
print('\n' + '=' * 70)
print('[2] CATEGORY-WISE BAYESIAN ANALYSIS')
print('=' * 70)

categories = ['factual', 'experiential', 'working']
cat_results = {}

for cat in categories:
    cat_counts_arr = np.array([cat_year_counts[cat].get(str(y), 0) for y in recent_years])
    
    # Bayesian proportion estimation
    total_cat = sum(cat_counts_arr)
    alpha_prior = 1
    
    # Posterior mean and CI for proportion
    prop_mean = (total_cat + alpha_prior) / (total_papers + 3 * alpha_prior)
    prop_ci_low = stats.beta.ppf(0.025, total_cat + alpha_prior, total_papers - total_cat + alpha_prior)
    prop_ci_high = stats.beta.ppf(0.975, total_cat + alpha_prior, total_papers - total_cat + alpha_prior)
    
    # Growth rate estimation
    if total_cat > 10:
        log_cat_counts = np.log(cat_counts_arr + 1)
        slope, intercept, r_value, p_value, _ = stats.linregress(recent_years, log_cat_counts)
        
        # Bootstrap CI for growth
        cat_slopes = []
        for _ in range(1000):
            idx = np.random.choice(len(recent_years), len(recent_years), replace=True)
            if len(np.unique(recent_years[idx])) < 2:
                idx = np.arange(len(recent_years))
            s, _, _, _, _ = stats.linregress(recent_years[idx], log_cat_counts[idx])
            cat_slopes.append(s)
        cat_slopes = np.array(cat_slopes)
        
        cat_growth = np.exp(np.mean(cat_slopes)) - 1
        cat_growth_ci = [np.exp(np.percentile(cat_slopes, 2.5)) - 1,
                        np.exp(np.percentile(cat_slopes, 97.5)) - 1]
    else:
        cat_growth = 0
        cat_growth_ci = [0, 0]
        r_value = 0
    
    cat_results[cat] = {
        'total': total_cat,
        'proportion': prop_mean,
        'prop_ci': [prop_ci_low, prop_ci_high],
        'growth_rate': cat_growth,
        'growth_ci': cat_growth_ci,
        'r_squared': r_value**2
    }
    
    print(f'\n{cat.capitalize()}:')
    print(f'  Total: {total_cat} papers ({prop_mean*100:.1f}%)')
    print(f'  Proportion 95% CI: [{prop_ci_low*100:.1f}%, {prop_ci_high*100:.1f}%]')
    if total_cat > 10:
        print(f'  Growth rate: {cat_growth*100:.1f}% per year [95% CI: {cat_growth_ci[0]*100:.1f}%, {cat_growth_ci[1]*100:.1f}%]')
        print(f'  R²: {r_value**2:.3f}')

# ========================================
# 4. Change Point Detection
# ========================================
print('\n' + '=' * 70)
print('[3] BAYESIAN CHANGE POINT DETECTION')
print('=' * 70)

# Compute likelihood for each potential change point
def compute_bayesian_cp_score(data, cp_idx):
    """Compute Bayesian score for change point at cp_idx."""
    if cp_idx <= 0 or cp_idx >= len(data) - 1:
        return -np.inf
    
    before = data[:cp_idx]
    after = data[cp_idx:]
    
    # Prior on rates (Gamma(1, 1))
    alpha_prior, beta_prior = 1, 1
    
    # Posterior for before
    alpha_before = alpha_prior + sum(before)
    beta_before = beta_prior + len(before)
    mean_before = alpha_before / beta_before
    
    # Posterior for after
    alpha_after = alpha_prior + sum(after)
    beta_after = beta_prior + len(after)
    mean_after = alpha_after / beta_after
    
    # Marginal likelihood (integrated over rate)
    # For Poisson-Gamma: (beta^alpha / Gamma(alpha)) * (Gamma(sum + alpha) / (beta + n)^ (sum + alpha))
    log_marginal_before = (alpha_before * np.log(beta_before) - np.log(special.gamma(alpha_before)) +
                          np.log(special.gamma(alpha_before + sum(before))) - 
                          (alpha_before + sum(before)) * np.log(beta_before + len(before)))
    log_marginal_after = (alpha_after * np.log(beta_after) - np.log(special.gamma(alpha_after)) +
                         np.log(special.gamma(alpha_after + sum(after))) - 
                         (alpha_after + sum(after)) * np.log(beta_after + len(after)))
    
    return log_marginal_before + log_marginal_after

# Test all change points
cp_scores = []
for cp in range(1, len(counts) - 1):
    score = compute_bayesian_cp_score(counts, cp)
    cp_scores.append(score)

cp_scores = np.array(cp_scores)
cp_probs = np.exp(cp_scores - np.max(cp_scores))
cp_probs /= np.sum(cp_probs)

best_cp_idx = np.argmax(cp_probs)
best_cp_year = years[best_cp_idx + 1]  # +1 because cp is between years
cp_confidence = cp_probs[best_cp_idx]

print(f'\nMost likely change point: {best_cp_year}')
print(f'Posterior probability: {cp_confidence*100:.1f}%')

# Rate before and after
before_mask = years < best_cp_year
after_mask = years >= best_cp_year

rate_before = np.mean(counts[before_mask]) if np.any(before_mask) else 0
rate_after = np.mean(counts[after_mask]) if np.any(after_mask) else 0

print(f'Average rate before {best_cp_year}: {rate_before:.1f} papers/year')
print(f'Average rate after {best_cp_year}: {rate_after:.1f} papers/year')
print(f'Acceleration factor: {rate_after / (rate_before + 0.1):.1f}x')

# ========================================
# 5. Subcategory Analysis
# ========================================
print('\n' + '=' * 70)
print('[4] SUBCATEGORY DISTRIBUTION & SPARSE CELLS')
print('=' * 70)

# Sort by count
sorted_subcats = sorted(subcat_counts.items(), key=lambda x: -x[1])

print('\nTop 5 cells:')
for i, (cell, count) in enumerate(sorted_subcats[:5]):
    prop = count / total_papers
    ci = stats.beta.ppf([0.025, 0.975], count + 1, total_papers - count + 1)
    print(f'  {i+1}. {cell}: {count} papers ({prop*100:.1f}%, 95% CI: [{ci[0]*100:.1f}%, {ci[1]*100:.1f}%])')

print('\nSparse cells (< 20 papers):')
sparse_cells = [(cell, count) for cell, count in sorted_subcats if count < 20]
for cell, count in sparse_cells:
    prop = count / total_papers
    ci = stats.beta.ppf([0.025, 0.975], count + 1, total_papers - count + 1)
    print(f'  {cell}: {count} papers ({prop*100:.1f}%, 95% CI: [{ci[0]*100:.1f}%, {ci[1]*100:.1f}%])')

# ========================================
# 6. Predictions
# ========================================
print('\n' + '=' * 70)
print('[5] BAYESIAN PREDICTIONS')
print('=' * 70)

# Predict future counts using posterior predictive distribution
print('\nPredicted paper counts (posterior predictive):')
for future_year in [2027, 2028, 2029, 2030]:
    # Sample from posterior
    pred_samples = []
    for _ in range(1000):
        slope_s = np.random.choice(bootstrap_slopes)
        intercept_s = np.random.choice(bootstrap_intercepts)
        rate = np.exp(intercept_s + slope_s * (future_year - 2023))
        pred_samples.append(np.random.poisson(rate))
    
    pred_samples = np.array(pred_samples)
    pred_median = np.median(pred_samples)
    pred_ci = [np.percentile(pred_samples, 2.5), np.percentile(pred_samples, 97.5)]
    
    print(f'  {future_year}: {pred_median:.0f} papers [95% CI: {pred_ci[0]:.0f}, {pred_ci[1]:.0f}]')

# ========================================
# 7. Save Results
# ========================================
results = {
    'total_papers': total_papers,
    'year_range': [int(years[0]), int(years[-1])],
    'overall_growth': {
        'rate_percent': float(growth_rate * 100),
        'ci_low_percent': float(growth_ci_low * 100),
        'ci_high_percent': float(growth_ci_high * 100),
        'r_squared': float(np.corrcoef(recent_years, log_counts)[0,1]**2)
    },
    'category_results': {cat: {
        'total': int(v['total']),
        'proportion': float(v['proportion']),
        'prop_ci': [float(v['prop_ci'][0]), float(v['prop_ci'][1])],
        'growth_rate_percent': float(v['growth_rate'] * 100),
        'growth_ci_percent': [float(v['growth_ci'][0] * 100), float(v['growth_ci'][1] * 100)],
        'r_squared': float(v['r_squared'])
    } for cat, v in cat_results.items()},
    'change_point': {
        'year': int(best_cp_year),
        'confidence': float(cp_confidence),
        'rate_before': float(rate_before),
        'rate_after': float(rate_after),
        'acceleration_factor': float(rate_after / (rate_before + 0.1))
    },
    'sparse_cells': [{'cell': cell, 'count': count, 'proportion': count/total_papers} 
                     for cell, count in sparse_cells],
    'predictions': {},
}

with open('docs/bayesian_analysis_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

# Add predictions
for year in [2027, 2028, 2029, 2030]:
    pred_samples = []
    for _ in range(1000):
        slope_s = np.random.choice(bootstrap_slopes)
        intercept_s = np.random.choice(bootstrap_intercepts)
        rate = np.exp(intercept_s + slope_s * (year - 2023))
        pred_samples.append(np.random.poisson(rate))
    results['predictions'][str(year)] = float(np.median(pred_samples))

# Rewrite with predictions
with open('docs/bayesian_analysis_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print('\nResults saved to: docs/bayesian_analysis_results.json')

print('\n' + '=' * 70)
print('ANALYSIS COMPLETE')
print('=' * 70)
