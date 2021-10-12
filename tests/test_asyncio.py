import pytest as pytest

from example.basic import call_google_n_times


@pytest.mark.asyncio
async def test_asyncio():
    await call_google_n_times(10)