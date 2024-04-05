import { OpenAPIRouter } from "@cloudflare/itty-router-openapi";
import {ImageCreate} from "./endpoints/imageCreate";
import {SpellCheck} from "./endpoints/spellCheck";
import {GrammarCheck} from "./endpoints/grammarCheck";
import {Translate} from "./endpoints/translate";
import {Summarize} from "./endpoints/summarize";

export const router = OpenAPIRouter({
	docs_url: "/",
});

router.post("/api/image", ImageCreate);
router.post("/api/spellcheck", SpellCheck);
router.post("/api/grammarcheck", GrammarCheck);
router.post("/api/translate", Translate);
router.post("/api/summarize", Summarize)

// 404 for everything else
router.all("*", () =>
	Response.json(
		{
			success: false,
			error: "Route not found",
		},
		{ status: 404 }
	)
);

export default {
	fetch: router.handle,
};
