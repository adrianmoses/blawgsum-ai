import {
    OpenAPIRoute,
    OpenAPIRouteSchema,
} from "@cloudflare/itty-router-openapi";
import { Ai } from '@cloudflare/ai'
import {TranslatePrompt} from "../types";
import type { AiEnv } from "../types";

const languageCodes = ["english",
    "spanish",
    "french",
    "german",
    "italian",
    "portuguese",
    "dutch",
    "russian",
    "japanese",
    "chinese",
    "korean",
    "arabic",
    "turkish",
    "hindi",
    "indonesian",
    "vietnamese",
    "thai",
    "greek",
    "hebrew",
    "swedish",
    "danish",
    "norwegian",
    "finnish",
    "czech",
    "polish",
    "hungarian",
    "romanian",
    "ukrainian",
    "catalan",
    "vietnamese",
    "tagalog",
    "malay",
    "swahili",
    "afrikaans",
    "esperanto",
    "latin",
    "welsh",
    "scots gaelic",
    "irish",
    "icelandic",
    "farsi",
    "serbian",
    "croatian",
    "bosnian",
    "slovak",
    "slovenian",
    "estonian",
    "latvian",
    "lithuanian",
    "maltese",
    "albanian",
    "macedonian",
    "kurdish",
    "armenian",
    "georgian",
    "basque",
    "galician",
    "catalan",
    "corsican"]

export class Translate extends OpenAPIRoute {
    static schema: OpenAPIRouteSchema = {
        tags: ["Translate"],
        summary: "Translate a text",
        requestBody: TranslatePrompt,
        responses: {
            "200": {
                description: "Returns the translated text",
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
            source_lang: data.body.sourceLanguage,
            target_lang: data.body.targetLanguage,
        }

        if (!languageCodes.includes(inputs.source_lang.toLowerCase())) {
            return Response.json({
                text: "Invalid source language"
            })
        }

        if (!languageCodes.includes(inputs.target_lang.toLowerCase())) {
            return Response.json({
                text: "Invalid target language"
            })
        }

        const response = await ai.run(
            "@cf/meta/m2m100-1.2b",
            inputs
        );

        return Response.json({
            text: response.translated_text
        })
    }
}