import re


class UnsafeQueryError(ValueError):
    """Raised when generated SQL violates the demo's read-only policy."""


_BLOCKED = re.compile(
    r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|REPLACE|TRUNCATE|ATTACH|DETACH|PRAGMA|"
    r"VACUUM|GRANT|REVOKE|EXEC|EXECUTE)\b",
    re.IGNORECASE,
)


def validate_read_only_sql(query: str) -> str:
    """Allow one SELECT statement only; reject comments and statement chaining."""
    sql = query.strip()

    # Remove common markdown fences emitted by language models.
    sql = re.sub(r"^\s*```(?:sql)?\s*", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"\s*```\s*$", "", sql)

    if not sql:
        raise UnsafeQueryError("The generated SQL query is empty.")

    if "--" in sql or "/*" in sql or "*/" in sql:
        raise UnsafeQueryError("SQL comments are not allowed.")

    normalized = sql.rstrip().rstrip(";").strip()
    if ";" in normalized:
        raise UnsafeQueryError("Only one SQL statement is allowed.")

    if not re.match(r"^SELECT\b", normalized, flags=re.IGNORECASE):
        raise UnsafeQueryError("Only SELECT statements are allowed.")

    if _BLOCKED.search(normalized):
        raise UnsafeQueryError("The query contains a prohibited SQL operation.")

    return normalized
