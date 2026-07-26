#!/usr/bin/env python3
"""Bayesian analysis of agent memory paper data."""
import yaml
import json
import numpy as np
from collections import defaultdict
from scipy import stats

# Load papers
with open('papers.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    papers = data['papers']

print(f'Total papers: {len(papers)}')

# Count by year
year_counts = defaultdict(int)
for p in papers:
    if p.get('date'):
        year = p['date'][:4]
        year_counts[year] += 1

print('\n=== Year Distribution ===')
for year in sorted(year_counts.keys()):
    print(f'  {year}: {year_counts[year]}')

# Count by category/subcategory
cat_counts = defaultdict(int)
for p in papers:
    cat = p.get('category', 'unknown')
    subcat = p.get('subcategory', 'unknown')
    cat_counts[f'{cat}/{subcat}'] += 1

print('\n=== Category/Subcategory Distribution ===')
for k in sorted(cat_counts.keys()):
    print(f'  {k}: {cat_counts[k]}')

# Bayesian Analysis: Publication Rate Growth
print('\n=== Bayesian Analysis: Publication Rate Growth ===')

# Convert to numpy arrays
years = np.array(sorted([int(y) for y in year_counts.keys()]))
counts = np.array([year_counts[str(y)] for y in years])

# Simple Poisson regression with Bayesian inference
# Using conjugate prior (Gamma prior on rate)
alpha_prior = 1  # shape
beta_prior = 1   # rate

# Posterior parameters for each year
print('\nYear-by-year growth analysis:')
for i, (year, count) in enumerate(zip(years, counts)):
    alpha_post = alpha_prior + count
    beta_post = beta_prior + 1
    
    # Posterior mean and credible interval
    posterior_mean = alpha_post / beta_post
    credible_low = stats.gamma.ppf(0.025, alpha_post, scale=1/beta_post)
    credible_high = stats.gamma.ppf(0.975, alpha_post, scale=1/beta_post)
    
    print(f'  {year}: count={count}, posterior_mean={posterior_mean:.2f}, 95% CI=[{credible_low:.2f}, {credible_high:.2f}]')

# Growth rate estimation
print('\n=== Growth Rate Analysis ===')
if len(years) >= 2:
    # Log-linear growth model
    log_counts = np.log(counts + 1)
    slope, intercept, r_value, p_value, std_err = stats.linregress(years, log_counts)
    
    print(f'  Log-linear growth rate: {slope:.3f} papers/year (log scale)')
    print(f'  R-squared: {r_value**2:.3f}')
    print(f'  p-value: {p_value:.3e}')
    
    # Exponential growth rate
    growth_rate = np.exp(slope) - 1
    print(f'  Exponential growth rate: {growth_rate*100:.1f}% per year')
    
    # Bayesian credible interval for growth rate
    # Using bootstrap
    bootstrap_slopes = []
    np.random.seed(42)
    for _ in range(1000):
        idx = np.random.choice(len(years), len(years), replace=True)
        slope_b, _, _, _, _ = stats.linregress(years[idx], log_counts[idx])
        bootstrap_slopes.append(slope_b)
    
    slope_ci_low = np.percentile(bootstrap_slopes, 2.5)
    slope_ci_high = np.percentile(bootstrap_slopes, 97.5)
    
    print(f'  95% CI for growth rate: [{slope_ci_low:.3f}, {slope_ci_high:.3f}] (log scale)')

# Category-wise growth
print('\n=== Category-wise Bayesian Analysis ===')
cat_year_counts = defaultdict(lambda: defaultdict(int))
for p in papers:
    if p.get('date'):
        year = p['date'][:4]
        cat = p.get('category', 'unknown')
        cat_year_counts[cat][year] += 1

for cat in sorted(cat_year_counts.keys()):
    cat_counts_list = [cat_year_counts[cat].get(str(y), 0) for y in years]
    total = sum(cat_counts_list)
    print(f'  {cat}: {total} papers ({total/len(papers)*100:.1f}%)')
