# Context Engineering Lab - GitHub Copilot

Welcome to the Context Engineering Lab! This hands-on lab teaches you how to set up and use GitHub Copilot's context engineering features including custom instructions, custom agents, and prompt files to build a C++ application with AI assistance.

## 🎯 Lab Objectives

By completing this lab, you will learn how to:
- Set up project-wide context using custom instructions
- Create custom agents for planning and implementation
- Use prompt files to define reusable workflows
- Guide AI to generate high-quality, architecture-aligned code

## Prerequisites

To complete the hands-on labs, ensure you have the following:

### Required Software
- **Visual Studio Code** (Latest) – [Download here](https://code.visualstudio.com/)
- **GitHub Copilot** - VS Code extension ([github.copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) v1.284.0 or later)
- **GitHub Copilot Chat** - VS Code extension ([github.copilot-chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) v0.25.1 or later)
- **GitHub Pull Requests** - VS Code extension ([github.vscode-pull-request-github](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) 0.120.0 or later)
- **GitHub MCP Server** - VS Code extension for agentic workflows ([github.vscode-github-mcp](https://marketplace.visualstudio.com/items?itemName=github.vscode-github-mcp))
- **Git** – [Download here](https://git-scm.com/install/)

### Install the GitHub MCP server

1. Open the **Extensions** view

   * Press **Ctrl+Shift+X**.
   * In the search box, type **@mcp GitHub**.
   * Find **GitHub — Official GitHub MCP Server** and click **Install**.

2. Approve the authentication prompt

   * You will see a dialog, “The MCP Server Definition ‘github/github-mcp-server’ wants to authenticate to GitHub.”
   * Click **Allow**.

3. Pick your GitHub account

   * A quick pick appears asking which account to use.
   * Select your account, for example **YKhadas**.
   * VS Code will finish connecting the server.

4. Verify the server is running

   * Press **Ctrl+Shift+P** (Windows) or **Cmd+Shift+P** (Mac) to open the Command Palette.
   * Type **MCP: List Servers**, then press **Enter**.
   * In the list, confirm **github/github-mcp-server** shows **Running**.

5. Enable the server in Copilot Chat tools

   * Open the **GitHub Copilot Chat** panel.
   * Click the **Tools** icon at the bottom right of the chat window. It opens the **Configure Tools** picker.
   * In the list, find **MCP Server: github/github-mcp-server** and make sure it is **checked**.
   * Click **OK** to save.

You are set. If **github/github-mcp-server** does not show as Running, run **MCP: List Servers** again, or reload the window with **Developer: Reload Window**, then repeat step 5 to confirm the tool is checked.

### Create a fork of the repository 
### Create a feature branch 
Create a feature branch and push it to the repo. The changes you make will go on that branch, and you'll create a Pull Request later.

## 🏗️ Application Overview

In this lab, you'll implement a **Task Manager CLI** - a command-line task management application for developers. 

## 📚 Lab Structure

This repository contains the context engineering setup:

### Documentation Files
- **PRODUCT.md** - Product vision, features, and goals
- **ARCHITECTURE.md** - System design and architectural patterns
- **CONTRIBUTING.md** - Code style, best practices, and guidelines

### Custom Instructions
- **.github/copilot-instructions.md** - Project-wide context automatically included in all AI interactions

### Custom Agents
- **.github/agents/plan.agent.md** - Planning agent for creating implementation plans
- **.github/agents/tdd.agent.md** - TDD implementation agent for writing code

### Templates
- **plan-template.md** - Template structure for implementation plans

### Prompt Files
- **.github/prompts/plan-qna.prompt.md** - Planning prompt with clarifying questions

## 🚀 Lab Steps

### Step 1: Explore the Context Engineering Setup

1. **Review the documentation files** to understand the project:
   - Open `PRODUCT.md` and read about the Task Manager's features and goals
   - Open `ARCHITECTURE.md` to understand the layered architecture design
   - Open `CONTRIBUTING.md` to learn the C++ coding standards

2. **Examine the custom instructions**:
   - Open `.github/copilot-instructions.md`
   - Notice how it references the documentation files
   - These instructions are automatically included in all Copilot interactions

3. **Review the custom agents**:
   - Open `.github/agents/plan.agent.md` - specialized for planning
   - Open `.github/agents/tdd.agent.md` - specialized for TDD implementation
   - Notice the handoff configuration from planning to implementation

4. **Check the templates and prompts**:
   - Open `plan-template.md` to see the implementation plan structure
   - Open `.github/prompts/plan-qna.prompt.md` for the clarifying questions prompt
  
### Step 2: Add custom instructions for testing guidelines:
From VS Code command palette:

#### Visual Guide
![Lab Instructions](img/lab%20instructions.png)

### Step 3: Create an Implementation Plan

Now you'll use the planning agent to create a detailed implementation plan.

1. **Open GitHub Copilot Chat** in VS Code

2. **Select the `plan` agent** from the agent picker in the chat interface

3. **Alternatively, use the prompt file** by typing:
   ```
   /plan-qna Add a Task Manager CLI application for managing tasks
   ```

4. **Or directly ask the plan agent**:
   ```
   @plan Create an implementation plan for the Task Manager CLI application as described in PRODUCT.md
   ```

5. **Answer any clarifying questions** the agent asks

6. **Review the generated plan**:
   - Does it follow the plan-template.md structure?
   - Does it break down into clear, actionable tasks?
   - Does it align with ARCHITECTURE.md design?

### Step 3: Implement Using Agent Mode

Once the implementation plan is ready, use the TDD implementation agent to write the code.

1. Switch to the implementation agent:

In Copilot Chat, choose the TDD implementation agent configured in .github/agents/tdd.agent.md, or
Use the handoff link in the planning agent’s response (for example: “Start Implementation”).

2. **Let the agent work autonomously**:
   - The agent will create files, write code, and build the application
   - It will follow the architecture in ARCHITECTURE.md
   - It will adhere to code style in CONTRIBUTING.md
   - Watch as it implements each component

3. **Review the implementation**:
   - Check that files are created in the correct structure
   - Verify code follows the C++17 standard and style guide
   - Confirm tests are included (if TDD agent was used)

### Step 4: Build and Test the Application

1. **Build the application**:
 
2. **Add some tasks**:

3. **List tasks**:
   
4. **Complete a task**:
  
### Step 5: Add a Document Agent
Create a complete workflow, add a Document agent:

1. Plan agent creates detailed plan
2. TDD agent implements with tests
3. Document agent updates documentation

#### Visual Guide
![Lab Instructions](img/custom%20agent.png)

**Commit changes**

**Create PR**

## Exercise 8 — Copilot as a Reviewer

**Where you work:** On **GitHub.com**, inside your open Pull Request.

**Checklist:**

* [ ] Navigate to your GitHub repository on GitHub.com
* [ ] Open the PR created 
* [ ] Assign Copilot as a reviewer to PR

#### Visual Guide
![Lab Instructions](img/review.png)


## Exercise 9 — Use MCP server
Go back to VS Code IDE. 
Let's use Github MCP server. 

In Agent Mode, ask to review the application and provide list of improvements. 

Prompt: 

Next prompt: 
For the first top 3 improvements create an issue on github. 

The MCP server should create the issues. 
Go to github.com and valide that issues were created. 


## Exercise 10 — Assign Coding agent for a selected issue
**Where you work:** On **GitHub.com**, in the Issue UI.

**What and why:**
Copilot Agents can take an issue, create a branch, and open a draft PR with code changes. This exercise lets you hand off your feature request and observe Copilot’s automation.

**Checklist:**

* [ ] Open the issue you created in Exercise 9
* [ ] Assign it to **Copilot** (Coding Agent)
* [ ] Observe as Copilot opens a branch and draft PR implementing the feature

### 1. Assign the issue to Coding Agent
1. **Open your GitHub repository** in your browser and navigate to the **Issues** tab
2. **Click on the issue** you created in Exercise 9 (e.g., "Add Nutrition Info to Recipe Details")
3. **In the right-hand panel**, look for the **"Assignees"** section
4. **First, assign yourself** by clicking "Assign yourself" - this ensures you'll get notifications and maintain ownership
5. **Then, click the "Assign to Copilot" button** - this adds Copilot as a co-assignee to implement the feature
6. Both you and Copilot should now be listed as assignees

This will trigger the automated workflow where Copilot begins implementing your feature request while you maintain oversight and responsibility for the final outcome.


TODO: Agents file
#### Visual Guide
![Lab Instructions](img/coding%20agent.png)


### 2. Observe the automation

Watch as Copilot opens a branch and draft PR implementing the feature automatically. The Agent follows the patterns defined in your `AGENTS.md` file to ensure code consistency.

### That is it for today, well done!

### Best Practices Learned
1. **Start with clear documentation** - Product, Architecture, Contributing
2. **Use custom instructions** - Automatic context for all interactions
3. **Create specialized agents** - Separate planning from implementation
4. **Define templates** - Ensure consistent output structure
5. **Iterate and refine** - Update context based on observed AI behavior

### Custom Agents vs Tools
- **Custom agents** have specialized personas and workflows
- **Handoffs** create guided transitions between agents
- **Prompt files** add variants to the same workflow
- **Instructions** provide persistent, project-wide context

