# Capybara redemption

## Building and running

```bash
docker build --rm -f Dockerfile -t capy-redeem:latest .
docker run --name capy-redeem --rm -p 30003:30003 capy-redeem:latest
```

## Task

Find out how many capybaras are still available for redemption.

## Detering manual checks

Use JS to add an artificial setTimeout counter of 2s

## Hard mode

Randomly put 0 width characters between letters of a word to make it impossible to grep

## TODO

create hidden page for capy redemption
