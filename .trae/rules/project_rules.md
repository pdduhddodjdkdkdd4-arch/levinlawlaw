# Git Workflow Rules

## Mandatory: After Every Task Completion

After completing any code modification task and verifying the code is correct, you MUST:

1. **Create a new branch** from `main` for each task:
   - Branch naming convention: `feature/<brief-description>` or `fix/<brief-description>`
   - Example: `feature/fix-counter-nan`, `fix/contact-form-validation`
   - Use English for branch names, keep them concise and descriptive

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
git checkout -b feature/add-dark-mode

# ... make code changes ...

# After verifying code is correct
git add -A
git commit -m "feat: add dark mode toggle"
git push -u origin feature/add-dark-mode
git checkout main
```

## Important Notes
- NEVER commit directly to `main` branch for task changes
- ALWAYS verify code correctness before committing (run lint/typecheck if available)
- ALWAYS create a new branch for each independent task
- If a task involves multiple related changes, they can share the same branch
