# NZ Accountant Toolkit

An open-source practical toolkit for New Zealand accountants, tax agents, bookkeepers, trustees, and small business advisors.

NZ Accountant Toolkit collects reusable workpaper designs, calculator specifications, review checklists, reconciliation workflows, and standard operating procedures for common New Zealand accounting and tax engagements.

The project is designed for practitioners first. It documents how each tool should be used in real client work, what information is required, what assumptions must be reviewed, and where professional judgement is still needed.

## Features

- FIF Calculator design covering FDR and CV comparison workflows.
- Working Python helper for simple FIF FDR and CV comparison.
- Quick Sale Calculator specification for taxable property disposal review.
- Working Python helper for draft quick sale adjustment calculation.
- GST Reconciliation Template design for GST return preparation and review.
- Working Python helper for GST variance checks.
- GST Review Checklist for common GST risk areas.
- Property Development Cost Tracker for land, construction, holding, and sale costs.
- Shareholder Current Account Tracker for advances, repayments, dividends, salaries, and overdrawn balances.
- Xero Bank Reconciliation SOP for bookkeepers and review teams.
- Year-End Workpaper Checklist for annual accounts and income tax engagements.
- Trust Accounting notes and example workpaper prompts.
- Starter GitHub issues, discussions topics, roadmap, and release notes.

## Repository Structure

```text
NZ Accountant Toolkit/
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── SECURITY.md
├── GOVERNANCE.md
├── MAINTAINERS.md
├── docs/
├── src/
├── tests/
├── templates/
├── tools/
├── examples/
├── checklists/
├── xero/
├── property-development/
└── .github/
```

## Screenshots

Screenshots will be added as the Excel templates and calculator prototypes are converted into working assets.

| Area | Placeholder |
| --- | --- |
| FIF Calculator | `docs/assets/fif-calculator-preview.png` |
| GST Reconciliation | `docs/assets/gst-reconciliation-preview.png` |
| Property Development Tracker | `docs/assets/property-development-preview.png` |
| Shareholder Current Account | `docs/assets/shareholder-current-account-preview.png` |

## Installation

This first release includes documentation, template specifications, and a small Python calculator layer.

To use the documentation and templates:

1. Clone or download the repository.
2. Open the relevant documentation file for the task.
3. Build the spreadsheet, checklist, or workpaper using the specifications provided.
4. Adapt the example assumptions to the client file.
5. Retain evidence, reviewer notes, and tax position sign-off in your normal practice management system.

To run the Python helpers locally:

```bash
python -m pip install -e .
nz-accountant-toolkit fif --opening 80000 --closing 92000 --purchases 10000 --dividends 1600
nz-accountant-toolkit gst-variance --accounting 12450 --filed 12300
nz-accountant-toolkit quick-sale --sale-price 900000 --purchase-price 760000 --acquisition-costs 7500 --improvements 48000 --sale-costs 22000
```

To run tests:

```bash
python -m pip install pytest
pytest
```

On Windows, use `py -m pip ...` and `py -m pytest` if `python` is not available.

## Usage Examples

### FIF Review

Use the FIF Calculator specification when a New Zealand tax resident client holds overseas shares, managed funds, or exchange traded funds and may be subject to the foreign investment fund rules.

The template design supports:

- Opening market value.
- Closing market value.
- Purchases and sales during the year.
- Dividends received.
- FDR method at 5 percent.
- CV method based on actual movement in value.
- Method comparison and reviewer sign-off.

### GST Reconciliation

Use the GST Reconciliation Template to compare:

- GST return periods.
- Xero GST reports.
- General ledger GST control accounts.
- Inland Revenue filing and payment history.
- Adjustments for mixed-use, private use, non-deductible items, and timing differences.

### Quick Sale Adjustment

Use the Quick Sale Calculator specification when reviewing a land or property transaction that may be taxable under New Zealand land rules, including bright-line, subdivision, dealer, developer, builder, or associated person considerations.

### Shareholder Loans

Use the Shareholder Current Account Tracker to monitor advances to shareholders, repayments, dividends, salaries, PAYE items, imputation credits, interest charges, and possible overdrawn current account risks.

## Roadmap

### Phase 1: Excel Templates

- Convert specifications into downloadable Excel workbooks.
- Add sample data and reviewer notes.
- Add template version control and change logs.

### Phase 2: Python Calculators

- Build command-line calculators for FIF, quick sale, GST checks, and shareholder current accounts.
- Add tests using realistic New Zealand accounting scenarios.
- Provide simple CSV input examples.

### Phase 3: Web Application

- Build a browser-based toolkit for firms and small business advisors.
- Add guided workflows, PDF outputs, and internal review notes.
- Include non-technical setup for accountants.

### Phase 4: Xero Integration

- Explore secure Xero API integration.
- Pull trial balance, GST control account, and bank reconciliation data.
- Create reconciliation exception reports.

## Contributing

Contributions are welcome from accountants, tax agents, bookkeepers, software developers, educators, and students.

Good contributions include:

- Practical template improvements.
- Better New Zealand tax examples.
- Review checklists.
- Plain-English explanations.
- Calculator test cases.
- Corrections to assumptions or terminology.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Project Health

- [Governance](GOVERNANCE.md)
- [Maintainers](MAINTAINERS.md)
- [Security Policy](SECURITY.md)
- [Privacy Policy](PRIVACY.md)
- [Support](SUPPORT.md)
- [Maintenance Plan](docs/maintenance-plan.md)
- [Release Checklist](docs/release-checklist.md)

## Disclaimer

This project provides general information, template designs, and workflow guidance only. It is not tax advice, legal advice, financial advice, or a substitute for professional judgement.

New Zealand tax law, Inland Revenue guidance, accounting standards, and client facts change over time. Practitioners must verify all calculations, assumptions, and tax positions before relying on any template or tool.

Use at your own risk.
