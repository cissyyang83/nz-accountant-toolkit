from nz_accountant_toolkit import calculate_gst_variance


def test_gst_variance_flags_material_difference():
    result = calculate_gst_variance(accounting_gst=12450, filed_gst=12300)

    assert result.variance == 150
    assert result.requires_review is True


def test_gst_variance_allows_small_rounding_difference():
    result = calculate_gst_variance(accounting_gst=1000.40, filed_gst=1000.00, review_threshold=1)

    assert result.variance == 0.4
    assert result.requires_review is False

