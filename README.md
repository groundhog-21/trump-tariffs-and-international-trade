# Trump Tariffs and International Trade

An exploratory analysis of US goods import growth, import levels, and the trade balance during Trump's second term, following the CRISP-DM process.

**Read the blog post on Medium:** [Did Trump's Tariffs Slow US Imports? What 19 Months Can Tell Us](https://medium.com/@agbrowne/did-trumps-tariffs-slow-us-imports-what-19-months-can-tell-us-a8e3fa2de37a)

## Research objective and questions

Investigate whether the data support the proposition that Trump's second-term tariffs reduced US goods imports, and describe how the goods trade balance differed between periods.

1. **Import growth:** Was average year-over-year import growth lower during Trump's second term than in the preceding period?
2. **Import levels:** Were monthly import values lower during the second term after accounting for their long-term linear trend?
3. **Trade balance:** How did the average monthly US goods trade balance differ between the second term and the preceding period?

Questions 1 and 2 use regressions; Question 3 uses a descriptive comparison of period averages. These analyses describe associations and observed differences. The presidential indicator does not isolate tariff effects or establish what imports would have been without tariffs.

## Data source and scope

- **Publisher:** US Census Bureau, [International Trade](https://www.census.gov/foreign-trade/index.html).
- **Included source snapshot:** [`data/raw/FTD-mf.csv`](data/raw/FTD-mf.csv), a multi-section CSV containing metadata and observations. No separate data download is required.
- **Series selected:** US goods only, balance-of-payments basis (`cat_idx = 2`, `geo_idx = 1`, `is_adj = 0`). Goods and services combined are excluded.
- **Measures:** imports, exports, and trade balance, in millions of US dollars. Values are not inflation-adjusted.
- **Raw coverage:** January 1992-July 2026, with 415 complete monthly observations for these measures. The file states an update date of September 3, 2026.
- **Analysis sample:** January 1993-July 2026, with 403 complete observations after calculating year-over-year changes.
- **Second-term indicator:** 1 for January 2025-July 2026 (19 months), and 0 for January 1993-December 2024 (384 months, including Trump's first term). January 2025 is included in full.

The exact export URL and download date have not yet been recorded. The source's update date is not the download date. Census estimates may be revised.

## Data preparation decisions

The [preparation notebook](notebooks/data_understanding_and_preparation.ipynb) reports missing counts and percentages before exclusions, checks numeric conversions and date joins, and checks for absent calendar months. All **415 selected source months are complete**: no source measurements are dropped or imputed. Unexpected missing measurements stop execution for investigation.

The first **12 months (January–December 1992; 2.89% of the source sample)** have undefined year-over-year measures because the preceding year is unavailable. These months are excluded rather than filled with invented growth values. This removes 12 of 396 earlier-period months and none of the 19 second-term months. All three questions use the resulting 403-month sample for comparability, although the levels and balance analyses could use 1992.

A sensitivity check in the preparation notebook compares the trade-balance result across these sample windows. The average deficit widens by **$47.67 billion per month** using all 415 months and by **$46.27 billion** using the common sample. The direction is unchanged, but the baseline affects the magnitude. This check does not establish that the import-level regression is insensitive to its sample window.

Source category codes select and reshape the series; they are not treated as continuous regression predictors. The second-term category uses one **0/1 indicator**, with the earlier period as the reference group and an intercept in each regression. A second dummy would be redundant. The notebook documents these choices and distinguishes the period indicator from tariff exposure.

## Setup

Use Python 3.12. From the project root, run these commands in PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If the project's Python 3.12 environment already exists, run only the installation command. Open the project folder in VS Code, open a notebook, and select `.venv` as its Python kernel. VS Code's Python and Jupyter extensions are required for this workflow.

Use the included `data/raw/FTD-mf.csv` snapshot to reproduce the reported results. The preparation notebook reads its named sections, including `TIME PERIODS` and `DATA`. See [data documentation](data/README.md) for provenance and preparation details.

The repository includes the source CSV and the data directories. Run the preparation notebook to generate `data/processed/analysis_data.csv`, then run the modeling notebook. Generated datasets and other raw files remain excluded from Git. Dependencies are currently unpinned.

## Notebook order

Across the four notebooks, explicitly numbered headings identify the six CRISP-DM stages: **1. Business Understanding**, **2. Data Understanding**, **3. Data Preparation**, **4. Modeling**, **5. Evaluation**, and **6. Deployment**. The business-understanding notebook includes a stage-by-stage navigation map.

Run code cells from top to bottom, using the project root or `notebooks` as the working directory.

1. [Business understanding](notebooks/business_understanding.ipynb): the three investigative questions, scope, regression hypotheses, and descriptive comparison.
2. [Data understanding and preparation](notebooks/data_understanding_and_preparation.ipynb): covers stages 2–3: gathers and assesses the source, audits missingness, selects goods-only records, visualizes trends, explains categorical encoding, constructs YoY variables, checks sample sensitivity, and saves `data/processed/analysis_data.csv`.
3. [Modeling and evaluation](notebooks/modeling_and_evaluation.ipynb): covers stages 4–5: fits the two regressions in Modeling, then presents question-by-question charts, the descriptive trade-balance table, and interpretations in Evaluation. Shared functions handle regression fitting and plotting.
4. [Deployment](notebooks/deployment.ipynb): covers stage 6: summarizes all three answers and limitations, and links to the blog for communication to stakeholders.

Run the preparation notebook before the modeling notebook. The saved CSV lets each notebook use its own kernel session.

## Blog visuals and reproduction

The [repository blog post](BLOG_POST.md) pairs each business question with a hypothesis or descriptive expectation, a labeled visual, and an explanation of what the evidence supports.

| Question | Supporting chart |
| --- | --- |
| Q1: Import growth | [Average year-over-year growth by period](reports/figures/q1-import-growth.png), with uncertainty for the difference stated in the chart note. |
| Q2: Import levels | [Estimated second-term difference and 95% confidence interval](reports/figures/q2-import-levels.png), relative to the fitted linear trend. |
| Q3: Trade balance | [Average monthly balance by period](reports/figures/q3-trade-balance.png), shown as signed values; this comparison is descriptive. |

After running the preparation notebook, regenerate the three PNG figures from the project root:

```powershell
.\.venv\Scripts\python.exe src/create_blog_figures.py
```

The script reads `data/processed/analysis_data.csv`, refits the import-level model for its confidence interval, and writes the images to `reports/figures/`. It is designed for the included 403-month snapshot: some annotations and period labels are fixed to this analysis and must be reviewed if the data change.

`BLOG_POST.md` and its charts are the repository version of the article. Changes to these files do not automatically update the Medium article; its text and images must be updated separately.

## Analysis and findings

All three comparisons use the same 403 complete monthly observations. For Questions 1 and 2, OLS regressions use HAC standard errors with 12 monthly lags and a small-sample correction. Each tests a negative second-term coefficient against a null of a nonnegative coefficient. Question 3 compares average monthly trade balances without a significance test.

### Questions 1 and 2: Import growth and levels

| Question and model | Estimated second-term difference | One-sided p-value for a reduction |
| --- | --- | --- |
| Q1: YoY import growth, intercept and second-term dummy | -2.37 percentage points | 0.278 |
| Q2: Import levels, linear monthly time trend and second-term dummy | +$23.89 billion per month relative to the fitted trend | 0.998 |

In the growth model, average YoY growth was 6.50% before January 2025 and 4.13% during the second term. The difference was not statistically significant. In the levels model, the positive difference was statistically significant on a two-sided test (p = 0.004), conditional on that specification.

### Question 3: Average monthly goods trade balance

The average monthly goods trade deficit was **$54.30 billion** in January 1993–December 2024 and **$100.57 billion** in January 2025–July 2026, a **$46.27 billion larger average deficit per month** during the second term. This answers Question 3 using a descriptive comparison, without a significance test. Values are not inflation-adjusted, and the comparison does not control for the long-term scale of trade, exports, or other economic influences; it does not identify a causal tariff effect.

**Conclusion:** Import growth was lower on average but not significantly so; import levels were above the fitted linear trend; and the average nominal goods deficit was larger. These comparisons address different outcomes and do not provide robust evidence that Trump's second-term tariffs reduced imports. The short second-term observation window limits inference, and none of these findings establishes a causal tariff effect or proves that tariffs had no effect.

## Libraries used

- pandas and NumPy: data preparation and numerical operations.
- Matplotlib: charts of trade trends, model fits, and the three blog findings.
- statsmodels: OLS regression with HAC standard errors.
- SciPy: one-sided p-values.
- Jupyter and ipykernel: notebook execution.

Seaborn is included in the environment but is not used in the current analysis.

## Supporting files

- [`BLOG_POST.md`](BLOG_POST.md): repository copy of the nontechnical article, including all three questions, supporting charts, and interpretations.
- `data/raw/FTD-mf.csv`: original Census source snapshot used in the analysis.
- `data/processed/analysis_data.csv`: generated analysis table, recreated by the preparation notebook and not tracked in Git.
- `requirements.txt`: Python dependencies.
- `.gitignore`: excludes virtual environments, generated datasets, other raw files, and temporary files; explicitly retains the source snapshot `data/raw/FTD-mf.csv`.
- `data/README.md`: source snapshot provenance, coverage, and preparation details.
- `src/create_blog_figures.py`: recreates the three question-specific blog charts from the prepared data. Run `.\.venv\Scripts\python.exe src/create_blog_figures.py` after the preparation notebook.
- `reports/figures/`: contains the blog header illustration, import-growth table image, and three question-specific charts.

## Limitations

- Only 19 second-term months are available, and monthly observations are dependent.
- The indicator measures presidential tenure, not tariff rates, coverage, or implementation dates. Anticipatory importing and later declines may offset each other in period averages.
- Lower import growth is different from lower import levels. Dollar values are not inflation-adjusted and also reflect exchange rates and demand.
- The descriptive trade-balance comparison contrasts 19 recent months with 384 earlier months without controlling for the increasing scale of trade or changes in exports. A larger nominal deficit alone does not establish a tariff effect.
- The levels model assumes a single linear trend and does not include seasonal controls. HAC standard errors do not correct model misspecification.
- Aggregate national data conceal country and product differences. Other policies and economic changes are not controlled for.
- Model exploration and the directional hypothesis were informed by earlier results; the tests should be treated as exploratory.

Preserve the notebooks and source snapshot, and revisit the analysis as additional observations become available.

## Acknowledgments

This project was developed as part of my Udacity Data Science
Nanodegree studies. 

Trade data were provided by the US Census Bureau. 

**AI assistance disclosure:** I used OpenAI’s ChatGPT/Codex to support concept development, research-question refinement, coding and debugging, statistical analysis and interpretation, validation, and preparation of documentation and blog content. AI assistance also supported visualization creation, including the generated header illustration. I reviewed and edited the resulting work and take responsibility for the final submission and its conclusions.
