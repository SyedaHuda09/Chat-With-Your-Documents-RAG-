import pytest

from app.security import UnsafeQueryError, validate_read_only_sql


def test_accepts_select_query():
    assert validate_read_only_sql("SELECT name FROM employees;") == "SELECT name FROM employees"


def test_accepts_select_with_markdown_fence():
    query = "```sql\nSELECT COUNT(*) FROM employees\n```"
    assert validate_read_only_sql(query) == "SELECT COUNT(*) FROM employees"


@pytest.mark.parametrize("query", [
    "DELETE FROM employees",
    "DROP TABLE employees",
    "UPDATE employees SET salary = 0",
    "INSERT INTO employees VALUES (9, 'Bad', 1, 0)",
    "SELECT * FROM employees; DELETE FROM employees",
    "PRAGMA table_info(employees)",
    "SELECT * FROM employees -- bypass",
])
def test_rejects_unsafe_query(query):
    with pytest.raises(UnsafeQueryError):
        validate_read_only_sql(query)
