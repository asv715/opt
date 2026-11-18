import pytest
from decimal import Decimal
from starter import recommend_price, sample_fetch_offers

@pytest.mark.asyncio
async def test_success_path():
    result = await recommend_price(
        sample_fetch_offers,
        current_price=Decimal("4900.00"),
        min_price=Decimal("4500.00"),
    )

    assert result['price'] == 4728


@pytest.mark.asyncio
async def test_review_decision():
    result = await recommend_price(
        sample_fetch_offers,
        current_price=Decimal("2900.00"),
        min_price=Decimal("4500.00"),
    )

    assert result['decision'] == 'REVIEW'