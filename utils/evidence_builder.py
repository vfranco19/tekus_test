import json
import os
from datetime import datetime

JSON_DIR = "evidence/json/"
os.makedirs(JSON_DIR, exist_ok=True)


class EvidenceCollector:
    """Recolector de evidencia de ejecucion de tests."""

    def __init__(self, on_step=None):
        self.execution_start = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.tests = []
        self.current_test = None
        self.on_step = on_step

    def start_test(self, test_name):
        self.current_test = {
            "name": test_name,
            "status": "PASS",
            "steps": [],
            "start_time": datetime.now().strftime("%H:%M:%S"),
        }
        if self.on_step:
            self.on_step(test_name, None)

    def end_test(self):
        if self.current_test:
            self.current_test["end_time"] = datetime.now().strftime("%H:%M:%S")
            self.tests.append(self.current_test)

            if self.on_step:
                self.on_step(
                    self.current_test["name"],
                    {
                        "description": f"TEST {self.current_test['status']}",
                        "status": self.current_test["status"],
                        "time": datetime.now().strftime("%H:%M:%S"),
                        "screenshot": None,
                    },
                )

            self.current_test = None

    def fail_test(self):
        if self.current_test:
            self.current_test["status"] = "FAIL"

    def add_step(self, description, status="PASS", screenshot=None):
        if not self.current_test:
            return

        if status == "FAIL":
            self.current_test["status"] = "FAIL"

        step = {
            "description": description,
            "status": status,
            "screenshot": screenshot,
            "time": datetime.now().strftime("%H:%M:%S"),
        }

        self.current_test["steps"].append(step)

        if self.on_step:
            self.on_step(self.current_test["name"], step)

    def save(self):
        data = {"execution_start": self.execution_start, "tests": self.tests}

        path = f"{JSON_DIR}execution_report.json"

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return path


collector = EvidenceCollector()
