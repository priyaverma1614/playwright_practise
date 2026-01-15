import pytest
import pytest_asyncio
from playwright.async_api import async_playwright

# @pytest.fixture(scope="function")
@pytest_asyncio.fixture(params=["chromium", "firefox"])
async def browser(request):
    async with async_playwright() as p:
        if request.param == "chromium":
            browser = await p.chromium.launch(headless=False)
        elif request.param == "firefox":
            browser = await p.firefox.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser: {request.param}")

        yield browser
        # if request.node.rep_call.failed:
        #     screenshot = await page.screenshot()
        #     allure.attach(
        #         screenshot,
        #         name="Failure Screenshot",
        #         attachment_type=allure.attachment_type.PNG,
        #     )
        await browser.close()
