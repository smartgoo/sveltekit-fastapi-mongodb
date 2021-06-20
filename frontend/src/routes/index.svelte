<script context="module">
	// see https://kit.svelte.dev/docs#loading
	export async function load({ fetch }) {
		const res = await fetch('http://backend:8000/api/v1/demo/posts');

		if (res.ok) {
			const data = await res.json();
            const posts = data

			return {
				props: { posts }
			};
		}

		const { message } = await res.json();

		return {
			error: new Error(message)
		};
	};
</script>


<script>
    export let posts;
</script> 


<div class="container">
    {#each posts as post}
		<h1>{post.title}</h1>
		<h4>Publish date: {post.date}</h4>
		<p>{post.text}</p>
	{/each}
</div>
