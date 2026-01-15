import allure
import pytest
from playwright.async_api import async_playwright
from locators import blogsSpotsLocators

@pytest.mark.asyncio
@allure.title("Test Login Functionality")
async def test_google_search(browser):
    async with async_playwright() as p:
        # browser = await p.chromium.launch(headless=False)
        context =await browser.new_context(
                   record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
        )
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.goto("https://testautomationpractice.blogspot.com/")
        assert "Automation Testing Practice" in await page.title()
        source=page.locator(blogsSpotsLocators.DRAGELEMENT)
        await source.scroll_into_view_if_needed()
        target=page.locator(blogsSpotsLocators.DROPHERE)
        await source.drag_to(target)
        await page.locator(blogsSpotsLocators.COUNTRYDROPDOWN).select_option("Canada")
        print("selected canada")
        await page.locator("#singleFileInput").set_input_files("/home/dell/Pictures/Screenshot from 2025-12-24 23-18-53.png")
        print("choose file")
        await page.screenshot(path="screenshot.png")
        await page.pause()
        await context.tracing.stop(path="trace_google.zip")
        await context.close()

@pytest.mark.asyncio
async def test_bing_search():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.bing.com")
        assert "Bing" in await page.title()
        await browser.close()

