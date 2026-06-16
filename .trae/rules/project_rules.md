# Git Workflow Rules

## Mandatory: After Every Task Completion

After completing any code modification task and verifying the code is correct, you MUST:

1. **Create a new branch** from `main` for each task:
   - Branch naming convention: `<YYYYMMDD>_<修改标题总结>`
   - Example: `20260510_更新域名和邮箱`, `20260511_修复计数器NaN问题`
   - 时间格式为年月日，标题用中文简要概括本次修改内容

2. **Commit changes** to the new branch:
   - Stage all modified files: `git add -A`
   - Commit with a descriptive message: `git commit -m "<type>: <description>"`
   - Commit message types: `feat`, `fix`, `style`, `refactor`, `docs`, `chore`
   - Use English for commit messages

3. **Push the new branch** to remote:
   - `git push -u origin <branch-name>`

4. **Switch back to main** after pushing:
   - `git checkout main`

## Git Configuration
- Remote repository: https://github.com/pdduhddodjdkdkdd4-arch/levinlawlaw.git
- User: pdduhddodjdkdkdd4-arch
- Email: pdduhddodjdkdkdd4@gmail.com
- Default branch: main

## Workflow Example
```bash
# Start of task
git checkout main
git checkout -b 20260510_更新域名和邮箱

# ... make code changes ...

# After verifying code is correct
git add -A
git commit -m "feat: update domain and email"
git push -u origin 20260510_更新域名和邮箱
git checkout main
```

## Important Notes
- NEVER commit directly to `main` branch for task changes
- ALWAYS verify code correctness before committing (run lint/typecheck if available)
- ALWAYS create a new branch for each independent task
- If a task involves multiple related changes, they can share the same branch
