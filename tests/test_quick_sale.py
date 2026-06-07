from nz_accountant_toolkit import calculate_quick_sale_adjustment


def test_quick_sale_example_calculates_draft_adjustment():
    result = calculate_quick_sale_adjustment(
        sale_price=900000,
        purchase_price=760000,
        acquisition_costs=7500,
        improvement_costs=48000,
        sale_costs=22000,
    )

    assert result.deductible_cost_base == 837500
    assert result.draft_adjustment == 62500

