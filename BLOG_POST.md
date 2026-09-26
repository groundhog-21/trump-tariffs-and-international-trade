# Did Trump's Tariffs Slow US Imports? What 19 Months Can Tell Us

![Illustration of a container ship arriving at a port with cranes and stacked containers.](reports/figures/trade-blog-header.png)

*Illustration generated with OpenAI's image-generation tool; not a photograph of a specific port.*

Did Trump's second-term tariffs reduce the goods entering the United States? It sounds like a straightforward question: look at imports before and after, and compare.

The data tell a less decisive story. **Import growth was lower on average during the second term, but this analysis did not find convincing evidence of a reduction attributable to tariffs.**

## What I wanted to find out

The central question was whether imports were lower than they would have been without the tariffs. To explore it, I asked two more specific questions:

1. Was import growth lower during Trump's second term than in the preceding period?
2. Were import values below their long-term upward trend?

I used US Census Bureau monthly data on goods imports. Services were excluded. The analysis covers January 1993 through July 2026: **403 months in total, but only 19 during the second term**.

I counted January 2025 as the start of the second-term period, including the whole month. That comparison includes months before the April tariff announcement, allowing room for businesses to bring purchases forward in anticipation. The earlier period includes Trump's first term.

## Growth slowed, but the evidence is uncertain

To compare growth, I measured each month's imports against the same month one year earlier.

| Period | Months observed | Average year-over-year import growth |
| --- | ---: | ---: |
| January 1993-December 2024 | 384 | 6.50% |
| January 2025-July 2026 | 19 | 4.13% |
| Difference | | **-2.37 percentage points** |

*Source: calculations from the project's US Census Bureau data extract. These are averages of monthly year-over-year growth rates.*

Growth was lower by 2.37 percentage points. However, the uncertainty around that difference was too large to confidently distinguish it from ordinary variation.

Slower growth also does not mean imports fell. A positive growth rate means imports were higher than a year earlier; they were simply increasing more slowly on average.

## Import values tell another part of the story

I also compared monthly import values with a straight-line historical trend. On that benchmark, second-term imports were approximately **$23.9 billion per month above the fitted trend**, rather than below it.

That result does not show that tariffs increased imports. It shows why the benchmark matters: imports can grow more slowly than their historical average while remaining above a projected trend in dollar values.

The two comparisons therefore offer no consistent evidence that imports were lower during the second term.

## What can we conclude?

**This analysis does not provide robust evidence that Trump's second-term tariffs reduced US goods imports. It also does not establish that tariffs had no effect.**

Nineteen months is a short window, and neighboring months do not provide wholly independent evidence. Prices, exchange rates, demand, and other policies can influence the dollar value of imports. This study does not separate those influences from tariffs, and it measures spending on imported goods rather than physical quantities.

Businesses might also import more before tariffs and less afterward. Averaging the whole period can blur that pattern; this analysis does not establish whether that happened.

For now, the findings are preliminary. More observations will allow us to revisit the question, although additional data alone will not resolve every question about cause and effect.

## Data and further reading

- Data provider: [US Census Bureau, International Trade](https://www.census.gov/foreign-trade/index.html). The local extract contains observations through July 2026 and states an update date of September 3, 2026.
- [Project overview and reproduction instructions](README.md).
- [Data preparation notebook](notebooks/data_understanding_and_preparation.ipynb).
- [Models, statistical results, and charts](notebooks/modeling_and_evaluation.ipynb).

*Created as part of my Udacity Data Science Nanodegree studies, with OpenAI Codex assistance for coding, writing, and discussion of methods.*
