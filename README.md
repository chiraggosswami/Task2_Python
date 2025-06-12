# Task2_Python
Company: CodTech IT Solutions 
Name: Chirag Goswami 
Intern Id: CT06DF670 
Domain: Python Programming 
Duration: 4 weeks 
Mentor: NEELA SANTOSH #Result: 

Description:
This Python script is a complete data analysis and PDF report generation tool for a loan dataset. It integrates the capabilities of pandas for data manipulation and ReportLab for PDF generation. Its purpose is to load, clean, analyze, and summarize loan application data, and present this information in a structured, professionally styled PDF report. Let’s walk through the major components of the script and understand how each part contributes to the final output.

1. Library Imports and Setup
The script begins by importing essential libraries:

pandas is used for data loading, cleaning, and analysis. It provides a powerful DataFrame structure for manipulating tabular data.

reportlab libraries (SimpleDocTemplate, Paragraph, Table, etc.) are used to create PDF documents. These enable the addition of formatted text, tables, and layout control.

os is used to verify if the required CSV file exists before proceeding.

This careful selection of libraries ensures the script is both data-aware and capable of professional report generation.

2. Function Definition: generate_loan_report()
All logic is encapsulated within a function named generate_loan_report(). This approach promotes modularity, readability, and reusability.

3. Checking for Data File
The script expects a CSV file named "loan.csv" to exist in the same directory. Using os.path.exists, it checks whether the file is present. If not, an error is printed and the function exits early. This safeguard prevents the program from crashing due to missing input files.

python
Copy
Edit
csv_file = "loan.csv"
if not os.path.exists(csv_file):
    print(f"Error: {csv_file} not found.")
    return
4. Reading and Cleaning Data
The next step is to load the data using pandas.read_csv() into a DataFrame df. After loading, the script performs several data cleaning operations:

LoanAmount: Missing values are filled with the median, a common technique to handle outliers.

Gender: Missing genders are labeled as "Unknown".

Credit_History: Missing values are filled with the mode (most frequent value), as it's typically categorical.

This preprocessing ensures that the dataset is complete and suitable for analysis, without introducing significant bias.

5. Basic Data Analysis
Once cleaned, the script performs descriptive analysis:

Total number of applications

Number and percentage of approved loans (where Loan_Status == 'Y')

Average loan amount

Average applicant income

These metrics provide an immediate understanding of the dataset's overall characteristics.

6. Grouped Analysis by Category
To understand trends across specific groups, the script computes loan approval rates based on:

Gender

Property Area

Credit History

This is achieved using groupby() and value_counts(normalize=True), followed by reshaping using unstack() and multiplying by 100 to get percentages.

These statistics are helpful for identifying any demographic or geographic patterns in loan approvals, potentially aiding in fairer policy or better risk assessment.

Example:

python
Copy
Edit
gender_approval = df.groupby('Gender')['Loan_Status'].value_counts(normalize=True).unstack().fillna(0)
gender_approval_rate = gender_approval['Y'] * 100
7. Extracting Sample Data
To give a glimpse of the actual data, the script extracts the first five records, focusing on:

Loan ID

Gender

Loan Amount

Loan Status

This table will later be rendered into the PDF to give readers a direct look at real examples from the dataset.

8. Setting Up the PDF Document
The ReportLab library is used to create a PDF file named "loan_report.pdf". The SimpleDocTemplate object is initialized with letter page size. An empty list called elements is created to store the content blocks that will be added to the PDF.

9. Building the Report Layout
The report consists of several structured sections:

Title
A main title, “Loan Application Report”, is added using a heading style (Heading1). A spacer is added to provide visual separation between sections.

Summary Statistics
Using the normal text style (Normal), key summary metrics (total applications, approvals, average income, etc.) are added as paragraphs. This gives the reader a top-level overview of the data.

Approval Rates by Category
Subsections are introduced for each grouping (gender, property area, and credit history), along with their respective approval rates formatted with one decimal precision. This part of the report presents deeper insights into who gets approved more often.

Each entry is dynamically generated from the earlier grouped analysis data and converted into formatted paragraph elements.

Sample Table
The sample loan data is presented in a tabular format using ReportLab’s Table class. It includes headers and the first five records. To make the table visually appealing and easy to read, the script applies several styles:

Header row with grey background and white text.

Center alignment.

Grid lines and font styling for readability.

This table provides a snapshot of the underlying data, making the report more concrete.

10. Footer and Finalization
A simple footer is added to indicate that the document was generated by this script. It uses an italicized paragraph style for distinction.

After all elements are prepared, doc.build(elements) is called to generate the final PDF file. If the operation is successful, a confirmation message is printed to the console.

In case of any exceptions (e.g., file reading issues, processing errors), they are caught by a try-except block, and the error message is printed without crashing the program.

11. Running the Script
Finally, the script includes a standard Python idiom:

python
Copy
Edit
if __name__ == "__main__":
    generate_loan_report()
This ensures that the report generation only runs when the script is executed directly, not when it is imported as a module.

Conclusion
This script is a great example of combining data analytics with reporting automation. It handles the complete pipeline—from reading raw data to generating a professional PDF report. Let’s recap the strengths of this program:

Modular and maintainable: All logic is inside a function, promoting clean code organization.

Fault-tolerant: Includes file checks and error handling.

Data cleansing: Takes care of missing values, making analysis reliable.

Insightful analysis: Computes both overall and grouped statistics.

Polished reporting: Uses ReportLab to create a visually clean and informative document.

This tool could be highly useful in real-world scenarios like business reporting, loan approval dashboards, or administrative summaries, especially in financial institutions or data analysis roles. By adapting the code slightly, it could also support visual charts, multi-page reports, or real-time data feeds.
