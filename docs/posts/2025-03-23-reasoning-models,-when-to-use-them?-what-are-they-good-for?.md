---

title: Reasoning Models, When to Use Them? What Are They Good for?
date: 2025-03-23

# Reasoning Models, When to Use Them? What Are They Good for?
---

## What's a Reasoning Model?

I guess I want to start this conversation by defining what a thinking/reasoning model is. The easiest way to define it is that it is a model specially trained and designed for thinking through problems. 

Now, the more elaborate way of going about this definition is to look into the information we have about what differs between these models and the traditional models we are used to like ChatGPT or Claude.

??? notes "How Reasoning models differ from Traditional LLMs"

    Reasoning models differ from traditional LLMs in several key ways:

    - **Computational Approach**: While traditional LLMs generate text in a fixed number of passes and are optimized for efficiency, reasoning models allocate variable computation time based on problem complexity and implement explicit "thinking" phases.

    - **Problem-Solving Methods**: Traditional LLMs rely primarily on pattern recognition, while reasoning models utilize explicit step-by-step reasoning processes and show their work through intermediate steps.

    - **Training Methodology**: Reasoning models are trained on specialized datasets focused on reasoning tasks and use reinforcement learning with rewards specifically for reasoning quality.

    - **Output Characteristics**: Reasoning models produce more structured, methodical responses with explicit verification steps and self-critique, prioritizing logical correctness over natural-sounding language.
    
    - **Chain of Thought (CoT) Processing**: Models like o1 and DeepSeek R1 implement extensive chain-of-thought reasoning, breaking down complex problems into manageable steps before providing answers.

The way I like to think about them for the purpose of building stuff with them is this: 
> It's a model that gives you almost guaranteed better performance at the expense of latency and cost.

So it's essentially a __better yet slower model__. 

I think looking at it from this perspective will help us define a framework for thinking about them effectively.

---

## How do we Know they're Better?

Well, if you go to <a href="www.artificialanalysis.ai"> Artificial Analysis </a> and check out their independent evaluation of different models, you will see that their performance against other models for different indexes of capabilities like intelligence (performance in intelligence related tasks) almost always come out on top.

According to recent benchmarks, reasoning models consistently outperform traditional LLMs on tasks requiring complex logical thinking, mathematical problem-solving, and coding challenges. For example, DeepSeek R1 has demonstrated superior performance on mathematical reasoning compared to many general-purpose models, while Claude 3.7 Sonnet with extended thinking enabled shows remarkable improvements over its standard mode.

The performance gap is particularly noticeable in:
- Complex mathematical problems
- Multi-step logical puzzles
- Detailed code generation with explanations
- Step-by-step problem-solving in scientific domains

However, it's worth noting that this superior performance comes with trade-offs in speed and computational cost, which I'll discuss later.

## Which Models we can officially call Reasoning Models?

Let's make a little list of the current leading reasoning models:

1. **Deep Seek R1** - An open-source 671B parameter model that excels in mathematical reasoning and has distilled versions available
2. **OpenAI o-series models** - Including o1, o1-mini, o1-pro, o3-mini, and o3-mini-high, specifically designed for extended reasoning
3. **Claude 3.7 Sonnet** - With "extended thinking" mode activated, becoming a hybrid reasoning/general model
4. **Grok-3** - xAI's latest model with enhanced reasoning capabilities
5. **Gemini 2.0 Flash/Advanced** - Google's reasoning-focused models
6. **Sky T-1** - A relatively new Chinese reasoning model from SkyWork
7. **Baidu's ERNIE 4.0-Reasoning** - Launched in March 2025 as a competitor to DeepSeek R1
8. **Tencent's T1** - A reasoning model introduced in early 2025
9. **Llama-3-70B-Instruct** - While not explicitly marketed as a reasoning model, it shows strong reasoning capabilities

This list is continually growing as more companies release specialized reasoning models to compete in this rapidly evolving space.

## When Should You Use Reasoning Models?

Reasoning models shine in specific scenarios, but they're not always the right choice. Here's my take on when they make sense:

### 1. Complex Problem-Solving

If your use case involves solving intricate problems that require breaking down complex logic into steps, reasoning models are your best bet. They excel at:

- Mathematical challenges
- Logic puzzles
- Scientific reasoning
- Step-by-step explanations

### 2. Code Generation and Analysis

For software development tasks requiring thoughtful analysis, reasoning models offer significant advantages:

- Writing complex algorithms
- Debugging with systematic approaches
- Explaining code behavior comprehensively
- Architecture design with logical justification

### 3. High-Stakes Decision Support

When accuracy and reliability are paramount:

- Financial analysis where errors could be costly
- Medical reasoning requiring careful consideration
- Legal analysis with logical chains of thought
- Risk assessment requiring thorough evaluation

### 4. Educational Applications

For tools designed to teach or explain complex topics:

- Tutorial systems requiring step-by-step instruction
- Math problem solving with shown work
- Scientific concept explanations
- Knowledge exploration with logical connections

## When Traditional LLMs Might Be Better

Despite their impressive capabilities, reasoning models aren't always the optimal choice:

1. **Speed-Critical Applications**: When response time matters more than deep thinking
2. **Creative Content Generation**: For stories, marketing copy, or creative writing
3. **Casual Conversation**: When natural dialogue flow is more important than rigorous logic
4. **High-Volume, Simple Tasks**: For straightforward, repetitive tasks where the computational overhead isn't justified

## The Performance-Latency Trade-off

This is perhaps the most critical consideration when deciding whether to implement reasoning models. They typically:

- Take significantly longer to respond (sometimes 5-10x longer)
- Consume more tokens (and therefore cost more)
- Require more computational resources
- Provide more thorough, accurate results for complex problems

In my experience, this trade-off means you should be selective about when to deploy reasoning capabilities. For many applications, a hybrid approach works best:

- Use standard LLMs for straightforward queries and initial interactions
- Switch to reasoning modes for complex questions
- Allow users to choose whether they want quick answers or deeper analysis

## How to Prompt Reasoning Models Effectively

Interestingly, prompting reasoning models often requires a different approach than traditional LLMs. Based on OpenAI's official guidance and my own experimentation:

1. **Keep prompts simple and direct** - Contrary to what you might expect, you often don't need to explicitly tell reasoning models to "think step by step." They're already designed to do this.

2. **Structure complex problems clearly** - Use delimiters and clear formatting to separate different parts of your input.

3. **For mathematical or logical problems**, provide:
   - Clear problem statements
   - Relevant context
   - Expected output format

4. **Model-specific considerations**:
   - For OpenAI's o-series, "developer messages" replace traditional system messages
   - Claude 3.7 Sonnet requires explicit activation of extended thinking mode
   - DeepSeek R1 excels with mathematical reasoning when given clean, well-structured problems

5. **Use verification steps for critical applications** - Ask the model to verify its own work when accuracy is paramount.

## Implementation Considerations

If you're planning to implement reasoning models in your applications, consider these practical factors:

### 1. Cost Management

Reasoning models typically:
- Process more tokens per request
- Take longer to generate responses
- May require premium API access

Implement strategies like:
- Selective use for complex queries only
- Caching common reasoning patterns
- User-controlled access to reasoning capabilities

### 2. Latency Handling

The extended processing time requires thoughtful UX design:
- Implement streaming for progressive response display
- Show intermediate reasoning steps as they're generated
- Provide clear user expectations about response times

### 3. Hybrid Architectures

Consider architectures that combine:
- Traditional LLMs for routine queries
- Reasoning models for complex problems
- Distilled reasoning models as a middle ground
- Human review for critical applications

### 4. The Role of Distilled Models

An exciting development is the emergence of distilled reasoning models like DeepSeek-R1-Distill-Qwen-32B, which:
- Retain 80-95% of the reasoning capabilities of larger models
- Run on more modest hardware
- Offer faster inference times
- Provide a cost-effective middle ground

For many practical applications, these distilled models hit the sweet spot between performance and efficiency.

## The Future of Reasoning Models

We're just at the beginning of the reasoning model era, and I expect rapid developments:

- More efficient reasoning approaches that reduce latency
- Specialized reasoning models for specific domains (medical, legal, financial)
- Improved distillation techniques preserving more reasoning capabilities
- Better integration of reasoning with multimodal capabilities

The competition between open-source models like DeepSeek R1 and proprietary offerings like OpenAI's o-series is driving innovation at a remarkable pace, with the performance gap between them narrowing significantly.

## Conclusion

Reasoning models represent a significant advancement in AI capabilities, offering new possibilities for applications requiring thoughtful, methodical problem-solving. They're not a replacement for traditional LLMs but rather a specialized tool for specific use cases where depth of thinking matters more than speed.

When implementing them, focus on:
1. Selecting the right use cases where their advantages justify the trade-offs
2. Designing user experiences that manage expectations around response times
3. Considering hybrid approaches that leverage different model types appropriately
4. Exploring distilled models as a balanced option for many applications

As these models continue to evolve, they'll enable increasingly sophisticated applications that tackle problems previously beyond the reach of AI systems. The key is understanding their unique characteristics and implementing them thoughtfully where they add the most value.

What are your experiences with reasoning models? Have you found particular applications where they shine? Let me know in the comments below!
