# Autom – AI-Powered Workflow & Personal Assistant

Autom is a Gemini-powered agent built on **n8n** that automates workflows across multiple domains. It integrates Gmail, Google Calendar, Google Contacts, and web forms to streamline productivity tasks. In addition, Autom includes a custom local automation server that can directly control the laptop environment, enabling actions such as launching applications, browsing websites, and executing scripted sequences.

---

## Overview

Autom combines large language model reasoning with workflow automation. The system routes natural language instructions to the appropriate tools or workflows. It can:

- Automate email communication through Gmail.
- Manage scheduling and reminders with Google Calendar.
- Create and update Google Contacts programmatically.
- Respond automatically to form submissions.
- Execute desktop automation tasks through a custom Flask server.

---

## Architecture

```
+----------------------+       +---------------------+
|    Gemini AI Agent   | <---> |         n8n         |
+----------------------+       +---------------------+
         |                             |
         v                             v
  [Email Agent]                 [Calendar Agent]
  [Contact Agent]               [Workflow Agent]
         |                             |
         v                             v
+---------------------------------------------------+
| Custom Flask Server (Local Automation Layer)      |
| Executes instructions via PyAutoGUI / Webbrowser  |
+---------------------------------------------------+
```

---

## Workflows

### 1. Email Agent
Autom manages Gmail tasks such as sending, replying, and retrieving emails. It uses Gemini to determine intent and n8n to execute the actions.

*Screenshot Placeholder*

### 2. Calendar Agent
Autom integrates with Google Calendar to create, update, and delete events. It can be used to schedule meetings or reminders automatically.

*Screenshot Placeholder*

### 3. Contact Agent
This workflow manages Google Contacts by creating, updating, or retrieving contact information directly through connected APIs.

*Screenshot Placeholder*

### 4. Form Response Agent
Autom can respond to submissions from external contact forms. Based on the submission, it can trigger workflows such as sending a confirmation email or scheduling a follow-up meeting.

*Screenshot Placeholder*

### 5. Local Automation Server
Autom includes a Flask-based server that receives structured arrays of instructions from the agent. These are executed on the local machine using PyAutoGUI and webbrowser, enabling true desktop-level automation.

*Screenshot Placeholder*

---

## Technology Stack

- **AI and Orchestration**: Google Gemini, n8n
- **Backend Automation**: Flask, PyAutoGUI, webbrowser
- **Integrations**: Gmail API, Google Calendar API, Google Contacts API
- **Planned Extensions**: Playwright for advanced browser automation

---

## Future Enhancements

- Integration of Playwright for robust browser control.
- Expansion to include more APIs (Google Drive, Slack, etc.).
- Voice-based interaction capabilities.
- Deployment of the local automation server for remote access.

---

## Author

**Srinivasan L**  
[Portfolio](https://srinivasan.vercel.app) | [LinkedIn](https://linkedin.com/in/srlog) | [GitHub](https://github.com/srlog)
