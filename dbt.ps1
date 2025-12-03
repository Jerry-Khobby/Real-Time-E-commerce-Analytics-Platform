param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$args
)

docker run --rm -it `
  -v ${PWD}:/app `
  -p 8080:8080 `
  my-dbt dbt $args `
  --profiles-dir /app/ecommerce_dbt `
  --project-dir /app/ecommerce_dbt

