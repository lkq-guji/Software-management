# 教学工作量管理系统｜软件项目管理实验3：配置管理

> 课程实验项目，数据均为虚构示例。主要用于演示 Git 环境搭建、仓库与工作流、远程推送、克隆、分支及版本标签，不代表生产教务系统。

## 仓库与运行环境
- 仓库：https://github.com/lkq-guji/Software-management
- Python 3.9+、Git 2.x；无需第三方依赖
- Windows Git Bash / PowerShell 均可运行

```bash
git clone https://github.com/lkq-guji/Software-management.git
cd Software-management
python app.py summary --file data/workload.csv
python -m unittest discover -s tests -v
```

## 初始功能
读取 CSV 教学任务，验证数据，根据 `工作量 = 课时 × 班级数` 按教师汇总，支持查询教师、导出 CSV。后续功能和测试由小组成员通过独立分支开发。

## 四人小组分工
| 角色 | 工作分支 | 修改范围 |
|---|---|---|
| 组长 | `docs/leader-release` | `docs/配置管理计划.md`、PR 审核、发布标签及实验报告 |
| 组员 A | `docs/requirements` | `docs/需求说明.md`、`docs/配置项清单.md` |
| 组员 B | `feature/course-statistics` | `workload.py`、`app.py` |
| 组员 C | `test/coverage-ci` | `tests/`、`docs/测试报告.md`、`.github/workflows/` |

先从 `main` 创建自己的分支，完成改动、运行测试、以本人 Git 身份提交并 push，然后创建指向 `main` 的 Pull Request。组长审核后才合并并打版本标签。

## 实验任务与证据
1. 环境搭建：`git --version`、`git config --list --show-origin`（截图前注意隐私）
2. 仓库及工作流：`git status`、`git log --oneline --graph --all`
3. 远程仓库：`git remote -v`、`git push`
4. 克隆仓库：`git clone`、`git status`
5. 分支和标签：`git branch -a`、`git tag -n`、GitHub Pull Request 和 Tags 页面

## 注意事项
- 不要上传真实学生信息、密码、Token 或课程之外的无关文件。
- 不要冒充其他组员提交，勿强制推送或重写历史。
- 在其他组员未真实推送前，不要将其工作标为“已完成”。
- 本仓库公开可见。组员如需保密，先由组长调整仓库权限。
