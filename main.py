import os
import pandas as pd
import subprocess
from copy import copy

# Load participant names from CSV
csv_filename = "FINAL.csv"  # Ensure this file exists
participants = pd.read_csv(
    csv_filename, sep=";", names=["FirstName", "LastName", "Affiliation"], dtype=str
)

# LaTeX template with dummy event details, organizers, and dates
latex_template = r"""
\documentclass[a4paper]{article}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{setspace}
\usepackage{ragged2e}
\geometry{a4paper, total={170mm,5000mm}, left=20mm, top=2mm} 

\begin{document}

\linespread{1.5}
\null\vspace{50pt} 

\begin{center}
    \LARGE\textbf{Certificate of Participation}
\end{center}

\vspace{20pt}

\large
To whom it may concern,

\medskip
The representative of the Dummy Organizers at the Dummy University on behalf of the Organizing Committee of the Dummy Event 2025 hereby certifies that:

\begin{center}
    {\LARGE\textbf{ first_name last_name }}
\end{center}

participated in the \textbf{First Edition of the Dummy Event (12 hours)}, held in Dummy City, Country, from January 1 to January 2, 2025.

\vspace{20pt}
\noindent
Best Regards,

\vspace{10pt}
\noindent
\textbf{The Dummy Organizing Committee}
\vspace{0.5cm}

\begin{center}
    \includegraphics[width = 3cm]{firma_ivan.png}\hspace{1cm}
    \includegraphics[width = 5cm]{firma_ivan.png}\hspace{1cm}
    \includegraphics[width = 5cm, height = 2cm]{firma_ivan.png}
\end{center}
\begin{center}
    \includegraphics[width = 5cm]{firma_ivan.png}\hspace{1cm}
    \includegraphics[width = 5cm]{firma_ivan.png}
\end{center}

\vspace{0.5cm}
\noindent
January 3, 2025 \hfill Dummy City, Country

\vspace{.1cm}
\begin{center}
    \includegraphics[width=30mm]{LOGO_GNCS.png}\hspace{10mm}
    \includegraphics[width=30mm]{siam_logo_teal_cobranded_stack.png}\hspace{10mm}
    \includegraphics[width=30mm]{logo_imati_box.png}\hspace{10mm}
    \includegraphics[width=40mm]{MAIN_LOGO_suduerighe_1000x1000_Granata su bianco}
\end{center}
\vspace{8mm}
\begin{center}
    \includegraphics[width=30mm]{matematica_centrale_blu.png}\hspace{10mm}
    \includegraphics[width=30mm]{Logo_Politecnico_Milano.png}\hspace{10mm}
    \includegraphics[width=30mm]{logo_mathlab.png}
\end{center}

\end{document}
"""

# Create output directory
output_dir = "certificates"
os.makedirs(output_dir, exist_ok=True)

# Process each participant
for _, row in participants.iterrows():
    first_name, last_name = str(row["FirstName"]).strip(), str(row["LastName"]).strip()
    pdf_filename = f"{output_dir}/{first_name}_{last_name}.pdf"
    tex_filename = f"{output_dir}/{first_name}_{last_name}.tex"

    # Generate LaTeX file with dummy event details and participant names
    with open(tex_filename, "w") as tex_file:
        latex_template_tmp = copy(latex_template)
        latex_template_tmp = latex_template_tmp.replace("first_name", first_name)
        latex_template_tmp = latex_template_tmp.replace("last_name", last_name)
        tex_file.write(latex_template_tmp)

    # Compile LaTeX to PDF
    subprocess.run(
        ["pdflatex", "-output-directory", output_dir, tex_filename],
        stdout=subprocess.DEVNULL,
    )

    # Clean auxiliary files
    aux_extensions = [".aux", ".log", ".out", ".tex"]
    for ext in aux_extensions:
        aux_file = f"{output_dir}/{first_name}_{last_name}{ext}"
        if os.path.exists(aux_file):
            os.remove(aux_file)

print(f"Certificates generated in the '{output_dir}' folder.")
