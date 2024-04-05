import {
    OpenAPIRoute,
    OpenAPIRouteSchema,
} from "@cloudflare/itty-router-openapi";
import { Ai } from '@cloudflare/ai'
import { SpellCheckPrompt } from "../types";
import type { AiEnv } from "../types";

interface GemmaResponse {
    response: string
}
export class SpellCheck extends OpenAPIRoute {
    static schema: OpenAPIRouteSchema = {
        tags: ["SpellCheck"],
        summary: "Spell check a text",
        requestBody: SpellCheckPrompt,
        responses: {
            "200": {
                description: "Returns the spell checked text",
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
            { role: "user", content: `You are a spell checker that looks for mistakes in the user's provided text. 
                You take in all the user input and auto correct it. Just reply to user input with the correct spelling.
                If the user input is spelled correctly, just reply "ok". Here's the user input: ${inputs.text}`
            }
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