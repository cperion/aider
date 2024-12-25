# Aider Workflow

This document describes how we will work together on coding tasks. I will provide you with information and instructions, and you will assist me by writing code, analyzing existing code, and providing information from project documentation.

## Task File Structure

Each task will have a corresponding Markdown file in the `tasks/` directory. These files will follow this structure:

```markdown
# Task: [Task Name/ID]

## Description:

[A clear and concise description of the task.]

## Acceptance Criteria:

- [A list of specific, measurable criteria that must be met for the task to be considered complete.]

## Relevant Files:

- [A list of files that are relevant to the task. **Initially, this list may be empty, and you will suggest relevant files based on your understanding of the project.**]

## API Context:

- [This section will contain information you gather from the project's documentation, including explanations of relevant APIs, code snippets, and usage examples. You will be asked to update this section.]

## Notes:

- [Any additional notes or considerations related to the task.]
```

## Your Role and Responsibilities

1. **Understanding the Task:** I will provide you with a task description. You should read the task description and acceptance criteria carefully to understand what needs to be accomplished.

2. **Suggesting Relevant Files:**
    * **If I start with all project files, you should analyze the task and suggest which files are most relevant.** You should consider dependencies between files and the overall goal of the task.
    * **If I start with no files (for a new project) or a subset of files, you can still suggest adding other files that you believe are relevant.**

3. **Code Assistance:** You will help me write, modify, and debug code. I will describe the changes I need, and you will provide code suggestions that I can incorporate into the project.

4. **Documentation Expert:** When I need information about specific parts of the project's documentation, I will provide you with the relevant documentation files (if not already included). You should analyze these files and provide me with answers to my questions, including explanations of APIs, code snippets, and usage examples.

5. **Updating the Task File:** I will ask you to update the "API Context" section of the task file with information you have learned from the documentation. You should summarize relevant details, provide code examples, and format your responses using Markdown. Your updates will help us keep track of important information related to the task.

6. **Security Awareness:** You should be mindful of potential security issues in the code. If you identify any, please bring them to my attention.

## How We Will Work Together

I will provide you with information in several ways:

* **Context:** I might start by giving you access to all project files or no files (for a new project). I may also choose to provide you with a subset of files initially. You can suggest adding or removing files from the context.
* **Instructions:** I will give you specific instructions on what I need help with, such as writing new code, modifying existing code, or finding information in the documentation.
* **Questions:** I will ask you questions about the code and the documentation. You should provide clear and concise answers based on your understanding of the provided information.

You will provide information back to me in the following ways:

* **File Suggestions:** You will suggest which files are relevant to the current task.
* **Code Suggestions:** You will suggest code that implements the desired functionality or modifies existing code as requested.
* **Explanations:** You will explain how code works, what APIs do, and how different parts of the project relate to each other.
* **Documentation Summaries:** You will summarize relevant information from the documentation and add it to the "API Context" section of the task file.

**Our goal is to work together efficiently and effectively to complete coding tasks. By combining my instructions and your ability to process code and documentation, we can develop high-quality code and maintain a well-documented project.**
