# Understanding Transactions and ACID Properties

<section>

## 1\. What are Transactions?

Transactions are sequences of operations performed as a single logical unit of work in a database. They ensure data integrity by either fully completing or fully rolling back changes, maintaining consistency even in the event of failures.

</section>

<section>

## 2\. What are ACID Properties?

### ACID Properties:

*   **Atomicity:** Ensures all parts of a transaction are completed or none are.
*   **Consistency:** Maintains data integrity by enforcing rules and constraints.
*   **Isolation:** Ensures transactions don’t interfere with each other.
*   **Durability:** Guarantees that committed transactions are permanently saved.

</section>

<section>

## 3\. The Importance of Transactions

A system without transactions is generally unreliable and can lead to data corruption. Without the ability to ensure atomicity and consistency, partial updates may occur, resulting in inconsistent data states. This lack of reliability makes the system unsuitable for critical applications where data integrity is paramount.

</section>

<section>

## 4\. Properties of a File System

A file system typically possesses properties such as:

*   **Reliability:** Ensuring data is not lost.
*   **Performance:** Allowing for quick data access.
*   **Scalability:** Accommodating growing data needs.
*   **Security:** Protecting against unauthorized access.

These properties collectively provide a robust framework for effective data management and storage.

</section>

<section>

## 5 & 6\. Implications of Bending ACID Properties

### No Atomicity:

The system doesn’t guarantee that every part of a transaction finishes together. For example, X updates the retweet count right away but might delay recording who retweeted, letting things happen in pieces to keep things fast.

### No Consistency:

The data doesn’t always follow the rules immediately. Amazon lets stock drop below zero during a rush, fixing it later by canceling an order, so sales don’t slow down.

### No Isolation:

Transactions can overlap and mess with each other. Uber might let two people book the same driver at once, sorting out the mix-up afterward to keep bookings quick.

### No Durability:

Changes aren’t always saved permanently right away. Netflix tracks what you’re watching in the moment but might not save it to disk instantly, risking a loss if there’s a crash, all to prioritize smooth streaming.

These big players show that bending ACID rules helps them handle speed and scale, even if it means perfection takes a backseat!

</section>