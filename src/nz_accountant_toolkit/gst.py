from dataclasses import dataclass


@dataclass(frozen=True)
class GstVarianceResult:
    accounting_gst: float
    filed_gst: float
    variance: float
    requires_review: bool


def calculate_gst_variance(
    accounting_gst: float,
    filed_gst: float,
    review_threshold: float = 1.0,
) -> GstVarianceResult:
    """Compare accounting GST to a filed GST return amount."""
    if review_threshold < 0:
        raise ValueError("review_threshold must not be negative")

    variance = round(accounting_gst - filed_gst, 2)
    return GstVarianceResult(
        accounting_gst=round(accounting_gst, 2),
        filed_gst=round(filed_gst, 2),
        variance=variance,
        requires_review=abs(variance) > review_threshold,
    )

