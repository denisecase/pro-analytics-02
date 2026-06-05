# AI Power, Capability, and Governance

AI tools are rapidly becoming part of professional work.

AI can be an excellent resource to help explain concepts, draft code,
summarize errors, improve documentation, generate tests, or review project work.
Used well, AI can help us learn faster and work more efficiently.

But like all power tools, AI must be used responsibly.

## Early Generative AI (Reply to Requests)

Modern AI took a noticeable leap with large language models (LLM).
These systems were trained on massive text and
recursively apply "predict the next part of speech"
to produce text that emulated human conversation.
The public release of OpenAI's ChatGPT and similar products
made this capability widely available.

These large language model (LLM) chatbots could respond quite well
to prompts or questions from the user.
Except for some repeating patterns and tells, they can appear quite similar
to human-generated text.
These chatbots can explain ideas, answer questions,
summarize text, suggest code, help debug, and more.
They are powerful, but limited in capability.
They are typically constrained to **producing text**
(or speech) as requested by a user.
The early chatbot can't open files,
run anything, or otherwise act in the world.
We read what it says and we decide what to do.

That boundary changes with **agents**.

## Agentic AI (Brings New Capabilities)

Agentic AI goes further.
An AI system becomes more **agentic** when it can:

- inspect files,
- read a project,
- modify code,
- run commands,
- use tools,
- call services,
- create pull requests, or
- act inside a workspace.

These additional **capabilities** mean the agent can **take actions**
that a typical chatbot cannot.
This changes the **risk** and the associated **responsibility** significantly.

## Capability is a Dial

Just because we build agents that **can** execute actions,
does not mean that they **should**.

It may be helpful to imagine a dashboard of dials,
one for each capability,
measuring how much a system is allowed to do.

Before, the systems had one dial: respond.

But now, the capabilities are proliferating, and the dials
can go higher,
depending on what the agent has been connected to
and permitted to use:

- Text-Only: the agent answers; we read and decide.
- Retrieval: the agent can search and fetch content to include in its reply.
- Read-Only: the agent can open files, projects, and data.
- Actions: the agent can edit files, author files, run commands, call tools and services.
- Multi-Step Agency: the agent can pursue a goal across steps
  with differing reviews and approvals at each step.
  These agents can read an entire repository, write tests,
  and prepare a commit or pull request for us.
  (e.g.,  the GitHub "Agents" tab or Claude Code.)

Notice what changes as we work down the list.
It's not the agent "intelligence".

What grows is the agent **access**:
how much it can touch,
and how directly its actions land
without a person checking each one.

Increasing access tends to mean increasing risk.
Power increases what we might call the blast radius:
how much can go wrong,
and how hard it is to undo,
if the system gets confused
or asked for the wrong thing.

And, as agent capabilities expand,
they do not necessarily become more responsible.
Agent capabilities do not confer maturity or wisdom.

A tool may be **able** to do something that it
**should not be allowed to do** without review.

## Managing the Controls

As we keep adding capabilities, and dialing them up,
the agents increasingly become more autonomous,
with broader access,
and possibly the ability to acquire resources,
spend money, copy itself, operate across many systems,
and persuade people.

At that point, agents are acting beyond a single repository.

They are becoming systems acting in the open world.

Researchers and institutions study risks
ranging from misuse and accidents
up to scenarios some argue could be catastrophic for humanity.

We don't have to take a position on how likely a risk is to
recognize the shape of the concern.
Those of us building and using AI can already see it:
it's the blast-radius question with the radius set large,
and our ability to review, authorize, and stop the systems
may be lagging behind what we think the systems can do.

When we pause before acting and ask

> Before I run this, what could it touch, and what's the blast radius if it's wrong?

We are practicing with safer, smaller stakes
the exact discipline the field is trying to build
as these systems grow.

## Responsible AI Use

Responsible AI use means knowing what outcomes we want,
and understanding what the tool can access
and what it could change.
It means understanding what impacts that access and objective could have.

Unintended authorization by anyone, anywhere can have unintended consequences.

People using power tools must act responsibly.

As agentic capabilities increase, we must be able to answer:

- What tool did I use?
- What did I ask it to do?
- Could it read my files or project?
- Could it modify files?
- Could it run commands?
- Could it access external services?
- What actions and updates have I accepted?
- How careful was my review?
- Am I being a responsible power user?

## AI Governance

AI governance helps powerful tools remain useful, safe, inspectable,
and accountable.

In professional projects, governance may include:

- version control,
- review before merging,
- tests,
- logs,
- clear documentation,
- dependency checks,
- security checks,
- protected files,
- generated artifacts,
- and explicit review requirements.

Sound practices can reduce avoidable mistakes.
Good procedures and workflows help teams understand what changed, why it changed,
and ensure proper review and documentation.

## Accountable Surfaces

Some files and workflows carry more authority than others.

Examples include:

- setup instructions,
- assignment instructions,
- grading expectations,
- dependency files,
- workflow files,
- release instructions,
- security policies,
- AI-use policies,
- and repository governance files.

These are examples of **accountable surfaces**.

An accountable surface is a part of a project where the technical ability
to make a change is not enough. The change may require human review,
supporting evidence, or additional care.

This project uses accountable surfaces because the content
affects what tools people install on their machines,
and helps inform the critical professional habits related to these powerful tools.

## In Practice

Use AI to learn and work responsibly.
Do not use AI as a way to avoid understanding.

As AI tools become more capable, our professional skill
is not just being able to use them well.
Our professional skill includes knowing when a tool
has been given additional capability,
understanding the potential risk that can create,
and knowing how to manage the risks and rewards **before** requesting the result.

Responsibility for all outcomes
remain with the people and institutions that
build, release, deploy, authorize, operate, and review these systems.
