

# How We Work on This Project (Peer Notes)

Hey! Here’s a quick rundown of how we handle branches, commits, and general workflow in this repo. This isn’t corporate boilerplate—just what’s worked well for us and should make life easier for anyone jumping in.


## Branching: Keep It Simple

We stick to GitHub Flow:
- The `main` branch is always stable—don’t break it!
- For anything new (feature, fix, docs), make a branch with a clear name, like `feature/login-form` or `fix/quote-bug`.
- Do your work there, commit as you go (see below), and when you’re happy, push and open a pull request (PR).
- PRs are where we review, chat, and merge. Don’t be shy about asking for a review or feedback.

**Typical steps:**
1. `git checkout -b feature/something-cool`
2. Make changes, commit often (see next section).
3. `git push origin feature/something-cool`
4. Open a PR, tag someone if you want a second set of eyes.

This keeps things organized and makes it easy to see what’s being worked on. Plus, if something goes wrong, it’s easy to roll back.


## Commits: One Change, One Commit

Try to keep each commit focused—fix one thing, add one feature, etc. It makes it way easier to review and debug later. For messages, we use this style:

`type(scope): short description`

Examples:
- `feat(api): add quote calculation endpoint`
- `fix(form): validate age input`
- `docs(readme): clarify setup instructions`

Types you’ll see: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, etc. Scope is optional but helps.

Why bother? Because when you look back, you’ll thank yourself for making things easy to follow. Plus, it’s a lifesaver if you ever need to revert something.


## If We Were Shipping to Production

Some things we’d want to do for a real-world launch:
- Use environment variables for secrets and config (never hardcode them).
- Add proper error handling and input checks—don’t trust user input!
- Write tests (unit, integration, maybe end-to-end if it grows).
- Set up CI/CD so tests run automatically before merging.
- Swap Flask’s built-in server for something like Gunicorn.
- Document the API and how to use it.
- Add logging and monitoring so we know if things break.


## Want to Improve Something?

If you spot a way to make this process better, or want to suggest a change:
- Open an issue or start a discussion—just say what you’re thinking and why.
- For bigger changes, explain the benefit and how it’ll help us all.
- Stick to the same branch/commit style so it’s easy for everyone to follow.

---

This isn’t set in stone—if you have ideas, let’s talk! The goal is to keep things clean, easy to work on, and friendly for anyone who joins in.
