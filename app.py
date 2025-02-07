import gradio as gr
from PyPDF2 import PdfMerger

# Function to merge PDFs
def merge_pdfs(files):
    merger = PdfMerger()
    
    for file in files:
        merger.append(file.name)

    output_filename = "merged_output.pdf"
    merger.write(output_filename)
    merger.close()

    return output_filename

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# PDF Merger App")
    
    with gr.Row():
        pdf_files = gr.File(file_types=[".pdf"], file_count="multiple", label="Upload PDF Files")
        merge_button = gr.Button("Merge PDFs")
    
    output_file = gr.File(label="Download Merged PDF")

    merge_button.click(fn=merge_pdfs, inputs=[pdf_files], outputs=[output_file])

# Launch the app
demo.launch()
