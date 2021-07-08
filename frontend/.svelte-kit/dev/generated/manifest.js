const c = [
	() => import("../../../src/routes/__layout.svelte"),
	() => import("../components/error.svelte"),
	() => import("../../../src/routes/index.svelte"),
	() => import("../../../src/routes/tutorials.svelte"),
	() => import("../../../src/routes/articles.svelte"),
	() => import("../../../src/routes/contact.svelte"),
	() => import("../../../src/routes/admin/login.svelte")
];

const d = decodeURIComponent;

export const routes = [
	// src/routes/index.svelte
	[/^\/$/, [c[0], c[2]], [c[1]]],

	// src/routes/tutorials.svelte
	[/^\/tutorials\/?$/, [c[0], c[3]], [c[1]]],

	// src/routes/articles.svelte
	[/^\/articles\/?$/, [c[0], c[4]], [c[1]]],

	// src/routes/contact.svelte
	[/^\/contact\/?$/, [c[0], c[5]], [c[1]]],

	// src/routes/admin/login.svelte
	[/^\/admin\/login\/?$/, [c[0], c[6]], [c[1]]]
];

export const fallback = [c[0](), c[1]()];