# Trump Tariffs and International Trade

An exploratory analysis of US goods imports following the CRISP-DM process.

**Read the blog post on Medium:** [Did Trump's Tariffs Slow US Imports? What 19 Months Can Tell Us](https://medium.com/@agbrowne/did-trumps-tariffs-slow-us-imports-what-19-months-can-tell-us-a8e3fa2de37a)

## Research question

Did Trump's second-term tariffs reduce US goods imports?

The models compare import growth or import levels during the second term with earlier observations. They describe associations; the presidential indicator does not isolate tariff effects.

## Data source and scope

- **Publisher:** US Census Bureau, [International Trade](https://www.census.gov/foreign-trade/index.html).
- **Included source snapshot:** [`data/raw/FTD-mf.csv`](data/raw/FTD-mf.csv), a multi-section CSV containing metadata and observations. No separate data download is required.
- **Series selected:** US goods only, balance-of-payments basis (`cat_idx = 2`, `geo_idx = 1`, `is_adj = 0`). Goods and services combined are excluded.
- **Measures:** imports, exports, and trade balance, in millions of US dollars. Values are not inflation-adjusted.
- **Raw coverage:** January 1992-July 2026, with 415 complete monthly observations for these measures. The file states an update date of September 3, 2026.
- **Analysis sample:** January 1993-July 2026, with 403 complete observations after calculating year-over-year changes.
- **Second-term indicator:** 1 for January 2025-July 2026 (19 months), and 0 for January 1993-December 2024 (384 months, including Trump's first term). January 2025 is included in full.

The exact export URL and download date have not yet been recorded. The source's update date is not the download date. Census estimates may be revised.

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

Run code cells from top to bottom, using the project root or `notebooks` as the working directory.

1. [Business understanding](notebooks/business_understanding.ipynb): research objective, scope, and hypotheses.
2. [Data understanding and preparation](notebooks/data_understanding_and_preparation.ipynb): reads the source, selects goods-only records, explores trends, creates the indicator and YoY variables, and saves `data/processed/analysis_data.csv`.
3. [Modeling and evaluation](notebooks/modeling_and_evaluation.ipynb): loads the prepared data, fits the regressions, and plots actual versus fitted values.
4. [Deployment](notebooks/deployment.ipynb): records the final preliminary conclusion.

Run the preparation notebook before the modeling notebook. The saved CSV lets each notebook use its own kernel session.

## Models and findings

The modeling notebook retains two OLS specifications. Both use the same 403 observations and HAC standard errors with 12 lags and a small-sample correction. The one-sided alternative is a negative second-term coefficient.

| Model | Estimated second-term difference | One-sided p-value for a reduction |
| --- | --- | --- |
| YoY import growth, intercept and second-term dummy | -2.37 percentage points | 0.278 |
| Import levels, linear monthly time trend and second-term dummy | +$23.89 billion per month relative to the fitted trend | 0.998 |

In the growth model, average YoY growth was 6.50% before January 2025 and 4.13% during the second term. The difference was not statistically significant. In the levels model, the positive difference was statistically significant on a two-sided test (p = 0.004), conditional on that specification.

### Descriptive finding: goods trade balance

The average monthly goods trade deficit was **$54.30 billion** in January 1993–December 2024 and **$100.57 billion** in January 2025–July 2026, a **$46.27 billion larger average deficit per month** during the second term. This answers Question 3 using a descriptive comparison, without a significance test. Values are not inflation-adjusted, and the comparison does not control for the long-term scale of trade, exports, or other economic influences; it does not identify a causal tariff effect.

**Conclusion:** The analysis does not provide robust evidence that Trump's second-term tariffs reduced imports. Results vary by specification, and the short second-term observation window limits inference. These findings are preliminary and do not establish either the presence or absence of a causal tariff effect.

## Libraries used

- pandas and NumPy: data preparation and numerical operations.
- Matplotlib: charts of trade trends and model fits.
- statsmodels: OLS regression with HAC standard errors.
- SciPy: one-sided p-values.
- Jupyter and ipykernel: notebook execution.

Seaborn is included in the environment but is not used in the current analysis.

## Supporting files

- `requirements.txt`: Python dependencies.
- `.gitignore`: excludes virtual environments, local datasets, and temporary files.
- `data/README.md`: source snapshot provenance, coverage, and preparation details.
- `src/`: reserved for reusable Python code.
- `reports/figures/`: reserved for exported charts.

## Limitations

- Only 19 second-term months are available, and monthly observations are dependent.
- The indicator measures presidential tenure, not tariff rates, coverage, or implementation dates. Anticipatory importing and later declines may offset each other in period averages.
- Lower import growth is different from lower import levels. Dollar values also reflect prices, exchange rates, and demand.
- The levels model assumes a single linear trend and does not include seasonal controls. HAC standard errors do not correct model misspecification.
- Aggregate national data conceal country and product differences. Other policies and economic changes are not controlled for.
- Model exploration and the directional hypothesis were informed by earlier results; the tests should be treated as exploratory.

Preserve the notebooks and source snapshot, and revisit the analysis as additional observations become available.

## Acknowledgments

Trade data were provided by the US Census Bureau.
This project was developed as part of my Udacity Data Science
Nanodegree studies, with assistance from OpenAI Codex for coding,
documentation, and discussion of statistical methods.
