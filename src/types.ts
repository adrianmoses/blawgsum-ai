import { Str, Int } from "@cloudflare/itty-router-openapi";

export const ImagePrompt = {
	prompt: new Str({ example: "an elephant made of leaves" }),
};

export const SpellCheckPrompt = {
	text: new Str({ example: "This is a test" }),
};

export const GrammarCheckPrompt = {
	text: new Str({ example: "This is a test" }),
};

export const SummarizePrompt = {
	text: new Str({ example: "This is a test" }),
	maxLength: new Int({ example: 1024 })
};

export const TranslatePrompt = {
	text: new Str({ example: "This is a test" }),
	sourceLanguage: new Str({ example: "en" }),
	targetLanguage: new Str({ example: "es" }),
};

export const Image = {
	contentType: String,
	data: String,
}

export const SpellCheckResponse = {
	text: String,
}

export const SummarizeResponse = {
	summary: String
}
export interface AiEnv {
	AI: any;
}