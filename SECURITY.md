# Security Policy

## Supported Versions

NZ Accountant Toolkit is in an early alpha stage.

| Version | Supported |
| --- | --- |
| v0.1.x | Yes |

## Reporting Security Issues

If you find a security or privacy issue, do not post confidential details in a public issue.

Examples include:

- Accidental client-identifiable information.
- Unsafe handling of financial data.
- Insecure future Xero integration design.
- Formula or calculator behaviour that could materially mislead users.

Report the issue privately to the maintainer where a private contact channel is available. If no private channel is available, open a public issue with a general description only and omit sensitive details.

## Data Handling

The current repository should not contain client data. Examples must use fictional or anonymised information.

Future tools should:

- Avoid storing client-identifiable data by default.
- Clearly document data inputs and outputs.
- Keep API credentials out of source code.
- Provide safe sample data.
- Include review warnings for tax-sensitive outputs.

