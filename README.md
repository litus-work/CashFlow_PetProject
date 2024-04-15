## Cash-Flow_PetProject

### Description:
Cash-Flow_PetProject is a web application designed to help users manage their finances by tracking transactions and categorizing expenses. It provides a user-friendly interface for adding, editing, and deleting transactions, as well as managing transaction categories.

### Features:
1. **Transaction Management:**
   - Add new transactions with details such as amount, date, description, and category.
   - Edit existing transactions to update their details.
   - Delete individual transactions.
   - View a list of all transactions.

2. **Category Management:**
   - Add new transaction categories.
   - Edit existing categories to update their names.
   - Delete individual categories.
   - View a list of all categories.

3. **CSV File Upload:**
   - Upload transactions in bulk using a CSV file.
   - Process the uploaded CSV file to add transactions to the database.

4. **Clear Data:**
   - Delete all transactions to start fresh.
   - Delete all categories when needed.

5. **Styling and UI:**
   - Responsive and intuitive user interface.
   - Bootstrap framework for styling and layout.
   - Custom CSS for additional styling.

### Technologies Used:
- Django: Backend web framework for Python.
- SQLite: Relational database management system.
- HTML/CSS: Frontend markup and styling.
- Bootstrap: Frontend framework for responsive design.
- JavaScript: Used for client-side interactions.

### Setup Instructions:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run migrations to create the database schema using `python manage.py migrate`.
5. Start the development server using `python manage.py runserver`.
6. Access the application in your web browser at `http://localhost:8000`.

### Contributors:
- Litus Serhii