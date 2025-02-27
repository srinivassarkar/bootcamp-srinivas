
## 10 Key Points to Remember about DBs

*   **File Systems vs. RDBMS:** File systems are simple but lack concurrency control, indexing, and transaction management. RDBMS provides structured data storage and robust data management.
*   **ACID Properties:**
    *   **Atomicity:** Ensures all parts of a transaction are completed or none are.
    *   **Consistency:** Maintains data integrity by enforcing rules and constraints.
    *   **Isolation:** Ensures transactions don’t interfere with each other.
    *   **Durability:** Guarantees that committed transactions are permanently saved.
*   **Indexing:** Indexes speed up data retrieval but require maintenance during inserts, updates, and deletes. Without indexing, querying large datasets can be slow.
*   **SQL (Structured Query Language):** A declarative language used to interact with RDBMS. It allows users to define what data they need without specifying how to retrieve it.
*   **Concurrency Control:** RDBMS handles multiple users accessing and modifying data simultaneously, preventing data corruption.
*   **Relational Model:** Data is stored in tables with rows and columns. Relationships between tables are established using keys (primary and foreign keys).
*   **Object-Relational and Object Databases:** Object-relational databases extend RDBMS to support custom data types. Object databases store data as objects but are less popular due to complexity.
*   **Data Integrity:** RDBMS enforces constraints (e.g., primary keys, foreign keys, and check constraints) to ensure data accuracy and consistency.
*   **Performance Considerations:** RDBMS performance depends on proper indexing, query optimization, and hardware resources.
*   **Evolution of Databases:** RDBMS evolved from hierarchical and network databases of the 1960s. Despite newer technologies, RDBMS remains dominant due to its reliability and scalability.

</div>

<footer>

Note: This document was created using DeepSeek AI.

</footer>