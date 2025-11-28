param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$args
)


docker run --rm -it `
  -v ${PWD}:/app `
  --network host `
  my-dbt dbt $args `
  --profiles-dir /app/ecommerce_dbt `
  --project-dir /app/ecommerce_dbt
```