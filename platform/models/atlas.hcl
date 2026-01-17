variable "url" {
    type = string
    default = getenv("PLATFORM_OPERATIONS_DB_URL")
}

env "main" {
    url = var.url

    src = [
        "file://database/tables",
        "file://database/constraints",
        "file://database/indexes"
    ]

    migration {
        dir = "file://migrations"
    }

    format {
        schema {
            inspect = "{{ sql . }}"
        }
    }

    dev = "docker://postgres/17/dev"
}