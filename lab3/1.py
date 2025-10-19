from abc import ABC, abstractmethod


#Інтерфейс
class QueryBuilder(ABC):
    @abstractmethod
    def select(self, columns):
        pass

    @abstractmethod
    def where(self, condition):
        pass

    @abstractmethod
    def limit(self, n):
        pass

    @abstractmethod
    def getSQL(self):
        pass


#Реалізація для PostgreSQL
class PostgreSQLQueryBuilder(QueryBuilder):
    def __init__(self):
        self.query = {
            "select": "*",
            "from": "",
            "where": "",
            "limit": ""
        }

    def select(self, columns):
        if isinstance(columns, list):
            self.query["select"] = ", ".join(columns)
        else:
            self.query["select"] = columns
        self.query["from"] = "FROM some_table"
        return self

    def where(self, condition):
        self.query["where"] = f"WHERE {condition}"
        return self

    def limit(self, n):
        self.query["limit"] = f"LIMIT {n}"
        return self

    def getSQL(self):
        sql = f"SELECT {self.query['select']} {self.query['from']}"
        if self.query["where"]:
            sql += f" {self.query['where']}"
        if self.query["limit"]:
            sql += f" {self.query['limit']}"
        return sql + ";"


#   Реалізація для MySQL 
class MySQLQueryBuilder(QueryBuilder):
    def __init__(self):
        self.query = {
            "select": "*",
            "from": "",
            "where": "",
            "limit": ""
        }

    def select(self, columns):
        if isinstance(columns, list):
            self.query["select"] = ", ".join(columns)
        else:
            self.query["select"] = columns
        self.query["from"] = "FROM some_table"
        return self

    def where(self, condition):
        self.query["where"] = f"WHERE {condition}"
        return self

    def limit(self, n):
        self.query["limit"] = f"LIMIT {n}"
        return self

    def getSQL(self):
        sql = f"SELECT {self.query['select']} {self.query['from']}"
        if self.query["where"]:
            sql += f" {self.query['where']}"
        if self.query["limit"]:
            sql += f" {self.query['limit']}"
        return sql + ";"


#Клієнтський код 
def client_code(builder: QueryBuilder):
    query = (
        builder
        .select(["id", "name", "email"])
        .where("age > 18")
        .limit(10)
        .getSQL()
    )
    print(query)


#Використання
if __name__ == "__main__":
    print("PostgreSQL:")
    client_code(PostgreSQLQueryBuilder())

    print("\nMySQL:")
    client_code(MySQLQueryBuilder())
