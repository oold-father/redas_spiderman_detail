const puppeteer = require('puppeteer');

var arguments = process.argv.splice(2);

function startCrawl(url) {
    (async () => {
        const browser = await puppeteer.launch({
            // headless: false,
            slowMo: 200
        });

        const page = await browser.newPage();

        // 删除chromium的webdriver
        await page.evaluateOnNewDocument(() => {
            delete navigator.__proto__.webdriver;
        });

        // 设置HTTP头，对整个请求过程的所有子页面有效
        page.setExtraHTTPHeaders({
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'DNT': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        });

        // 修改UA，这种方式设置，在HTTP头中会是大写的：'User-Agent'
        await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36');

        var sendSingle = 1;
        try {
            console.log("准备爬取链接:", url);
            await page.goto(url);
        } catch (error) {
            console.log("浏览器访问错误");
            // console.log("\n", error);
            sendSingle = 0;
            browser.close();
        }

        if (1 == sendSingle) {
            var result = await page.content();
        }
        browser.close();
    })();
};

startCrawl(arguments[0]);