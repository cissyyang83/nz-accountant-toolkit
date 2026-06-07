# Quick Sale Calculator Template Specification

## Purpose

Design an Excel workbook for reviewing whether a property disposal may produce taxable income and calculating a practical quick sale adjustment for workpaper purposes.

## Intended Use

Use this template for New Zealand land and property transactions where taxability needs to be reviewed, including residential property sales, subdivisions, developments, associated person transactions, and short ownership periods.

## Workbook Sheets

| Sheet | Purpose |
| --- | --- |
| Cover | Client, property, tax year, preparer, reviewer |
| Property Facts | Acquisition, disposal, use, intention, parties |
| Taxability Review | Bright-line, developer, dealer, builder, subdivision prompts |
| Cost Base | Purchase price, legal costs, improvements, selling costs |
| Proceeds | Sale price and settlement adjustments |
| Adjustment Calculation | Gain or loss calculation |
| GST Review | GST registration, taxable activity, zero-rating prompts |
| Review Sign-Off | Conclusion and evidence checklist |

## Key Fields

- Property address.
- Acquisition date.
- Disposal date.
- Settlement dates.
- Purchase price.
- Sale price.
- Legal fees.
- Agent commission.
- Capital improvements.
- Holding costs.
- Interest treatment.
- GST inclusive or exclusive status.
- Use of property.
- Associated persons.
- Development or subdivision activity.

## Calculation Logic

```text
Taxable adjustment = Sale proceeds - deductible cost base
```

The workbook should separately show:

- Accounting gain or loss.
- Taxable adjustment.
- Non-deductible or capital items.
- GST impact where relevant.

## Review Prompts

- Was the client a dealer, developer, or builder?
- Was there an intention or purpose of resale?
- Was the property subject to bright-line rules?
- Was the main home exclusion considered?
- Were any associated person rules relevant?
- Was there subdivision or development work?
- Was GST zero-rating considered for land transactions?

## Example Scenario

Client sells a residential property within a short ownership period.

| Item | Amount |
| --- | ---: |
| Sale price | NZD 900,000 |
| Purchase price | NZD 760,000 |
| Legal and acquisition costs | NZD 7,500 |
| Improvement costs | NZD 48,000 |
| Agent and sale costs | NZD 22,000 |

Draft adjustment:

```text
900,000 - 760,000 - 7,500 - 48,000 - 22,000 = 62,500
```

Reviewer must confirm taxability before treating the amount as taxable income.

