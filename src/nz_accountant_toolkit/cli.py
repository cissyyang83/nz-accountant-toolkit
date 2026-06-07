import argparse

from .fif import calculate_fif
from .gst import calculate_gst_variance
from .quick_sale import calculate_quick_sale_adjustment


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="nz-accountant-toolkit",
        description="Practical calculation helpers for New Zealand accounting workpapers.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    fif = subparsers.add_parser("fif", help="Compare simple FIF FDR and CV estimates")
    fif.add_argument("--opening", type=float, required=True)
    fif.add_argument("--closing", type=float, required=True)
    fif.add_argument("--purchases", type=float, default=0.0)
    fif.add_argument("--sales", type=float, default=0.0)
    fif.add_argument("--dividends", type=float, default=0.0)

    gst = subparsers.add_parser("gst-variance", help="Compare accounting GST to filed GST")
    gst.add_argument("--accounting", type=float, required=True)
    gst.add_argument("--filed", type=float, required=True)
    gst.add_argument("--threshold", type=float, default=1.0)

    quick_sale = subparsers.add_parser("quick-sale", help="Calculate a draft property sale adjustment")
    quick_sale.add_argument("--sale-price", type=float, required=True)
    quick_sale.add_argument("--purchase-price", type=float, required=True)
    quick_sale.add_argument("--acquisition-costs", type=float, default=0.0)
    quick_sale.add_argument("--improvements", type=float, default=0.0)
    quick_sale.add_argument("--sale-costs", type=float, default=0.0)

    args = parser.parse_args()

    if args.command == "fif":
        result = calculate_fif(args.opening, args.closing, args.purchases, args.sales, args.dividends)
        print(f"FDR income: NZD {result.fdr_income:,.2f}")
        print(f"CV income: NZD {result.cv_income:,.2f}")
        print(f"Lower draft method: {result.lower_method}")
        print(f"Review note: {result.review_note}")
    elif args.command == "gst-variance":
        result = calculate_gst_variance(args.accounting, args.filed, args.threshold)
        print(f"Accounting GST: NZD {result.accounting_gst:,.2f}")
        print(f"Filed GST: NZD {result.filed_gst:,.2f}")
        print(f"Variance: NZD {result.variance:,.2f}")
        print(f"Requires review: {'Yes' if result.requires_review else 'No'}")
    elif args.command == "quick-sale":
        result = calculate_quick_sale_adjustment(
            args.sale_price,
            args.purchase_price,
            args.acquisition_costs,
            args.improvements,
            args.sale_costs,
        )
        print(f"Sale proceeds: NZD {result.sale_proceeds:,.2f}")
        print(f"Deductible cost base: NZD {result.deductible_cost_base:,.2f}")
        print(f"Draft adjustment: NZD {result.draft_adjustment:,.2f}")
        print(f"Review note: {result.review_note}")


if __name__ == "__main__":
    main()

