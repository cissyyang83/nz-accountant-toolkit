from nz_accountant_toolkit import calculate_fif


def test_fif_example_compares_fdr_and_cv():
    result = calculate_fif(
        opening_market_value=80000,
        closing_market_value=92000,
        purchases=10000,
        dividends=1600,
    )

    assert result.fdr_income == 4000
    assert result.cv_income == 3600
    assert result.lower_method == "CV"

