# SQLite Insert Statements Guide

## Step 1: Delete Existing SQL File

<pre>rm generate_inserts.sql
</pre>

## Step 2: Create SQL File with Insert Statements

<pre># Create the SQL file and add initial lines
echo "-- This script generates 500 insert statements" > generate_inserts.sql
echo "BEGIN TRANSACTION;" >> generate_inserts.sql

# Generate insert statements
for i in {1..500}; do
    echo "INSERT INTO COMPANIES VALUES ('Company_$i', $i);" >> generate_inserts.sql
done

# Add commit statement
echo "COMMIT;" >> generate_inserts.sql
</pre>

## Step 3: Verify Contents of SQL File

<pre>cat generate_inserts.sql
</pre>

## Step 4: Execute SQL File with SQLite

<pre>sqlite3 example.db < generate_inserts.sql
</pre>

## Summary of Commands

<pre># Delete existing SQL file
rm generate_inserts.sql

# Create SQL file with insert statements
echo "-- This script generates 500 insert statements" > generate_inserts.sql
echo "BEGIN TRANSACTION;" >> generate_inserts.sql
for i in {1..500}; do
    echo "INSERT INTO COMPANIES VALUES ('Company_$i', $i);" >> generate_inserts.sql
done
echo "COMMIT;" >> generate_inserts.sql

# Execute SQL file
sqlite3 example.db < generate_inserts.sql
</pre>