import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

# Function to generate the PDF report
def generate_loan_report():
    # Step 1: Check if the CSV file exists
    csv_file = "loan.csv"
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    try:
        # Step 2: Read the CSV file
        df = pd.read_csv(csv_file)

        # Step 3: Data Cleaning
        # Fill missing LoanAmount with median
        df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
        # Fill missing Gender with 'Unknown'
        df['Gender'] = df['Gender'].fillna('Unknown')
        # Fill missing Credit_History with mode
        df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

        # Step 4: Data Analysis
        # Total applications
        total_applications = len(df)
        # Approved loans
        approved_loans = len(df[df['Loan_Status'] == 'Y'])
        approval_rate = (approved_loans / total_applications) * 100
        # Average loan amount and applicant income
        avg_loan_amount = df['LoanAmount'].mean()
        avg_applicant_income = df['ApplicantIncome'].mean()

        # Approval rates by group
        # By Gender
        gender_approval = df.groupby('Gender')['Loan_Status'].value_counts(normalize=True).unstack().fillna(0)
        gender_approval_rate = gender_approval['Y'] * 100 if 'Y' in gender_approval.columns else pd.Series(0, index=gender_approval.index)
        
        # By Property Area
        property_approval = df.groupby('Property_Area')['Loan_Status'].value_counts(normalize=True).unstack().fillna(0)
        property_approval_rate = property_approval['Y'] * 100 if 'Y' in property_approval.columns else pd.Series(0, index=property_approval.index)
        
        # By Credit History
        credit_approval = df.groupby('Credit_History')['Loan_Status'].value_counts(normalize=True).unstack().fillna(0)
        credit_approval_rate = credit_approval['Y'] * 100 if 'Y' in credit_approval.columns else pd.Series(0, index=credit_approval.index)

        # Sample data for table (first 5 records, selected columns)
        sample_df = df[['Loan_ID', 'Gender', 'LoanAmount', 'Loan_Status']].head(5)

        # Step 5: Set up the PDF
        pdf_file = "loan_report.pdf"
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        elements = []

        # Step 6: Add a title
        styles = getSampleStyleSheet()
        title = Paragraph("Loan Application Report", styles['Heading1'])
        elements.append(title)
        elements.append(Spacer(1, 12))

        # Step 7: Add summary statistics
        summary = [
            Paragraph(f"Total Applications: {total_applications}", styles['Normal']),
            Paragraph(f"Approved Loans: {approved_loans} ({approval_rate:.1f}% approval rate)", styles['Normal']),
            Paragraph(f"Average Loan Amount: ${avg_loan_amount:,.2f}K", styles['Normal']),
            Paragraph(f"Average Applicant Income: ${avg_applicant_income:,.2f}", styles['Normal'])
        ]
        elements.extend(summary)
        elements.append(Spacer(1, 12))

        # Step 8: Add grouped analysis
        elements.append(Paragraph("Approval Rates by Category", styles['Heading2']))
        elements.append(Spacer(1, 6))
        
        # Gender approval rates
        gender_text = [Paragraph("By Gender:", styles['Normal'])]
        for gender, rate in gender_approval_rate.items():
            gender_text.append(Paragraph(f"  {gender}: {rate:.1f}%", styles['Normal']))
        elements.extend(gender_text)
        
        # Property Area approval rates
        property_text = [Paragraph("By Property Area:", styles['Normal'])]
        for area, rate in property_approval_rate.items():
            property_text.append(Paragraph(f"  {area}: {rate:.1f}%", styles['Normal']))
        elements.extend(property_text)
        
        # Credit History approval rates
        credit_text = [Paragraph("By Credit History:", styles['Normal'])]
        for credit, rate in credit_approval_rate.items():
            credit_text.append(Paragraph(f"  {credit}: {rate:.1f}%", styles['Normal']))
        elements.extend(credit_text)
        elements.append(Spacer(1, 12))

        # Step 9: Add sample data table
        elements.append(Paragraph("Sample Loan Records", styles['Heading2']))
        data = [sample_df.columns.tolist()] + sample_df.values.tolist()
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 12))

        # Step 10: Add footer
        footer = Paragraph("Generated by Loan Report Script", styles['Italic'])
        elements.append(footer)

        # Step 11: Build the PDF
        doc.build(elements)
        print(f"PDF report generated: {pdf_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the function
if __name__ == "__main__":
    generate_loan_report()