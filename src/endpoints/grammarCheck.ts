import {
    OpenAPIRoute,
    OpenAPIRouteSchema,
} from "@cloudflare/itty-router-openapi";
import { Ai } from '@cloudflare/ai'
import { GrammarCheckPrompt } from "../types";
import type { AiEnv } from "../types";

interface GemmaResponse {
    response: string
}
export class GrammarCheck extends OpenAPIRoute {
    static schema: OpenAPIRouteSchema = {
        tags: ["GrammarCheck"],
        summary: "Grammar check a text",
        requestBody: GrammarCheckPrompt,
        responses: {
            "200": {
                description: "Returns the grammar checked text",
                schema: {},
            },
        },
    };

    async handle(
        request: Request,
        env: AiEnv,
        context: any,
        data: Record<string, any>
    ) {
        // Retrieve the validated request body
        const ai = new Ai(env.AI);

        const inputs = {
            text: data.body.text,
        }
        const messages = [
            { role: "system", content: "You are a spell and grammar checker that looks for mistakes in the user's provided text."},
            { role: "user", content: `You are a grammar checker that looks for mistakes in the user's provided text. 
            You take in all the user input and auto correct it. Just reply to user input with the correct grammar. 
            If the user input is grammatically correct, just reply "ok". Here's the user input: ${inputs.text}`}
        ]


        // @ts-ignore
        const response: GemmaResponse = await ai.run("@hf/google/gemma-7b-it",
            { messages }
        )

        console.log(response)
        const responseText = response.response

        return Response.json({
            text: responseText
        })
    }
}
