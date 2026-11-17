"""教学工作量的 CSV 读取、校验和汇总。所有数据仅用于课程实验。"""
import csv
from collections import defaultdict
from pathlib import Path


def read_records(path):
    """从 CSV 读取教学任务，校验教师、课程、课时和班级数。"""
    records = []
    with Path(path).open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        required = {"teacher", "course", "hours", "classes"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("CSV 缺少必要列：teacher/course/hours/classes")
        for rownum, row in enumerate(reader, start=2):
            teacher = (row.get("teacher") or "").strip()
            course = (row.get("course") or "").strip()
            if not teacher or not course:
                raise ValueError(f"第 {rownum} 行教师或课程名称为空")
            try:
                hours = int(row["hours"])
                classes = int(row["classes"])
            except (TypeError, ValueError) as ex:
                raise ValueError(f"第 {rownum} 行课时或班级数不是整数") from ex
            if hours <= 0 or classes <= 0:
                raise ValueError(f"第 {rownum} 行课时及班级数必须为正整数")
            records.append({
                "teacher": teacher, "course": course,
                "hours": hours, "classes": classes,
            })
    return records


def summarize(records):
    """按教师汇总工作量，公式为课时×班级数。"""
    totals = defaultdict(int)
    for record in records:
        totals[record["teacher"]] += record["hours"] * record["classes"]
    return dict(sorted(totals.items()))


def export_summary(path, totals):
    """将汇总结果导出为 Excel 友好的 UTF-8 BOM CSV。"""
    with Path(path).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["teacher", "workload"])
        for teacher, workload in totals.items():
            writer.writerow([teacher, workload])
