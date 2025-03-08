---
title: Quick Tips on Using LLMs Effectively
date: 2025-02-02
---

# **Quick Tips on Using LLMs Effectively**

All right, this is going to be my own attempt at compiling some fun examples of how to prompt LLM models effectively to do useful stuff.

## **Prompt Iteratively**

I think it was Jeremy Howard who coined this term ['Dialog Engineering'](https://arc.net/l/quote/vjuccuvd) where you build and engineer things through talking to an LLM in small steps.

This could not be more true. Prompt atomically, for example: instead of asking a model to build a 'quiz app' maybe ask the model to:

1. "Design a basic data structure for quiz questions and answers"
2. "Create a function to load and parse quiz questions from a JSON file" 
3. "Build a simple command-line interface to display questions and accept user input"
4. "Add scoring logic to track correct/incorrect answers"
5. "Implement a way to save quiz results and show final score"

Something like that where you prompt in small pieces and for each you supervise the result and incrementally grow into the final result you were looking for.

This is a perfect segway to my next tip.

## **Use LLMs as assistants not as replacements**

Don't treat whatever is generated with an AI as the final all might output.
Treat everything you get from it critically, which I know can sound a bit contradictory given the nature of why we are using LLMs right? We are using it so we don't have to do the work. However, this approach can only lead to hours of mindless debugging and absolute dread. 

Instead, treat the model like the great [Simon Willison](https://simonwillison.net/) puts it in this [youtube video](https://www.youtube.com/watch?v=uRuLgar5XZw&t=78s) where he mentions you should treat them as "smart interns" that "read through all the documentation" and can help 24/7.

> [I think you should use them as supporting like tools to support support the decisions that you're making... - Simon Willison ](https://www.youtube.com/watch?v=uRuLgar5XZw&t=78s)

## **Ask for Multiple Options**

Specially for tought questions, don't ask the models for one answer, ask for many and pick the ones that looks best.

## **Use it to Explore and Not Just for Quick Answers**

Do side projects with these tools and explore what they can do instead of 
relying on them just as a google search replacement.

## **Explore and Experiment**

When working with AI tools, it's important to approach them with a spirit of exploration and experimentation rather than just using them for quick answers. Here are some key ways to do this:

Challenge yourself to do complete projects using AI tools. As one developer put it: *"If you can afford to do a side project with these tools and like set yourself a challenge to write every line of code with these tools, I think that's a great thing you can do."*
