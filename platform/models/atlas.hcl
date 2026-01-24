variable "operations_url" {
    type = string
    default = getenv("PLATFORM_OPERATIONS_DB_URL")
}

variable "analytics_url" {
    type = string
    default = getenv("PLATFORM_ANALYTICS_DB_URL")
}

env "operations" {
    url = var.operations_url

    src = [
        "file://operations/database/tables",
        "file://operations/database/constraints/unique_keys",
        "file://operations/database/constraints/foreign_keys",
        "file://operations/database/indexes"
    ]

    migration {
        dir = "file://operations/migrations"
    }

    format {
        schema {
            inspect = "{{ sql . }}"
        }
    }

    dev = "docker://postgres/17/dev"
}

env "analytics" {
    url = var.analytics_url

    src = [
        "file://analytics/databases/schema",
        "file://analytics/databases/public/tables"
    ]

    migration {
        dir = "file://analytics/migrations"
    }

    format {
        schema {
            inspect = "{{ sql . }}"
        }
    }

    dev = "docker://clickhouse/latest"
}