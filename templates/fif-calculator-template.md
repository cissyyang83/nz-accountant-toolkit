# FIF Calculator Template Specification

## Purpose

Design an Excel workbook to help New Zealand tax practitioners compare Foreign Investment Fund income under the fair dividend rate and comparative value methods.

## Intended Use

Use this template where a New Zealand tax resident client holds overseas shares, ETFs, managed funds, or other investments that may be subject to FIF rules.

## Workbook Sheets

| Sheet | Purpose |
| --- | --- |
| Cover | Client details, tax year, preparer, reviewer, disclaimer |
| Instructions | Plain-English usage notes and limitations |
| Investment Register | List of overseas holdings |
| Market Values | Opening and closing market values |
| Transactions | Purchases, sales, dividends, foreign tax credits |
| FDR Calculation | Fair dividend rate calculation |
| CV Calculation | Comparative value calculation |
| Method Comparison | Summary of FDR versus CV |
| Review Notes | Assumptions, exemptions, reviewer sign-off |

## Key Fields

| Field | Description |
| --- | --- |
| Client name | Taxpayer or entity being reviewed |
| IRD number | Optional internal reference |
| Tax year | Year ended 31 March |
| Investment name | Security or fund name |
| Country | Jurisdiction of investment |
| Currency | Original investment currency |
| Opening market value | Value at start of income year |
| Closing market value | Value at end of income year |
| Purchases | Additions during the year |
| Sales proceeds | Disposal proceeds during the year |
| Dividends | Cash or reinvested distributions |
| Foreign tax deducted | Withholding tax or similar |

## Calculation Logic

### FDR

Suggested design:

```text
FDR income = Opening market value x 5%
```

Reviewer must confirm that FDR is available for the investment and that no exemption, quick sale rule, or special method applies.

### CV

Suggested design:

```text
CV income = Closing market value + sales proceeds + dividends - opening market value - purchases
```

Negative results should be clearly highlighted and reviewed.

## Review Checks

- Has the client exceeded any relevant de minimis threshold?
- Are Australian listed shares excluded where applicable?
- Are all currencies converted using an acceptable method?
- Are dividends and tax credits supported by broker statements?
- Has the practitioner considered whether FDR or CV is permitted?
- Has the final method selection been documented?

## Example Scenario

Client holds a United States ETF.

| Item | Amount |
| --- | ---: |
| Opening market value | NZD 80,000 |
| Closing market value | NZD 92,000 |
| Purchases | NZD 10,000 |
| Sales proceeds | NZD 0 |
| Dividends | NZD 1,600 |

FDR income design result:

```text
80,000 x 5% = 4,000
```

CV income design result:

```text
92,000 + 0 + 1,600 - 80,000 - 10,000 = 3,600
```

Reviewer notes should explain the selected method and support for values.

