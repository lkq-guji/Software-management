"""教学工作量统计 CLI 入口：python app.py summary --file data/workload.csv。"""
import argparse

from workload import export_summary, read_records, summarize


def main(argv=None):
    parser = argparse.ArgumentParser(description="教学工作量管理系统（课程实验）")
    commands = parser.add_subparsers(dest="command", required=True)
    summary = commands.add_parser("summary", help="汇总每位教师的教学工作量")
    summary.add_argument("--file", default="data/workload.csv")
    summary.add_argument("--teacher", help="按教师姓名过滤")
    summary.add_argument("--export", help="将汇总结果导出到 CSV")
    args = parser.parse_args(argv)
    totals = summarize(read_records(args.file))
    if args.export:
        export_summary(args.export, totals)
        print(f"汇总已导出：{args.export}")
    for teacher, workload in totals.items():
        if not args.teacher or teacher == args.teacher:
            print(f"{teacher}: {workload} 工作量单位")


if __name__ == "__main__":
    main()
