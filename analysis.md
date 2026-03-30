Production Migration Strategy

In a production environment with live traffic, this migration (adding salary_history and backfilling data) should be handled carefully to avoid downtime and data inconsistency.

First, I would deploy the new table (salary_history) without modifying existing logic. This ensures the current system continues to function normally while the new structure is introduced.

Next, I would run the backfill process in batches, instead of inserting all records at once. This prevents long-running locks and reduces load on the database. For example, processing employees in chunks (e.g., 100–500 rows per batch) avoids performance degradation.

To maintain data consistency during the transition, I would introduce a trigger or dual-write mechanism. Any new salary updates in the employees table should also be inserted into salary_history. This ensures no data is lost between the start and end of the migration.

After backfilling is complete, I would validate the data by comparing counts and aggregates (e.g., total salaries per department) between the old and new structures.

Finally, once confidence is established, I would gradually shift reads to the new table, and only then consider deprecating or refactoring the original schema if needed.