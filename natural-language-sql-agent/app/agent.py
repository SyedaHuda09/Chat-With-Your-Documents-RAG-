import os
import re

from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

from .database import get_sql_database
from .security import validate_read_only_sql


def build_query_chain():
    database = get_sql_database()
    model = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0,
    )
    return create_sql_query_chain(model, database), database


def answer_question(question: str) -> dict:
    chain, database = build_query_chain()
    generated = chain.invoke({"question": question})
    sql = validate_read_only_sql(generated)

    # Execute only after validation. SQLDatabase.run returns a printable result.
    result = database.run(sql)
    return {"question": question, "sql": sql, "result": result}
