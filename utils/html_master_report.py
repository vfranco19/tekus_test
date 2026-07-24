import json
import os
from pathlib import Path
import shutil

REPORT_DIR = "evidence/reports/"
JSON_DIR = "evidence/json/"
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(JSON_DIR, exist_ok=True)


def limpiar_json():
    """Elimina los archivos JSON anteriores."""
    carpeta = Path(JSON_DIR)
    if carpeta.exists():
        for item in carpeta.iterdir():
            if item.is_file():
                item.unlink()
            else:
                shutil.rmtree(item)


def generate_master_report(json_path):
    """Genera un reporte HTML a partir del JSON de evidencia."""
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    html = f"""
    <html>
    <head>
        <title>Execution Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f4f6f8;
                color: #222;
            }}
            h1 {{ margin-bottom: 5px; }}
            .pass {{ color: #16a34a; font-weight: bold; }}
            .fail {{ color: #dc2626; font-weight: bold; }}
            .accordion {{
                background-color: #ffffff;
                cursor: pointer;
                padding: 16px;
                width: 100%;
                border: none;
                text-align: left;
                font-size: 17px;
                border-radius: 10px;
                margin-top: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                transition: 0.2s;
            }}
            .accordion:hover {{ background-color: #f1f5f9; }}
            .accordion:after {{ content: '+'; float: right; font-weight: bold; font-size: 20px; }}
            .accordion.active:after {{ content: "\\2212"; }}
            .panel {{
                padding: 0 18px;
                background-color: white;
                max-height: 0;
                overflow: hidden;
                transition: max-height 0.3s ease-out;
                border-radius: 0 0 10px 10px;
                margin-bottom: 20px;
            }}
            .panel.open {{ padding: 16px; }}
            .panel p {{ margin: 6px 0; line-height: 1.4; }}
            .img-preview {{
                width: 260px;
                border-radius: 10px;
                border: 2px solid #ddd;
                margin-top: 8px;
                cursor: pointer;
                transition: transform .15s ease, box-shadow .15s ease;
            }}
            .img-preview:hover {{
                transform: scale(1.03);
                box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            }}
            #modal {{
                display:none; position:fixed; z-index:9999;
                left:0; top:0; width:100%; height:100%;
                background-color: rgba(0,0,0,0.88);
                justify-content:center; align-items:center;
            }}
            #modal-img {{
                max-width:92%; max-height:92%;
                border-radius:12px; border:4px solid #e5e7eb;
                box-shadow:0 0 25px rgba(0,0,0,0.6);
            }}
        </style>
    </head>
    <body>
        <h1>Execution Report</h1>
        <p><strong>Start:</strong> {data['execution_start']}</p>
        <hr>
    """

    for test in data["tests"]:
        status_class = "pass" if test["status"] == "PASS" else "fail"
        html += f"""
        <button class="accordion">
            {test['name']} -
            <span class="{status_class}">{test['status']}</span>
        </button>
        <div class="panel">
        """
        for step in test["steps"]:
            step_class = "pass" if step["status"] == "PASS" else "fail"
            html += f"""
            <p>
                <strong>{step['time']}</strong> —
                {step['description']} —
                <span class="{step_class}">{step['status']}</span>
            </p>
            """
            if step["screenshot"]:
                html += f'''
                <img class="img-preview"
                     src="../screenshots/{step["screenshot"]}"
                     onclick="openModal(this.src)">
                '''
        html += "</div>"

    html += """
        <div id="modal" onclick="closeModal()">
            <img id="modal-img">
        </div>
        <script>
            document.querySelectorAll(".accordion").forEach(btn => {
                btn.addEventListener("click", () => {
                    btn.classList.toggle("active");
                    const panel = btn.nextElementSibling;
                    if (panel.style.maxHeight) {
                        panel.style.maxHeight = null;
                        panel.classList.remove("open");
                    } else {
                        panel.style.maxHeight = panel.scrollHeight + "px";
                        panel.classList.add("open");
                    }
                });
            });
            function openModal(src) {
                document.getElementById("modal").style.display = "flex";
                document.getElementById("modal-img").src = src;
            }
            function closeModal() {
                document.getElementById("modal").style.display = "none";
            }
        </script>
    </body>
    </html>
    """

    os.makedirs(REPORT_DIR, exist_ok=True)
    report_path = f"{REPORT_DIR}execution_report.html"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html)

    return report_path
