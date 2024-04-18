# Git version controller

Git is a distributed version control system widely used for tracking changes in source code during software development. It was created by Linus Torvalds in 2005 to manage the Linux kernel development.

In essence, Git allows multiple developers to collaborate on a project efficiently by providing features like branching, merging, and version tracking. Each developer can work on their own branch of the codebase without interfering with others' work. Then, when they're ready, they can merge their changes back into the main codebase.

Git stores these changes in a repository, which can be local or remote. It also allows for easy collaboration by facilitating operations like cloning repositories, pulling changes from a remote repository, and pushing changes to it.

Its popularity stems from its speed, flexibility, and robustness, making it an essential tool in modern software development workflows.

### Mercurial

Mercurial is another distributed version control system (DVCS) similar to Git. Like Git, it allows multiple developers to collaborate on a project by tracking changes to source code files. It was created by Matt Mackall in 2005, around the same time as Git, and it's also used for managing software development projects.

Mercurial shares many similarities with Git in terms of its functionality, including features like branching, merging, and version tracking. However, there are some differences in their usage and implementation details.

One notable difference is in their underlying data structures and the way they store changes. While Git uses a content-addressable filesystem with a directed acyclic graph (DAG) to represent the commit history, Mercurial uses a different approach based on a more traditional model with revisions and file snapshots.

Despite these differences, both Git and Mercurial serve the same fundamental purpose: to facilitate collaborative software development by providing tools for version control and team coordination. The choice between Git and Mercurial often comes down to personal preference or specific project requirements.


## Installing Git

### Linux
For Debian/Ubuntu-based distributions, you can install Git using the package manager. Open a terminal and run:

```console
$ sudo apt install git
```
For Fedora, CentOS, or RHEL-based distributions:

```console
$ sudo yum install git
```

### MacOS
Git typically comes pre-installed with macOS. However, you can also install it via Homebrew if needed:
```console
$ brew install git
```

### Windows

You can download and install Git for Windows from the official Git website, [**Git for Windows**](https://gitforwindows.org) and follow the installation instructions provided by the installer.

After installation, verify that Git is installed correctly by running `git --version` in your terminal or command prompt. You should see the version number displayed.

Once Git is installed, you can start using it for version control in your projects.

## Configuring Git

After installing Git, you typically need to configure it with your name and email address. This information is used to identify you as the author of commits in the repositories you work with. Here's how you can configure Git:

1. **Open a terminal or command prompt**
2. **Set your username**: Run the following command, replacing "Your Name" with 
your actual name:

    ```console
    $ git config --global user.name "Your Name"
    ```


3. **Set your email address**: Run the following command, replacing "your_email@example.com" with your actual email address: 
    ```console
    $ git config --global user.email "your_email@example.com"
    ```
    This email address will be associated with your commits.

4. (*Optional*) **Set your preferred text editor**: If you prefer to use a text editor other than the default one, you can configure it using:

    ```console
    $ git config --global core.editor "editor_name"
    ```
    Replace "editor_name" with the command to launch your preferred text editor. For example, if you want to use Vim, you would use:
    ```console
    $ git config --global core.editor "vim"
    ```
5. **Verify your configuration**: You can verify that your Git configuration is set correctly by running:
    ```console
    $ git config --list
    ```
    This command will display a list of all your Git configurations.

Once you've completed these steps, your Git installation is configured and ready to use. You can start using Git to manage your repositories and collaborate with others.



## Git commands

Here are some essential Git commands along with examples and brief explanations for each:

- git init
  - Example: `git init`
  - Explanation: Initializes a new Git repository in the current directory. This command creates a hidden directory named .git where Git stores its metadata and version history.

- git clone
  - Example: `git clone <repository_url>`
  - Explanation: Copies an existing Git repository from a remote server to your local machine. You provide the URL of the remote repository as an argument. This command is used for creating a local copy of a remote repository.

- git add
  - Example: `git add file.txt`
  - Explanation: Adds changes in the specified file to the staging area. Before committing changes, you need to add them to the staging area using git add. This command stages changes for the next commit.

- git commit
  - Example: `git commit -m "Commit message"`
  - Explanation: Records the changes in the staging area as a new commit in the version history. You need to provide a meaningful commit message that describes the changes made in the commit.

- git status
  - Example: `git status`
  - Explanation: Displays the current state of the repository, including tracked/untracked files and changes staged for commit. It helps you understand what's happening in your repository.

- git push
  - Example: `git push origin main`
  - Explanation: Uploads local repository changes to a remote repository. This command is used to push committed changes from your local branch to the corresponding branch on the remote repository.

- git pull
  - Example: `git pull origin main`
  - Explanation: Fetches changes from a remote repository and merges them into the current branch. This command is used to update your local repository with changes made by others.

- git branch
  - Example: `git branch feature`
  - Explanation: Lists existing branches or creates a new branch. Branches are independent lines of development in Git. This command helps you manage branches in your repository.

- git checkout
  - Example: `git checkout feature`
  - Explanation: Switches to a different branch. It allows you to navigate between branches or restore files from different commits or branches.

- git merge
  - Example: `git merge feature`
  - Explanation: Combines changes from one branch into another. This command is used to integrate changes from one branch into another branch, typically the main branch.

These are some of the fundamental Git commands that are commonly used in day-to-day development workflows. Mastering these commands will give you a solid foundation for working with Git effectively.

## Git Advanced commands

- git rebase
  - Example: git rebase main
  - Explanation: Reapplies commits on top of another base tip. It allows you to rewrite commit history by moving, combining, or squashing commits. Rebasing is useful for keeping a clean and linear commit history.

- git cherry-pick
  - Example: git cherry-pick <commit_hash>
  - Explanation: Picks a single commit from one branch and applies it to another. This command allows you to apply specific commits to different branches without merging entire branches.

- git reset
  - Example: git reset --hard HEAD~2
  - Explanation: Resets the current branch to a specified state. It can be used to undo changes in the working directory, staging area, or commit history. The --hard option resets both the working directory and the staging area to the specified state.

- git stash
  - Example: git stash save "Work in progress"
  - Explanation: Temporarily shelves changes in the working directory. It allows you to store changes without committing them, making it easier to switch branches or work on different tasks. Stashed changes can be reapplied later using `git stash apply` or `git stash pop`.

- git bisect
  - Example: 
    ```console
    git bisect start
    git bisect good <commit_hash>
    git bisect bad <commit_hash>
    ```
  - Explanation: Helps find the commit that introduced a bug. It performs a binary search through the commit history to identify the first bad commit. You mark commits as `good` or `bad`, and Git narrows down the range where the bug was introduced.

- git submodule
  - Example: `git submodule add <repository_url>`
  - Explanation: Manages Git repositories as submodules within your main repository. Submodules allow you to include external repositories as dependencies in your project. This command adds a `submodule` to your project.

- git reflog
  - Example: `git reflog`
  - Explanation: Records changes to the tip of branches over time. It's a log of reference updates in the repository, including commits that are no longer referenced by any branch. The `reflog` can help you recover lost commits or undo accidental changes.

- git filter-branch
  - Example: `git filter-branch --tree-filter 'rm -f passwords.txt' HEAD`
  - Explanation: Rewrites branches to apply custom filters. It can be used to rewrite commit history by applying various filters, such as removing sensitive information, rewriting file paths, or splitting commits.

- git submodule update
  - Example: `git submodule update --init --recursive`
  - Explanation: Updates submodules in your repository to the latest commits. This command fetches and merges changes from submodule repositories, ensuring that your project's submodules are up to date.

- git worktree
  - Example: `git worktree add ../branch-2 branch-2`
  - Explanation: Allows multiple working directories for the same repository. This command creates additional working trees linked to the same repository, enabling you to work on multiple branches simultaneously without switching back and forth.

These advanced Git commands offer powerful functionality for managing complex development workflows, collaborating with others, and maintaining a clean and organized repository history. However, they also come with a greater risk of causing unintended changes, so it's essential to use them with caution and understand their implications.

## Git workflow

A Git workflow defines a set of rules or procedures that guide how developers collaborate on a project using Git for version control. There are various Git workflows, each tailored to meet specific project requirements, team size, and development practices. Here's an overview of a commonly used Git workflow, the "Feature Branch Workflow":

1. **Master Branch**: The master branch represents the mainline or production-ready version of the project. It should always contain stable, working code.

2. **Feature Branches**: Developers create a new branch for each feature, bug fix, or task they are working on. These branches are typically named descriptively to reflect the feature or issue they address. Branches are created off the master branch or, in some cases, from a development branch if present.

3. **Development Cycle**: Developers work independently on their feature branches, implementing new features, fixing bugs, or making changes as required. Regular commits are made to the feature branch to track progress and maintain a detailed history of changes.

4. **Code Review**: Once a feature is implemented or a bug is fixed, developers open a pull request (PR) or merge request (MR) to propose changes to the master branch.Other team members review the code changes, provide feedback, and ensure adherence to coding standards and project requirements.

5. **Integration**: After the code review process, the feature branch is merged into the master branch or another designated integration branch. Continuous integration (CI) tools may be used to automate testing and ensure that the merged changes do not introduce regressions or conflicts.

6. **Deployment**: Once changes are integrated and tested, they can be deployed to production or staging environments. Deployment may involve additional steps such as version tagging, release notes generation, and database migrations.

7. **Maintenance**: After deployment, the master branch may require maintenance, such as hotfixes for critical issues or updates for new features. Developers create new branches for maintenance tasks, following a similar workflow as for feature branches.

Key benefits of the Feature Branch Workflow include:

- Isolation: Each feature or fix is developed in isolation, minimizing conflicts and simplifying collaboration.
- Code Review: Encourages peer review, leading to higher code quality and knowledge sharing among team members.
- Stability: The master branch remains stable and production-ready at all times, as only tested and reviewed changes are merged into it.

While the Feature Branch Workflow is popular and widely adopted, it's essential to choose a workflow that best suits your team's needs, project complexity, and development practices. Other common Git workflows include Gitflow, Forking Workflow, and Centralized Workflow, each with its own advantages and considerations.
