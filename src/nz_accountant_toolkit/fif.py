from dataclasses import dataclass


@dataclass(frozen=True)
class FifResult:
    fdr_income: float
    cv_income: float
    lower_method: str
    review_note: str


def calculate_fif(
    opening_market_value: float,
    closing_market_value: float,
    purchases: float = 0.0,
    sales_proceeds: float = 0.0,
    dividends: float = 0.0,
    fdr_rate: float = 0.05,
) -> FifResult:
    """Compare simple FDR and CV FIF income estimates.

    This helper supports workpaper review only. It does not decide whether FIF
    rules apply or whether a method is available for a particular investment.
    """
    _require_non_negative("opening_market_value", opening_market_value)
    _require_non_negative("closing_market_value", closing_market_value)
    _require_non_negative("purchases", purchases)
    _require_non_negative("sales_proceeds", sales_proceeds)
    _require_non_negative("dividends", dividends)
    _require_non_negative("fdr_rate", fdr_rate)

    fdr_income = opening_market_value * fdr_rate
    cv_income = closing_market_value + sales_proceeds + dividends - opening_market_value - purchases
    lower_method = "CV" if cv_income < fdr_income else "FDR"

    return FifResult(
        fdr_income=round(fdr_income, 2),
        cv_income=round(cv_income, 2),
        lower_method=lower_method,
        review_note=(
            "Confirm FIF applicability, exemptions, currency conversion, "
            "and whether the selected method is permitted."
        ),
    )


def _require_non_negative(name: str, value: float) -> None:
    if value < 0:
        raise ValueError(f"{name} must not be negative")

