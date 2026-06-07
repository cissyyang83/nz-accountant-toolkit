from dataclasses import dataclass


@dataclass(frozen=True)
class QuickSaleResult:
    sale_proceeds: float
    deductible_cost_base: float
    draft_adjustment: float
    review_note: str


def calculate_quick_sale_adjustment(
    sale_price: float,
    purchase_price: float,
    acquisition_costs: float = 0.0,
    improvement_costs: float = 0.0,
    sale_costs: float = 0.0,
) -> QuickSaleResult:
    """Calculate a draft property sale adjustment for review."""
    for name, value in {
        "sale_price": sale_price,
        "purchase_price": purchase_price,
        "acquisition_costs": acquisition_costs,
        "improvement_costs": improvement_costs,
        "sale_costs": sale_costs,
    }.items():
        if value < 0:
            raise ValueError(f"{name} must not be negative")

    cost_base = purchase_price + acquisition_costs + improvement_costs + sale_costs
    adjustment = sale_price - cost_base

    return QuickSaleResult(
        sale_proceeds=round(sale_price, 2),
        deductible_cost_base=round(cost_base, 2),
        draft_adjustment=round(adjustment, 2),
        review_note=(
            "Confirm taxability under New Zealand land rules before treating "
            "this draft adjustment as taxable income."
        ),
    )

