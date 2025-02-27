<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SQLite Command Revision Document</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 20px;
      }
      h1 {
        color: #333;
      }
      table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
      }
      th,
      td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
      }
      th {
        background-color: #f2f2f2;
      }
      footer {
        margin-top: 20px;
        font-size: 0.9em;
        color: #777;
      }
    </style>
  </head>
  <body>
    <h1>SQLite Command Revision Document</h1>

    <table>
      <thead>
        <tr>
          <th>Step</th>
          <th>Command</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>sudo apt update</td>
          <td>Update the package list.</td>
        </tr>
        <tr>
          <td>2</td>
          <td>sudo apt install sqlite3</td>
          <td>Install SQLite.</td>
        </tr>
        <tr>
          <td>3</td>
          <td>sqlite3 example.db</td>
          <td>Open SQLite and create a database.</td>
        </tr>
        <tr>
          <td>4</td>
          <td>CREATE TABLE COMPANIES (company_name varchar(20), id int);</td>
          <td>Create a table named COMPANIES.</td>
        </tr>
        <tr>
          <td>5</td>
          <td>INSERT INTO COMPANIES VALUES ("aganitha", 1);</td>
          <td>Insert a record into the COMPANIES table.</td>
        </tr>
        <tr>
          <td>6</td>
          <td>Ctrl+D or .exit</td>
          <td>Exit SQLite.</td>
        </tr>
        <tr>
          <td>7</td>
          <td>ls -l example.db</td>
          <td>Verify the database file exists.</td>
        </tr>
        <tr>
          <td>8</td>
          <td>scp example.db user@server_ip:/path/to/destination/</td>
          <td>Copy the database to a server.</td>
        </tr>
        <tr>
          <td>9</td>
          <td>ssh user@server_ip</td>
          <td>SSH into your server.</td>
        </tr>
        <tr>
          <td>10</td>
          <td>sudo apt install sqlite3</td>
          <td>Install SQLite on the server.</td>
        </tr>
        <tr>
          <td>11</td>
          <td>sqlite3 example.db</td>
          <td>Open the database on the server.</td>
        </tr>
        <tr>
          <td>12</td>
          <td>SELECT * FROM COMPANIES;</td>
          <td>Execute a query to see the results.</td>
        </tr>
        <tr>
          <td>13</td>
          <td>nano generate_inserts.sql</td>
          <td>Create a new file for generating inserts.</td>
        </tr>
        <tr>
          <td>14</td>
          <td>BEGIN TRANSACTION;</td>
          <td>Start a transaction for inserts.</td>
        </tr>
        <tr>
          <td>15</td>
          <td>COMMIT;</td>
          <td>Commit the transaction.</td>
        </tr>
        <tr>
          <td>16</td>
          <td>sqlite3 example.db < generate_inserts.sql</td>
          <td>Execute the SQL file to insert records.</td>
        </tr>
        <tr>
          <td>17</td>
          <td>SELECT * FROM COMPANIES;</td>
          <td>Verify the inserts.</td>
        </tr>
      </tbody>
    </table>
    <footer>
      <p>Note: This document was created using Blackbox AI.</p>
    </footer>
  </body>
</html>
