import csv
from docxtpl import DocxTemplate
import os

with open("data.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=';')
    next(file_reader)

    output_dir = 'generated_documents'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for row in file_reader:
        diary_doc = DocxTemplate("diary_template.docx")
        diary_context = {
            "group_number": row[1],
            "student_name": row[2],
            "supervisor_name": row[3],
            "supervisor_position": row[4],
            "year": row[7],
            "start_date": row[8],
            "end_date": row[9],
            "place_of_practice": row[10],
        }
        diary_doc.render(diary_context)
        diary_output_path = os.path.join(output_dir, f'diary_{row[1]}_{row[2]}.docx')
        diary_doc.save(diary_output_path)

        report_doc = DocxTemplate("report_template.docx")
        report_context = {
            "group_number": row[1],
            "student_name": row[2],
            "supervisor_name": row[3],
            "supervisor_position": row[4],
            "mark": row[5],
            "date_of_delivery": row[6],
            "year": row[7],
            "start_date": row[8],
            "end_date": row[9],
            "place_of_practice": row[10],
            "purpose": row[11],
        }
        report_doc.render(report_context)
        report_output_path = os.path.join(output_dir, f'report_{row[1]}_{row[2]}.docx')
        report_doc.save(report_output_path)

print("Документы успешно сгенерированы!")
