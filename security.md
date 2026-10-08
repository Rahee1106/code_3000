# Security Statement

Maintained by: Rahee Patel (@Rahee1106)

## Intended Users

This repo holds my CSE 3000 homework. It's meant for me, since I'm the one working on it, and for my instructor and TAs, who grade what I turn in.

## Risk Assessment

The risk is low. There's no personal, financial, or private data here. The main concerns are someone changing or deleting the code, which would wipe out my work, or someone copying my homework and turning it in as their own. If a password or API key ever got committed, that could also be misused, so I keep those out of the repo.

## Security Steps

I updated the CODEOWNERS file to name me (@Rahee1106) as the owner of every file, so nothing changes without my approval.

I also set up a ruleset on the main branch called "Pull request approvals." It stops anyone from deleting main or force pushing, requires every change to go through a pull request, and requires a code owner to review it before it merges.
