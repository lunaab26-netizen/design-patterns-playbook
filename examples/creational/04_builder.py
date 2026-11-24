"""
Builder

Intent: construct a complex object step by step, so the same process can produce different representations and no half-built object ever escapes.

Category: Creational
"""

class QueryBuilder:
    def __init__(self):
        self._select = "*"
        self._where = []
        self._limit = None

    def select(self, *cols):
        self._select = ", ".join(cols)
        return self

    def where(self, cond):
        self._where.append(cond)
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self) -> str:
        sql = f"SELECT {self._select} FROM orders"
        if self._where:
            sql += " WHERE " + " AND ".join(self._where)
        if self._limit:
            sql += f" LIMIT {self._limit}"
        return sql

q = (QueryBuilder()
     .select("id", "total")
     .where("status = 'paid'")
     .where("total > 100")
     .limit(50)
     .build())
print(q)
