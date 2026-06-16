from fpdf import FPDF

message = "Assalamu Alaikum. I hope you are doing well. May Allah grant you complete shifa, restore your health, and bless you with strength and wellbeing. I just wanted to wish you the very best for your exams. May Allah guide you, grant you success, and ease your affairs in every step of life. Remember, I am always here if you ever need help or have any questions. Keep me in your prayers."

pdf = FPDF()
# pdf.set_auto_page_break(auto=True, margin=15) For Multiple Pages
pdf.add_page()
pdf.set_font("Arial", size = 12)
pdf.multi_cell(0, 10, str(message))
pdf.output("greeting.pdf")