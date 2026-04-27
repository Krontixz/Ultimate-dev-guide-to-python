import os
from weasyprint import HTML

def compile_markdown_to_pdf():
    # 1. Configuration
    output_dir = "scripts"
    output_filename = "my_ultimate_py_guide.pdf"
    output_path = os.path.join(output_dir, output_filename)

    # Create scripts folder if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. Find every .md file in the current folder and subfolders
    md_files = []
    for root, dirs, files in os.walk("."):
        # Tell the script to ignore the 'scripts' folder and hidden git folders
        if "scripts" in root or ".git" in root:
            continue
            
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))

    # Sort files alphabetically so the guide stays in order
    md_files.sort()

    # 3. Start building the HTML that will become the PDF
    # We use CSS to make it look professional (Cover page, headers, code blocks)
    html_body = """
    <html>
    <head>
    <style>
        @page {
            size: A4;
            margin: 20mm;
            @bottom-right { content: "Page " counter(page); font-family: sans-serif; font-size: 10pt; }
        }
        body { font-family: sans-serif; line-height: 1.6; color: #333; }
        .cover { height: 100vh; text-align: center; padding-top: 80mm; page-break-after: always; }
        .cover h1 { font-size: 32pt; color: #2c3e50; }
        .section-header { 
            background: #2c3e50; color: white; padding: 10px; 
            margin-top: 30px; border-radius: 5px; page-break-before: always;
        }
        .path { font-family: monospace; color: #2980b9; font-size: 10pt; margin-bottom: 20px; display: block; }
        pre { 
            background: #f4f4f4; border: 1px solid #ddd; padding: 15px; 
            border-radius: 5px; white-space: pre-wrap; font-size: 10pt; 
        }
    </style>
    </head>
    <body>
        <div class="cover">
            <h1>The Ultimate Python & Robotics Guide</h1>
            <p>A Complete Repository of Knowledge</p>
        </div>
    """

    # 4. Read the contents of every file found and add it to the PDF
    print(f"🔍 Scanning repository...")
    for filepath in md_files:
        print(f"📄 Adding: {filepath}")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Add the file content to our master HTML string
        html_body += f"""
        <div class="file-content">
            <div class="section-header">{os.path.basename(filepath)}</div>
            <span class="path">Location: {filepath}</span>
            <pre>{content}</pre>
        </div>
        """

    html_body += "</body></html>"

    # 5. Turn the final HTML string into a PDF
    print(f"🛠️ Compiling into {output_filename}...")
    HTML(string=html_body).write_pdf(output_path)
    print(f"✅ Done! Find your file in the '{output_dir}' folder.")

if __name__ == "__main__":
    compile_markdown_to_pdf()
