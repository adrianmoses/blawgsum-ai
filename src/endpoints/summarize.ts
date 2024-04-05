import {
    OpenAPIRoute,
    OpenAPIRouteSchema,
} from "@cloudflare/itty-router-openapi";
import { Ai } from '@cloudflare/ai'
import {SummarizePrompt, SummarizeResponse} from "../types";
import type { AiEnv } from "../types";

export class Summarize extends OpenAPIRoute {
    static schema: OpenAPIRouteSchema = {
        tags: ["Text"],
        summary: "Summarize text",
        requestBody: SummarizePrompt,
        responses: {
            "200": {
                description: "Returns the summarized text",
                schema: SummarizeResponse,
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
            input_text: data.body.text,
            max_length: data.body.maxLength
        }

        const response  = await ai.run(
            "@cf/facebook/bart-large-cnn",
            inputs
        )

        return {
            text: response.summary
        }
    }
}