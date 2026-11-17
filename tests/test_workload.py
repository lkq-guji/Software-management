"""项目基线测试；后续由测试负责人补充边界测试。"""
import tempfile
import unittest
from pathlib import Path

from workload import export_summary, read_records, summarize


class WorkloadTests(unittest.TestCase):
    def test_read_and_summarize(self):
        result = summarize(read_records("data/workload.csv"))
        self.assertEqual(result, {"张老师": 88, "李老师": 48, "王老师": 64})

    def test_export_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "result.csv"
            export_summary(path, {"张老师": 88})
            self.assertIn("张老师,88", path.read_text(encoding="utf-8-sig"))

    def test_invalid_hours(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text("teacher,course,hours,classes\n张老师,测试课,0,1\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_records(path)

    def test_missing_columns(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.csv"
            path.write_text("teacher,course\n张老师,测试课\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_records(path)


if __name__ == "__main__":
    unittest.main()
