# blawgsum-ai
FastAPI service used for AI Content Features



API service that offers content generation endpoints
- spell check and grammar check
- summarize
- translate
- adjust tone
- rephrase
- emojify
- extend
- generate on prompt
- image generation
- completion (RAG-supported)


Multiple models or services can be used
- hf (and model choice)
- ollama
- cohere
- openAI

Where hf and ollama could support llama or mixtral, etc

But the endpoints would choose the right ones and the support would be based on those specific endpoints

So first let's start with openAI and cohere just to make sure we can support everything

Use pinecone for rag and langchain for easy interopibility

Question is how to start using RAG?

We could just find docs and ingest them. Or build a Doc Ingestor in Blawgsum

It would be based on a topic (and I guess providing some general topics would be super helpful)

But that's a different project technically and should not be the focus for this.

TODO:
Build "api" response and an authorization header check

With that create a content generation folder with files that match the api endpoints

For now just focus on an object that can call the right model based on a value

