# My personal blog for WGU career

## Selecting career path

- Using tools we use at WGU
- Creating and experiment with them


## First project

- Django personal blog


## Tools

- UV
- RUFF
- DRF actions
- httpx



## Development


### Init the project

`$ uv sync`


### Create a superuser first (if not exists)
`uv run python manage.py createsuperuser`

### Load the fixtures
`uv run python manage.py loaddata posts`

### Or create fixtures from existing data
`uv run python manage.py dumpdata blog.post --indent 2 > blog/fixtures/posts.json`
