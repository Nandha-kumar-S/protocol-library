# Utility to run a function as a FastAPI background task
from fastapi import BackgroundTasks

from utils.constants import DEFAULT_EXPORT_WIDTH

def run_in_background(background_tasks: BackgroundTasks, func, *args, **kwargs):
	"""
	Adds the given function to FastAPI's background tasks.
	Usage:
		run_in_background(background_tasks, my_func, arg1, arg2, kwarg1=value)
	"""
	background_tasks.add_task(func, *args, **kwargs)



# Function to handle the export
def export_to_excel_sheets(all_data: list, output_filename: str):
	import pandas as pd
	from openpyxl.utils import get_column_letter
	"""
	Exports multiple JSON data lists to a single Excel file with separate sheets.

	Args:
		data_sheets (list): A list of tuples, where each tuple contains (data_list, sheet_name).
		output_filename (str): The name of the Excel file to create.
	"""
	with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
		for row in all_data:
			sheet_name = row.get('schema_name')
			data = row.get('json_value', [])
			try:
				# Use json_normalize to flatten the data.
				# It handles nested dictionaries by creating new columns
				# like 'notes.id' and 'notes.codes.code'.
				df = pd.json_normalize(data)

				# Write the flattened DataFrame to the specified sheet
				df.to_excel(writer, sheet_name=sheet_name, index=False)
				# Access the workbook and worksheet objects to set column widths
				workbook = writer.book
				
				worksheet = workbook[sheet_name]
				
				# Iterate through columns and set the default width
				for i, col in enumerate(df.columns):
					column_letter = get_column_letter(i + 1)
					worksheet.column_dimensions[column_letter].width = DEFAULT_EXPORT_WIDTH
				
				print(f"Successfully exported data to sheet: '{sheet_name}'")
			except Exception as e:
				print(f"Error exporting data to sheet '{sheet_name}': {e}")
				# Optional: you can continue to the next sheet even if one fails
				continue

