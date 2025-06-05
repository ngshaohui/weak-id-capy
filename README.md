# Capybara redemption

## Building and running

```bash
docker build --rm -f Dockerfile -t capy-redeem:latest .
docker run --name capy-redeem --rm -p 30003:30003 capy-redeem:latest
```

## Task

There are 2 tasks.

1. Find out what are the coupon codes that can still be redeemed.

2. Redeem the coupon codes from the hidden redemption page

### Detering manual checks

There is an artificial JS setInterval countdown timer before rendering the page to discourage people from manually visiting each page.

### Hard mode (not implemented)

1. Randomly put 0 width characters between letters of a word to make it impossible to grep
2. Only give one page and let them figure out the rest of the ID sequences

## Walkthrough

Visit some pages to figure out the URL structure

ID number starts from 100001, runs sequentially until 100111

The first one will always be an available coupon code

Need to use the intruder to run from 100001 through 100111 using a number payload, and find all the pages with "available" in the page text

Hidden redemption page can be found by triggering the Django debug page
